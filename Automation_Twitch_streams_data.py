'''
	Get data about 100 Twitch streams. Mincraft game (game_id=512980).
	application name : Get_Streams_Data
	Client ID / Client Secret Get_Streams_Data in password.txt file
'''
import sys
import getopt


def main(args):
    help_meg = 'Automation_Twitch_streams_data.py  -i <clientID> -s <clientSecret>'

    try:
        opts, args = getopt.getopt(
            args, 'h:i:s', ['clientID=', 'clientSecret='])
    except getopt.GetoptError as msg:
        print(msg)
        print(help_meg)
        sys.exit(2)

    print('Great we got your Client ID and secret')
    for opt, val in opts:
        if opt == '-h':
            print(help_meg)
            sys.exit(0)
        elif opt == '-i':
            print(f'Client ID {val} ')
        elif opt == '-s':
            print(f'Client Secret {val} ')


if __name__ == '__main__':
    main(sys.argv[1:])
