import os

is_alive = True


def log_key(keyvalue, filedir):
    if not os.path.exists(filedir):
        file_kv = open(filedir, 'w')
        file_kv.write(keyvalue)
        file_kv.close()
    elif os.path.exists(filedir):
        os.remove(filedir)
        file_ky = open(filedir, 'w')
        file_ky.write(keyvalue)
        file_ky.close()


def login():
    while is_alive:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('+-----------------------------------------------+\n'
              '|  Please enter the command below to start the  |\n'
              '|  login process for that social platform.      |\n'
              '|  Follow the directions EXPLICITLY             |\n'
              '+-----------------------------------------------+')
        print('Commands:\n'
              '- twitter\n'
              '- facebook\n')
        choice = raw_input('Enter Command: ')
        if choice == 'twitter':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('The twitter login requires four different keys:\n'
                  '- Consumer Key\n'
                  '- Consumer Secret\n'
                  '- Access Token Key\n'
                  '- Access Token Secret\n'
                  '\n'
                  'Watch this video to figure out your keys:\n'
                  'https://www.youtube.com/watch?v=KDdNMrueGQs\n'
                  '\n')
            consumer_key = raw_input('Please input your Consumer Key: ')
            consumer_secret = raw_input('Please input your Consumer Secret: ')
            access_token_key = raw_input('Please input your Access Token Key: ')
            access_token_secret = raw_input('Please input your Access Token Secret: ')
            log_key(consumer_key, './social keys/twitter-' + 'consumer_key.key')
            log_key(consumer_secret, './social keys/twitter-' + 'consumer_secret.key')
            log_key(access_token_key, './social keys/twitter-' + 'access_token_key.key')
            log_key(access_token_secret, './social keys/twitter-' + 'access_token_secret.key')
            if not os.path.exists('./settings/twitter_status.sta'):
                file_s = open('./settings/twitter_status.sta', 'w')
                file_s.write('true')
                file_s.close()
            elif os.path.exists('./settings/twitter_status.sta'):
                os.remove('./settings/twitter_status.sta')
                file_c = open('./settings/twitter_status.sta', 'w')
                file_c.write('true')
                file_c.close()
            break
        elif choice == 'facebook':
            print('The facebook login requires one key:\n'
                  '- Access Token\n'
                  '\n'
                  'Read this Tutorial to figure it all out:\n'
                  'https://smashballoon.com/custom-facebook-feed/access-token/ \n'
                  '\n')
            access_token = raw_input('Please input your Access Token: ')
            log_key(access_token, './social keys/facebook-' + 'access_token.key')
            if not os.path.exists('./settings/facebook_status.sta'):
                file_s = open('./settings/facebook_status.sta', 'w')
                file_s.write('true')
                file_s.close()
            elif os.path.exists('./settings/facebook_status.sta'):
                os.remove('./settings/facebook_status.sta')
                file_c = open('./settings/facebook_status.sta', 'w')
                file_c.write('true')
                file_c.close()
            break
