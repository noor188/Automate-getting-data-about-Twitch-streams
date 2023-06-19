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
        self.__StreamsURL = r'https://api.twitch.tv/helix/streams?first=100&language=en&&game_id=512980'
        self.__outputFile = r'oneHundredStreamsData'

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

        # POST: To submit clientID/secret to be processed to the Twitch server
        self.POSTOauthToken()

        # Get 100 streams data
        oneHandredStreams = self.GETStreamsData()

        self.storeToFile(oneHandredStreams)

    def POSTOauthToken(self):
        # ************** POST / Oauth token ************** #
        print('Getting the Authorization to access Twitch resources ......')
        self.__OAuthToken = self.getOAuthToken()

        if self.__OAuthToken == '':
            print("Could not get the Oauth toke ")
            return

        print('\nGot the authorization succesfully !')

    def GETStreamsData(self):

        print("\nStart Getting 100 streams data .... \n ")
        headers = {'Content-Type': 'application/json',
                   'Client-ID': self.__clientID,
                   'Authorization': f'Bearer {self.__OAuthToken}'
                   }

        try:
            # GET: To request data from the Twitch server
            oneHandredStreams = requests.get(
                self.__StreamsURL, headers=headers).json()['data']
        except requests.exceptions.RequestException as errex:
            print('Error in HTTP get')
        return oneHandredStreams

    def storeToFile(self, oneHandredStreams):
        print(
            f"Storing the 100 streams data into \{self.__outputFile}\output.txt file")
        with open(f'{self.__outputFile}/output.txt', "w") as file1:
            # file1.write(oneHandredStreams)
            json.dump(oneHandredStreams, file1, indent=4)
            pass

        print(f"Stored the data succesfully!")


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
