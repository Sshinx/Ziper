import os
import zipfile
from time import time
import argparse
import string, itertools
from colorama import *
from pyfade import Colors, Fade, Anime  #https://github.com/billythegoat356/pystyle

class Ziper():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Ziper cracker [Bidouffe]")
        self.parser.add_argument('-f', help='path of zipfile')
        self.parser.add_argument('-l', help='path of pass list')
        self.args = self.parser.parse_args()
        self.file = self.args.f
        self.lister = self.args.l
        zip_ = None
        self.password = None
        self.list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        try:
            self.zip_ = zipfile.ZipFile(self.file)

        except zipfile.BadZipfile:
            print(f'  [{Fore.RED}X{Fore.RESET}] Bad Zip-File')
            quit()

    def brand(self):
        ziper_brand = f'''
    ╔═╗┬┌─┐┌─┐╦═╗
    ╔═╝│├─┘├┤ ╠╦╝
    ╚═╝┴┴  └─┘╩╚═  {Fore.RESET}[github.com/{Fore.YELLOW}Sshinx{Fore.RESET}]
        '''
        print(Fade.Vertical(Colors.green_to_yellow, ziper_brand))

    def choice(self):
        os.system('title Ziper [github.com/Bidouffe]')

        """
        bruter = None
        if self.args.l == None:
            bruter = "yes"
        if bruter == "yes":
            Ziper().bruteforce('', 1)
        else:
            Ziper().brutelist()
        """

        Ziper().brutelist()


    """
    def bruteforce(word, a, self):
        os.system('cls')
        Ziper().brand()
        c_t = time()
        characters = string.printable

        def iter_all_strings():
            length = 1
            while True:
                for s in itertools.product(characters, repeat=length):
                    yield "".join(s)
                length +=1

        for s in iter_all_strings():
            password = bytes(s, 'utf-8')
            print(f"  Attempting pass => {Fore.GREEN}{password}{Fore.RESET}", end='\r')
            zp = self.zip_
            zp.extractall(pwd=password)
            t_t = time() - c_t
            password = str(password, 'utf-8')
            os.system('cls')
            Ziper().brand()
            print(f"  [{Fore.GREEN}*{Fore.RESET}] Password is " + f"[{Fore.YELLOW}{password}{Fore.RESET}]")
            print(f"  [{Fore.GREEN}*{Fore.RESET}] Time => [{Fore.YELLOW}{t_t}{Fore.RESET}]")
            quit()
        print(f"  [{Fore.RED}X{Fore.RESET}] Password Not Found !")
        quit()

    """
    def brutelist(self):
        os.system('cls')
        Ziper().brand()
        c_t = time()
        
        with open(self.lister, "r", encoding='latin-1') as f: 
            passes = f.readlines()
            for x in passes:
                try:
                    password = x.split("\n")[0]
                    bpassword = bytes(password, 'utf-8')
                    print(f"  Attempting pass => {Fore.GREEN}{password}{Fore.RESET}", end='\r')
                    zp = self.zip_
                    zp.extractall(pwd=bpassword)
                    t_t = time() - c_t
                    os.system('cls')
                    Ziper().brand()
                    print(f"  [{Fore.GREEN}*{Fore.RESET}] Password is " + f"[{Fore.YELLOW}{password}{Fore.RESET}]")
                    print(f"  [{Fore.GREEN}*{Fore.RESET}] Time => [{Fore.YELLOW}{t_t}{Fore.RESET}]")
                    quit()
                except Exception:
                    pass
            print(f"  [{Fore.RED}X{Fore.RESET}] Password isn't in {self.lister} !")
            quit()
    
Ziper().choice()
