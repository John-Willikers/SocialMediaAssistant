import os


def change_status(newvalue, social):
        os.remove('./settings/' + social + '_status.sta')
        file_value = open('./settings/' + social + '_status.sta', 'w')
        file_value.write(newvalue)
        file_value.close()


def status(social):
    file_a = open('./settings/' + social + '_status.sta', 'r')
    status_1 = file_a.read()
    file_a.close()
    return status_1


def show_options():
    print('Options:\n'
          '- socials: Change Social(s) active state')
    choice = raw_input('')
    if choice.lower() == 'socials':
        print('Current Socials:\n'
              '- Facebook: ' + status('facebook') + '\n'
              '- Twitter: ' + status('twitter') + ' ')
        social = raw_input('Which Social: ')
        newvalue = raw_input('New Value -  true or false: ')
        social1 = social.lower()
        newvalue1 = newvalue.lower()
        change_status(newvalue1, social1)
