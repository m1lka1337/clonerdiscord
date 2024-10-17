import requests
import subprocess
import sys
from time import sleep


class Update():
    def __init__(self):
        self.version = '0.2.2'
        self.github = 'https://raw.githubusercontent.com/m1lka1337/clonerdiscord/main/update.py'
        self.zipfile = 'https://github.com/m1lka1337/clonerdiscord/raw/refs/heads/main/main.zip'
        self.update_checker()

    def update_checker(self):
        code = requests.get(self.github).text
        if "self.version = '0.2.2'" in code:
            print('Ваша версия актуальна!')
            time.sleep(1)
            pass
        else:
            print('''
                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                      Ваша версия устарела выберите вариант ниже''')
            choice = input('\nХотите обновить? (да/нет): ')
            if choice.lower() == 'да':
                print('Скачивание обновления...')
                new_version_source = requests.get(self.zipfile)
                with open("Update.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)

                subprocess.Popen([sys.executable, 'updater.py'])

                sys.exit(2)
            if choice.lower() == 'нет':
                sys.exit(0)


if __name__ == '__main__':
    Update()
