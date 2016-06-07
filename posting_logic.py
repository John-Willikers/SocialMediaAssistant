import twitter
import facebook
import social_list


def check_facebook():
    if social_list.run_to_posting_fb():
        fb = True
        return fb
    elif not social_list.run_to_posting_fb():
        fb = False
        return fb


def check_twitter():
    if social_list.run_to_posting_tw():
        tw = True
        return tw
    if not social_list.run_to_posting_tw():
        tw = False
        return tw


def load_credentials(keyloc):
    file_k = open(keyloc, 'r')
    key = file_k.read()
    return key

consumer_key = load_credentials('./social keys/twitter-consumer_key.key')
consumer_secret = load_credentials('./social keys/twitter-consumer_secret.key')
access_token_key = load_credentials('./social keys/twitter-access_token_key.key')
access_token_secret = load_credentials('./social keys/twitter-access_token_secret.key')

fb_access_token = load_credentials('./social keys/facebook-access_token.key')

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

graph = facebook.GraphAPI(access_token=fb_access_token, version='2.2')


def post(msg, platform):
    if platform == 'all':
        if check_facebook():
            print('[Facebook]: Attempting to post: | ' + msg + ' | to wall.\n')
            choice = raw_input('[Y/N]')
            if choice.lower() == 'y':
                try:
                    graph.put_object(parent_object='me', connection_name='feed', message=msg)
                    print('[Facebook]: Message Posted.')
                except facebook.GraphAPIError:
                    print('[Error]: There was an Error posting the message. Check to make sure your\n'
                          'Access Token is still use-able.\n')
            elif choice.lower() == 'n':
                print(' ')
        elif not check_facebook():
            print('[Error]: Facebook has not been setup for posting to. Please type login, then facebook after\n'
                  '         to add your access token. This whole process will be explained over there.')
        if check_twitter():
            print('[Twitter]: Attempting to post: | ' + msg + ' | to wall.\n')
            choice = raw_input('[Y/N]')
            if choice.lower() == 'y':
                try:
                    api.PostUpdate(msg)
                    print('[Twitter]: Message Posted.')
                except facebook.GraphAPIError:
                    print('[Error]: There was an Error posting the message. Check to make sure your\n'
                          'Access Token is still use-able.\n')
            elif choice.lower() == 'n':
                return 1
        elif not check_twitter():
            print('[Error]: Twitter has not been setup for posting to. Please type login, then twitter after\n'
                  '         to add your access token. This whole process will be explained over there.')
        raw_input('Press enter key to continue.')
    elif platform == 'facebook':
        if check_facebook():
            print('[Facebook]: Attempting to post: | ' + msg + ' | to wall.\n')
            choice = raw_input('[Y/N]')
            if choice.lower() == 'y':
                try:
                    graph.put_object(parent_object='me', connection_name='feed', message=msg)
                    print('[Facebook]: Message Posted.')
                except facebook.GraphAPIError:
                    print('[Error]: There was an Error posting the message. Check to make sure your\n'
                          'Access Token is still use-able.\n')
            elif choice.lower() == 'n':
                return 0
        elif not check_facebook():
            print('[Error]: Facebook has not been setup for posting to. Please type login, then facebook after\n'
                  '         to add your access token. This whole process will be explained over there.')
        else:
            print('[Error]: Facebook Variable is neither true nor false. Please restart the application to\n'
                  '         fix this error or contact the developer @ lonelyretardxd@gmail.com')
        raw_input('Press enter key to continue.')
    elif platform == 'twitter':
        if check_twitter():
            print('[Twitter]: Attempting to post: | ' + msg + ' | to wall.\n')
            choice = raw_input('[Y/N]: ')
            if choice.lower() == 'y':
                try:
                    api.PostUpdate(msg)
                    print('[Twitter]: Message Posted.')
                except twitter.error.TwitterError:
                    print('[Error]: There was an Error posting the message. Check to make sure your\n'
                          '4 Access Tokens are still use-able.\n')
            elif choice.lower() == 'n':
                return 0
        elif not check_twitter():
            print('[Error]: Twitter has not been setup for posting to. Please type login, then twitter after\n'
                  '         to add your access token. This whole process will be explained over there.')
        else:
            print('[Error]: Twitter Variable is neither true nor false. Please restart the application to\n'
                  '         fix this error or contact the developer @ lonelyretardxd@gmail.com')
        raw_input('Press enter key to continue.')
    else:
        print('[Error]: Incorrect command. Please use either facebook, twitter, or all.')
        input('Press enter key to continue.')
