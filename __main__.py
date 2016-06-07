import os
import social_logins
import social_list
import posting_logic
import options

is_alive = True


def main():
    while is_alive:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('+-----------------------------------------------+\n'
              '|  Welcome to the Social Media Assistant.       |\n'
              '|  This is a simple application that allows     |\n'
              '|  the user to type a message once and it\'s     |\n'
              '|  posted across all of your social platforms.  |\n'
              '+-----------------------------------------------+\n')

        print('Current Commands:\n'
              '- Login\n'
              '- Post\n'
              '- Social\n'
              '- Options\n')
        choice = raw_input('Please Select a Command: ')
        if choice == "login":
            social_logins.login()
        elif choice == "post":
            msg = raw_input('What would you like to say: ')
            print('Now select a platform:\n'
                  '- facebook: Posts the message only to facebook\n'
                  '- twitter:  Posts the message only to facebook\n'
                  '- all:      Posts the message to all available platforms\n')
            platform = raw_input(' ')
            posting_logic.post(msg, platform)
        elif choice == "social":
            social_list.show_list()
        elif choice == "options":
            options.show_options()
        else:
            print("Unknown Command")

if __name__ == "__main__":
    main()
