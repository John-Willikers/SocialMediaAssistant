import os


def set_status(social):
    if not os.path.exists('./settings/' + social + '_status.sta'):
        file_s = open('./settings/' + social + '_status.sta', 'w')
        file_s.write('false')
        file_s.close()
    elif os.path.exists('./settings/' + social + '_status.sta'):
        file_y = open('./settings/' + social + '_status.sta', 'r')
        status = file_y.readline()
        file_y.close()
        return status

twitter_status = set_status('twitter')
facebook_status = set_status('facebook')


def show_list():
    print('Twitter - ' + twitter_status +
          '\nFacebook - ' + facebook_status + '\n')
    raw_input('Press enter key to continue.')


def run_to_posting_tw():
    if twitter_status == 'false':
        return False
    elif twitter_status == 'true':
        return True
    else:
        print('Twitter status neither True nor False')


def run_to_posting_fb():
    if facebook_status == 'false':
        return False
    elif facebook_status == 'true':
        return True
    else:
        print('Facebook status neither True nor False')
