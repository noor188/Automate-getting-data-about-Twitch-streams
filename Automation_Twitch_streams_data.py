'''
	Get data about 100 Twitch streams. Mincraft game (game_id=512980).
	application name : Get_Streams_Data
	Client ID / Client Secret Get_Streams_Data in password.txt file
'''
import sys
import getopt
import requests
import json


class getStreams:

    def __init__(self):
        self.__clientID = ''
        self.__clientSecret = ''
        self.__OAuthToken = ''
        self.__StreamsURL = 'https://api.twitch.tv/helix/streams?first=100&language=en&&game_id=512980'
        self.__outputFile = ''

    def setClientID(self, clientID):
        self.__clientID = clientID

    def setClientSecret(self, clientSecret):
        self.__clientSecret = clientSecret

    def getClientID(self):
        return self.__clientID

    def getClientSecret(self):
        return self.__clientSecret

    def getOAuthToken(self):

        try:
            # POST: To submit data to be processed to the Twitch server
            return requests.post(f"https://id.twitch.tv/oauth2/token"
                                 f"?client_id={self.__clientID}"
                                 f"&client_secret={self.__clientSecret}"
                                 f"&grant_type=client_credentials").json()['access_token']
        except:
            return None

    def run(self):

        if self.__clientID == '':
            print("If you don't have a client ID get one from this page :")
            print("https://dev.twitch.tv/console/apps")
            return

        if self.__clientSecret == '':
            print("If you don't have a clientSecret get one from this page")
            print("https://dev.twitch.tv/console/apps")
            return

        print('\n \n *** Welcome to Automate Twitch streams application *** \n')

        print('Getting the Authorization to access Twitch resources ......')
        self.__OAuthToken = self.getOAuthToken()
        print('\nGot the authorization succesfully !')

        print("\nStart Getting 100 streams metadata .... \n ")
        headers = {'Content-Type': 'application/json',
                   'Client-ID': self.__clientID,
                   'Authorization': f'Bearer {self.__OAuthToken}'
                   }
        # GET: To request data from the Twitch server
        oneHandredStreams = requests.get(
            self.__StreamsURL, headers=headers).json()['data']
        print(f"Stored the data succesfully in {self.__outputFile}")


def main(args):
    Twitch_Streams = getStreams()
    help_meg = 'Automation_Twitch_streams_data.py  -i <clientID> -s <clientSecret>'

    try:
        opts, args = getopt.getopt(
            args, 'h:s:i:', ['clientID=', 'clientSecret='])
    except getopt.GetoptError as msg:
        print(msg)
        print(help_meg)
        sys.exit(2)

    #print('Great we got your Client ID and secret ')
    for opt, val in opts:
        if opt == '-h':
            print(help_meg)
            sys.exit()
        elif opt in ('-i', '--clientID'):
            Twitch_Streams.setClientID(val)
        elif opt in ('-s', '--clientSecret'):
            Twitch_Streams.setClientSecret(val)

    # check
    #print(f'CLient ID {Twitch_Streams.getClientID()}')
    #print(f'CLient secret {Twitch_Streams.getClientSecret()}')
    #print(f'OAuth token {Twitch_Streams.getOAuthToken()}')
    Twitch_Streams.run()


if __name__ == '__main__':
    main(sys.argv[1:])
