'''
	Get data about 100 Twitch streams. Mincraft game (game_id=512980).
	application name : Get_Streams_Data
	Client ID / Client Secret Get_Streams_Data in password.txt file
'''
import sys
import getopt


class getStreams:

    def __init__(self):
        self.__clientID = ''
        self.__clientSecret = ''
        self.__OAuthToken = ''

    def setClientID(self, clientID):
        self.__clientID = clientID

    def setClientSecret(self, clientSecret):
        self.__clientSecret = clientSecret

    def getClientID(self):
        return self.__clientID

    def getClientSecret(self):
        return self.__clientSecret

    def getOAuthToken(self):
        pass

    def run(self):
        pass


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

    print('Great we got your Client ID and secret ')
    for opt, val in opts:
        if opt == '-h':
            print(help_meg)
            sys.exit(0)
        elif opt == '-i':
            Twitch_Streams.setClientID(val)
        elif opt == '-s':
            Twitch_Streams.setClientSecret(val)

    # check
    print(f'CLient ID {Twitch_Streams.getClientID()}')
    print(f'CLient secret {Twitch_Streams.getClientSecret()}')


if __name__ == '__main__':
    main(sys.argv[1:])
