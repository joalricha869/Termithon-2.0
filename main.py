#!/usr/bin/python3
# PyPrompt - An alternative cross-platform terminal shell made in Python!
# PyPrompt made by
#    _             _      _      _            ___    __ ___  
#   (_)           | |    (_)    | |          / _ \  / // _ \ 
#    _  ___   __ _| |_ __ _  ___| |__   __ _| (_) |/ /| (_) |
#   | |/ _ \ / _` | | '__| |/ __| '_ \ / _` |> _ <| '_ \__, |
#   | | (_) | (_| | | |  | | (__| | | | (_| | (_) | (_) |/ / 
#   | |\___/ \__,_|_|_|  |_|\___|_| |_|\__,_|\___/ \___//_/  
#  _/ |                                                      
# |__/  
#
# Based on Termithon by idkDwij
# Thanks to idkDwij for the base code of Termithon
# Thanks to BigBoyTaco for fixing the 'calc' command!
# btw do not trust anyone named theopensour or thesouropen or theclosedbitter
# 
# Billions of imports ahead!
#
#          .?77777777777777$.            
#          777..777777777777$+           
#         .77    7777777777$$$           
#         .777 .7777777777$$$$           
#         .7777777777777$$$$$$           
#         ..........:77$$$$$$$           
#  .77777777777777777$$$$$$$$$.=======.  
# 777777777777777777$$$$$$$$$$.========  
# 7777777777777777$$$$$$$$$$$$$.=========
# 77777777777777$$$$$$$$$$$$$$$.=========
# 777777777777$$$$$$$$$$$$$$$$ :========+.
# 77777777777$$$$$$$$$$$$$$+..=========++~
# 777777777$$..~=====================+++++
# 77777777$~.~~~~=~=================+++++.
# 777777$$$.~~~===================+++++++.
# 77777$$$$.~~==================++++++++:
# 7$$$$$$$.==================++++++++++. 
# .,$$$$$$.================++++++++++~.  
#         .=========~.........           
#         .=============++++++           
#         .===========+++..+++           
#         .==========+++.  .++           
#          ,=======++++++,,++,           
#          ..=====+++++++++=.            
#                ..~+=...  
#
from __future__ import division
import os
import string
import random
from random import choice
from random import randint
import socket
import platform
import fnmatch
from time import *
from time import sleep
import uuid
import py_compile
import getpass
import PyInstaller
import speedtest
import geocoder
import wget
import pyvim
import requests
import sys
import auto_py_to_exe
from tkinter import *
import pip


# Checks if Python version is more than 3.9 (Will only take effect on uncompiled build)
if sys.version_info < (3, 9):
    sys.stderr.write('You need Python 3.9 or later\n')
    sys.exit(1)

# Aw man no more neofetch screen :(
hostname = socket.gethostname()
curr_user = getpass.getuser()
global echo_on

def warnings():
    print("THIS IS A BETA BUILD OF PYPROMPT")
    print("NOTE THAT MOST COMMANDS MIGHT NOT WORK OR BE UNSTABLE")
    print("IT IS RECOMMENDED TO INSTALL PYTHON FOR BETA BUILDS")


# Ten Billion Imports Later...
joalricha = '''
    _             _      _      _            ___    __ ___  
   (_)           | |    (_)    | |          / _ \  / // _ \ 
    _  ___   __ _| |_ __ _  ___| |__   __ _| (_) |/ /| (_) |
   | |/ _ \ / _` | | '__| |/ __| '_ \ / _` |> _ <| '_ \__, |
   | | (_) | (_| | | |  | | (__| | | | (_| | (_) | (_) |/ / 
   | |\___/ \__,_|_|_|  |_|\___|_| |_|\__,_|\___/ \___//_/  
  _/ |                                                      
 |__/                                                       

'''
taco = '''

  ____  _       ____           _______              
 |  _ \(_)     |  _ \         |__   __|             
 | |_) |_  __ _| |_) | ___  _   _| | __ _  ___ ___  
 |  _ <| |/ _` |  _ < / _ \| | | | |/ _` |/ __/ _ \ 
 | |_) | | (_| | |_) | (_) | |_| | | (_| | (_| (_) |
 |____/|_|\__, |____/ \___/ \__, |_|\__,_|\___\___/ 
           __/ |             __/ |                  
          |___/             |___/                   

'''
dwij = '''

  _     _ _    _____           _ _ 
 (_)   | | |  |  __ \         (_|_)
  _  __| | | _| |  | |_      ___ _ 
 | |/ _` | |/ / |  | \ \ /\ / / | |
 | | (_| |   <| |__| |\ V  V /| | |
 |_|\__,_|_|\_\_____/  \_/\_/ |_| |
                               _/ |
                              |__/ 

'''
pypromptascii = '''
  _____       _____                           _   
 |  __ \     |  __ \                         | |  
 | |__) |   _| |__) | __ ___  _ __ ___  _ __ | |_ 
 |  ___/ | | |  ___/ '__/ _ \| '_ ` _ \| '_ \| __|
 | |   | |_| | |   | | | (_) | | | | | | |_) | |_ 
 |_|    \__, |_|   |_|  \___/|_| |_| |_| .__/ \__|
         __/ |                         | |        
        |___/                          |_|        

'''
print(pypromptascii)
print(" ")
warnings()
print(" ")
hostnamecomputer = socket.gethostname()
global current_dir
current_dir = os.getcwd()


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


commands = '''
  _____       _____                           _     _    _      _       
 |  __ \     |  __ \                         | |   | |  | |    | |      
 | |__) |   _| |__) | __ ___  _ __ ___  _ __ | |_  | |__| | ___| |_ __  
 |  ___/ | | |  ___/ '__/ _ \| '_ ` _ \| '_ \| __| |  __  |/ _ \ | '_ \ 
 | |   | |_| | |   | | | (_) | | | | | | |_) | |_  | |  | |  __/ | |_) |
 |_|    \__, |_|   |_|  \___/|_| |_| |_| .__/ \__| |_|  |_|\___|_| .__/ 
         __/ |                         | |                       | |    
        |___/                          |_|                       |_|    
                                                             
DIR                     (Integrated dir/ls command. To use vanilla dir on Windows, Enter CMD Mode and type dir.)
IP                      (Gives you your IP)
HOSTNAME                (Gives you your Computer's ID)
MAC                     (Retrieves the Physical MAC Address of The Device)
PING                    (lets you ping a website)
CALC                    (A simple CLI calculator)
PASSGEN                 (A very efficient password generator)
SYSINFO                 (Gets relevant system info)
TEST                    (Tests PyPrompt Sample Command)
MAILGEN                 (Generates dummy E-Mail Addresses)
VER                     (Reports PyPrompt Version)
CLEAR                   (Clears screen)
LOADBARTEST             (Tests the loadbar)
INTRO                   (Displays initial text)
SQRT                    (Enter a number and it will calculate the square root)
DATE                    (Displays date)
CD                      (Navigate through folders) (NOTE: Applicable on PyPrompt Mode ONLY!. If you use CMD/BASH directories will change)
IPLOCATION              (Find the physical location of your IP address)
SPEEDTEST               (Speedtest.net but built into PyPrompt!)
ENCRYPT                 (Uses the RSA Algorithm to encrypt a message!)
FILESEARCH              (Searches files via their file name)
FILEDOWNLOADER          (Download any file via their url)
UNHELP                  (i'm not sure what this is. it just exists.)
LOCATOR                 (Locate basically any location in the planet)
DEVHELP                 (Detailed info about PyPrompt useful for troubleshooting)
COMPILER                (Compile any standard Python file to a *.pyc format)
PYVIM                   (Vim clone 'MADE BY jonathanslenders On GitHub') WILL REQUIRE PYTHON!!
PYINSTALLER             (Another Python compiler) REQUIRES PYTHON
EZFORMAT                (Simplified disk formatter) ONLY WORKS ON WINDOWS
EZTASKKILL              (Eliminate some process without using the task mamager) ONLY WORKS ON WINDOWS
WEATHER                 (Gets the weather from any city) Made by imkaka. Github: https://github.com/imkaka
MAGIC8BALL              (A virtual Magic-8-Ball made in Python)
BETTERCAL               (GUI Calculator using Tkinter) Original: https://github.com/flatplanet/Intro-To-Tkinter-Youtube-Course
CREDITS                 (Credits for all commands & dev list)


PyPrompt Modes:

CMD Mode (If usual Windows Shell commands are broken in PyPrompt, just use the 'cmd' command and you are in vanilla Command Prompt.)
         (NOTE: You are still in the PyPrompt App. Exit by typing exit in CMD Mode)
Bash Mode (Same as CMD Mode but you can run UNIX commands. Again, this is just a sidemode. You can return by typing exit or logoff.)

'''


def whatiscommand(current_dir):
    args = cmd.split()
    if cmd == 'help':
        print(commands)
        main(current_dir)
    elif cmd == 'dir':
        print(os.listdir(current_dir))
        main(current_dir)
    elif cmd == 'exit':
        sys.exit(1)
    elif cmd == 'ip':
        print("Your IP Address is " + getip())
        main(current_dir)
    elif cmd == 'hostname':
        uname = platform.uname()
        print(hostnamecomputer)
        main(current_dir)
    elif cmd == "mac":
        getmac()
        main(current_dir)
    elif "calc" in cmd:
        calc()
        main(current_dir)
    elif cmd == "passgen":
        passGen()
    elif cmd == "sysinfo":
        getSystemInfo()
        main(current_dir)
    elif cmd == "ver":
        ver()
        main(current_dir)
    elif cmd == "test":
        testFunc()
        main(current_dir)
    elif cmd == "mailgen":
        mailGen()
        main(current_dir)
    elif cmd == "clear":
        clear()
    elif "loadbartest" in cmd:
        progressbar()
        main(current_dir)
    elif "intro" in cmd:
        intro()
        main(current_dir)
    elif "sqrt" in cmd:
        sqrt()
        main(current_dir)
    elif "date" in cmd:
        date()
        main(current_dir)
    elif "ignore" in cmd:
        easterEgg()
        main(current_dir)
    elif cmd == "speedtest":
        speedtestapp()
        main(current_dir)
    elif cmd == "iplocation":
        iplocation()
        main(current_dir)
    elif "encrypt" in cmd:
        encryptdecrypt()
        main(current_dir)
    elif cmd == "unhelp":
        print("The command is 'ignore'")
        main(current_dir)
    elif "cd" in cmd:
        args.remove('cd')
        args = ' '.join(args)
        if cmd == "cd":
            main(current_dir)
        old_dir = current_dir
        if os.path.isdir(args) == True:
            current_dir = args
            main(args)
        elif os.path.isdir(old_dir + '\\' + args):
            new_dir = old_dir + '\\' + args
            current_dir = new_dir
            main(new_dir)
        else:
            print('The system cannot find the path specified. \n')
            main(current_dir)
    elif cmd == "filesearch":
        fileSearch()
        main(current_dir)
    elif cmd == "filedownloader":
        fileDownloader()
        main(current_dir)
    elif "locator" in cmd:
        locator()
        main(current_dir)
    elif cmd == "devhelp":
        devHelp()
        main(current_dir)
    elif cmd == "compiler":
        pyCompiler()
        main(current_dir)
    elif cmd == "ezformat":
        ezformatter()
        main(current_dir)
    elif cmd == "eztaskkill":
        eztaskkill()
        main(current_dir)
    elif cmd == "credits":
        credits()
        main(current_dir)
    elif cmd == "weather":
        GetCurrentWeather()
        main(current_dir)
    elif cmd == "magic8ball":
        magic8Ball()
        main(current_dir)
    elif cmd == "bettercal":
        betterCalc()
        main(current_dir)
    elif str(cmd) in cmd:
        print("This MUST be a shell command in the OS else your command won't work!")
        os.system(cmd)
        main(current_dir)
    else:
        error()


def main(current_dir):
    global main
    global old_dir
    old_dir = current_dir
    global cmd
    cmd = input(current_dir + '>')
    whatiscommand(current_dir)


def ver():
    print("PyPrompt Version: " + y)
    print("(C) 2022 joalricha869, All Rights Reserved.")


def getSystemInfo():
    print("=" * 40, "System Information", "=" * 40)
    global uname
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print("System Info Retrieved!")


# Calculator by BigBoyTaco
def calc():
    if "+" in cmd:
        numbers = cmd.split()
        first_number = float(numbers[1])
        second_number = float(numbers[3])
        print(first_number + second_number)
    elif "-" in cmd:
        numbers = cmd.split()
        first_number = float(numbers[1])
        second_number = float(numbers[3])
        print(first_number - second_number)
    elif "/" in cmd:
        numbers = cmd.split()
        first_number = float(numbers[1])
        second_number = float(numbers[3])
        print(first_number / second_number)
    elif "*" in cmd:
        numbers = cmd.split()
        first_number = int(numbers[1])
        second_number = int(numbers[3])
        print(first_number * second_number)
    elif cmd == "calc help":
        print("Proper use of calculator: calc 1 + 2")
        print("Only two numbers are allowed")
        print('''Calculator supports:
        1. Addition
        2. Subtraction
        3. Division
        4. Multiplication''')
    else:
        print('Error... use "calc help" for more help')


def passGen():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(8, 16)))
    print("Is your Generated Password: ", password)
    repeatGen = input("Generate another one? ")
    if repeatGen == "yes":
        passGen()
    else:
        main(current_dir)


def getmac():
    print("The MAC address of this Device is : ", end="")
    print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                    for ele in range(0, 8 * 6, 8)][::-1]))


def getip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = "Either your connection is VERY limited or you don't have internet so your ip is just the default: 127.0.0.1"
    finally:
        st.close()
    return IP


def clear():
    os.system('cls||clear')
    main(current_dir)


def error():
    if (cmd == ""):
        main(current_dir)
    else:
        print("'" + str(cmd) + "'" + ''' is not recognized as an internal or external command''')
        print("For more help go to: https://github.com/joalricha869/PyPrompt or https://github.com/IdkDwij/Termithon")
        main(current_dir)


def testFunc():
    print("Testing Geocoder: " + geocoder.__version__)
    print("Testing Speedtest: " + speedtest.__version__)
    print("Testing Wget: " + wget.__version__)
    print("Testing Getpass: " + getpass.__doc__)


def mailGen():
    extensions = ['com']
    domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier', 'icloud', 'yandex']
    characters = string.ascii_letters + string.digits
    winext = extensions[random.randint(0, len(extensions) - 1)]
    windom = domains[random.randint(0, len(domains) - 1)]
    acclen = random.randint(1, 20)
    winacc = ''.join(choice(characters) for _ in range(acclen))
    finale = winacc + "@" + windom + "." + winext
    progressbar()
    print("Your Generated E-Mail Address is: ", finale)
    again = input("Generate another address? ")
    if again == "yes":
        progressbar()
        mailGen()
    else:
        main(current_dir)


def progressbar():
    def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '▒' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
        if iteration == total:
            print()

    items = list(range(0, 50))
    l = len(items)

    loadbar(0, l, prefix='Generating...', suffix='Done!', length=l)
    for i, item in enumerate(items):
        sleep(0.1)
        loadbar(i + 1, l, prefix='Generating...', suffix='Done!', length=l)


def intro():
    print(pypromptascii)
    print(" ")
    warnings()
    print(" ")


def sqrt():
    num = float(input('Enter a number: '))
    num_sqrt = num ** 0.5
    print('The square root of %0.3f is %0.3f' % (num, num_sqrt))


def date():
    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("Today's date is:", d2)
    main(current_dir)


def easterEgg():
    print("PyPrompt Made by joalricha869")
    print("Termithon Kernel by idkDwij")
    print("calc Fix by BigBoyTaco")


def speedtestapp():
    speed = speedtest.Speedtest()
    option = int(input('''
    What do you want to know:
    1) Download speed
    2) Upload speed
    3) Both Download and Upload
    4) Ping
    Your choice: '''))

    if option < 1 or option > 4:
        sleep(2)
        print('You have entered wrong choice, please enter again with values from 1 to 4')
    else:
        sleep(1)
        print()
        print('Pls wait, test in progress...')
        print()
        down_speed = round(speed.download() / 1000000, 3)
        up_speed = round(speed.upload() / 1000000, 3)
        print('One more sec please...')
        sleep(1.5)
        print()
        if option == 1:
            print('Your Download speed is: ', down_speed, 'Mbps')
        elif option == 2:
            print('Your Upload speed is: ', up_speed, 'Mbps')
        elif option == 3:
            print('Your Download speed is: ', down_speed, 'Mbps', end=" ")
            print(',and your Upload speed is: ', up_speed, 'Mbps')

        elif option == 4:
            s = []
            speed.get_servers(s)
            print(speed.results.ping, 'ms')
        else:
            print("Either you have a VERY unstable internet connection or you don't have internet. Please try again...")


def iplocation():
    g = geocoder.ipinfo('me')
    print(g.latlng)


def encryptdecrypt():
    def isPrime(n):
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        return prime[n]

    def gcd(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def Multiplicative_inverse(a, b):
        s1 = 1
        s2 = 0
        m = b
        while b != 0:
            q = a // b
            r = a % b
            a = b
            b = r
            s = s1 - q * s2
            s1 = s2
            s2 = s

        if s1 < 0:
            s1 += m

        return s1

    def powermod(x, y, p):
        res = 1

        x = x % p
        while (y > 0):

            if (y % 2) == 1:
                res = (res * x) % p

            y = y // 2
            x = (x * x) % p

        return res

    if __name__ == '__main__':
        while (True):
            res = input(
                'Do you want to enter prime numbers (y) or let the algorithm do it for you (n) or exit (e)? (y/n/e): ')
            if res == 'y':
                while True:
                    p = 13
                    p = int(input('Enter a prime number: '))
                    if isPrime(p):
                        break
                    else:
                        print(p, 'is not a prime number')
                        continue

                while True:
                    q = 17
                    q = int(input('Enter a different prime number: '))
                    if isPrime(q) and (p * q > 26):
                        break
                    else:
                        print(
                            'Both the prime numbers are same!! or product of both the prime numbers is less than 26!!')
                        continue

                n = p * q
                phi_n = (p - 1) * (q - 1)
                a = 19
                while True:
                    a = int(input('Enter a number such that Greatest Common Divisor of that number with ' + str(
                        phi_n) + ' is 1: '))
                    if gcd(a, phi_n) != 1:
                        continue
                    else:
                        break

                b = Multiplicative_inverse(a, phi_n)
                message = input('Enter the message to be encrypted (lower case): ')
                message = message.lower()

                encrypted_string = ""
                encrypted_num = []

                for i in range(len(message)):
                    ch = message[i]
                    if ch != ' ':
                        m = ord(ch) - 97
                        e = powermod(m, a, n)
                        encrypted_num.append(e)
                        encrypted_string += chr(e % 26 + 97)
                    else:
                        encrypted_string += ' '

                print('Encrypted message is:', encrypted_string)
                print(encrypted_num)
                res = input("Do you want to decrypt it too? (y/n): ")
                if res == 'y':
                    decrypted = ''
                    j = 0
                    for i in range(len(encrypted_string)):
                        ch = message[i]
                        if ch != ' ':
                            e = encrypted_num[j]
                            m = powermod(e, b, n)
                            ch = chr(m + 97)
                            decrypted += ch
                            j += 1
                        else:
                            decrypted += ' '

                    print("Decrypted message is:", decrypted)
                else:
                    ans = input("Do you want to continue? (y/n): ")
                    if ans == 'y':
                        continue
                    else:
                        break

            elif res == 'n':
                p = 13
                q = 17
                n = p * q
                a = 5
                b = 77
                message = input('Enter the message to be encrypted (lower case): ')
                message = message.lower()

                encrypted_string = ""
                encrypted_num = []

                for i in range(len(message)):
                    ch = message[i]
                    if ch != ' ':
                        m = ord(ch) - 97
                        e = powermod(m, a, n)
                        encrypted_num.append(e)
                        encrypted_string += chr(e % 26 + 97)
                    else:
                        encrypted_string += ' '

                print('Encrypted message is:', encrypted_string)
                res = input("Do you want to decrypt it too? (y/n): ")
                if res == 'y':
                    decrypted = ''
                    j = 0
                    for i in range(len(encrypted_string)):
                        ch = encrypted_string[i]
                        if ch != ' ':
                            e = encrypted_num[j]
                            m = powermod(e, b, n)
                            ch = chr(m + 97)
                            decrypted += ch
                            j += 1
                        else:
                            decrypted += ' '

                    print("Decrypted message is:", decrypted)
                else:
                    ans = input("Do you want to continue? (y/n): ")
                    if ans == 'y':
                        continue
                    else:
                        break
            elif res == 'e':
                break
            else:
                print('Invalid command!')
                continue

def fileSearch():
    rootPath = '/'
    print("Note that the file extension format must be '*.extension' without the apostrophe obv")
    print("Depending on the speed of your HDD/SSD this may take a while (depending on the extension asw)")
    pattern = input("Specify File Name: ")
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))


def fileDownloader():
    wget.download = input("Enter URL for file download: ")
    main(current_dir)


def locator():
    t = input("Enter the location: ")
    g = geocoder.arcgis(t)
    print(g.latlng)


def devHelp():
    print("----------PyPrompt System Details----------\n")
    print("PYPROMPT VERSION: " + y)
    print("TERMITHON KERNEL VERSION: 0.1.3 (RELEASE-SKU)")
    print("CODENAME: COMMON_TOOLS_BETA2")


def pyCompiler():
    fileinput = input("Enter name of file you want to compile into .pyc format: ")
    py_compile.compile(fileinput)


def testModules():
    print(pyvim.__version__)
    print(PyInstaller.__version__)
    print(auto_py_to_exe.__version__)
    print(pip.__version__)


def ezformatter():
    print("Easy Formatter\n")
    print("This tool simplifies the format command in Windows")
    print("Please be aware that you need to run PyPrompt as an administrator")
    print("Drive letter formatting (G:)")
    volume = input("Please specify drive letter: ")
    print("Supported File Systems are NTFS, FAT, FAT32, exFAT, UDF, ReFS")
    filesystem = input("Please type the file system you want to format your drive with: ")
    volumename = input("Type the volume name of your drive: ")
    quickformatconfirm = input("Quick format your drive?: ")
    if quickformatconfirm == "yes":
        formattype = "/Q"
    else:
        formattype = ""
    os.system("format " + volume + "/FS:" + filesystem + "/V:" + volumename + formattype)


def eztaskkill():
    print("Kill an Annoying Process")
    print(" ")
    print("Have some process that you need to eliminate but you either can't use the Task Manager")
    processName = input("What is the name of the process you want to kill? IE: msedge.exe: ")
    os.system("taskkill /f /im " + processName)
    print("Done!")
    taskAgain = input("Kill another process: ")
    if taskAgain == "yes":
        eztaskkill()
    else:
        main(current_dir)

def GetCurrentWeather():
    def get_temperature(json_data):
        temp_in_farenheit = json_data['main']['temp']
        return temp_in_farenheit

    def get_weather_type(json_data):
        weather_type = json_data['weather'][0]['description']
        return weather_type

    def get_wind_speed(json_data):
        wind_speed = json_data['wind']['speed']
        return wind_speed



    def get_weather_data(json_data, city):
        description_of_weather = json_data['weather'][0]['description']
        weather_type = get_weather_type(json_data)
        temperature = get_temperature(json_data)
        wind_speed = get_wind_speed(json_data)
        weather_details = ''
        return weather_details + ("The weather in {} is currently {} with a temperature of {} degrees farenheit and wind speeds reaching {} km/ph".format(city, weather_type, temperature, wind_speed))


    def weather():
        print("Gather the Weather!")
        print(" ")
        print("NOTE: The inputs are CASE-SENSITIVE!!!")
        print("Any wrong misspell and PyPrompt will crash")
        city = input("Please Input City Name: ")
        countrycode = input("Please Input Country Code (ie. us, mx): ")
        api_address = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + countrycode + '&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
        units_format = "&units=imperial"
        final_url = api_address + city + units_format
        json_data = requests.get(final_url).json()
        weather_details = get_weather_data(json_data, city)
        # print formatted data
        print(weather_details)



    weather()

def magic8Ball():
    title = '''

        __  __                        __                 ____         ___             __  __ 
    F  \/  ]     ___ _     ___ _   LJ    ____        F __ J       F _ ",   ___ _   LJ  LJ 
    J |\__/| L   F __` L   F __` L       F ___J.     J `--' L     J `-'(|  F __` L  FJ  FJ 
    | |`--'| |  | |--| |  | |--| |  FJ  | |---LJ     / ,--. \     | ,--.\ | |--| | J  LJ  L
    F L    J J  F L__J J  F L__J J J  L F L___--.    F L__J J     F L__J \F L__J J J  LJ  L
    J__L    J__LJ\____,__L )-____  LJ__LJ\______/F   J\______/L   J_______J\____,__LJ__LJ__L
    |__L    J__| J____,__FJ\______/F|__| J______F     J______F    |_______FJ____,__F|__||__|
                            J______F                                                         
    '''
    ball = '''
            ____
        ,dP9CGG88@b,
    ,IP  _   Y888@@b,
    dIi  (_)   G8888@b
    dCII  (_)   G8888@@b
    GCCIi     ,GG8888@@@
    GGCCCCCCCGGG88888@@@
    GGGGCCCGGGG88888@@@@...
    Y8GGGGGG8888888@@@@P.....
    Y88888888888@@@@@P......
    `Y8888888@@@@@@@P'......
        `@@@@@@@@@P'.......
            """"........
    '''


    def magicBall():
        responses = ["It is certain.", 
        "It is decidedly so.", 
        "Without a doubt.", 
        "Yes definitely.", 
        "You may rely on it.", 
        " As I see it, yes.", 
        "Most likely.", 
        "Outlook good.", 
        "Yes.", 
        "Signs point to yes.", 
        "Reply hazy, try again.", 
        "Ask again later.", 
        "Better not tell you now.", 
        "Cannot predict now.", 
        "Concentrate and ask again.", 
        "Don't count on it.", 
        "My reply is no.", 
        "My sources say no.", 
        "Outlook not so good.", 
        "Very doubtful."]
        
        question = input("What do you want to ask the Magic 8 Ball? ")
        if question == str(question):
            print(random.choice(responses))
            again = input("Run Again? ")
            if again == "yes":
                magicBall()
            else:
                main(current_dir)
        else:
            print(random.choice(responses))
            again2 = input("Run Again? ")
            if again2 == "yes":
                magicBall()
            else:
                main(current_dir)

    def M8B():
        print(title)
        print(ball)
        magicBall()


    M8B()

def betterCalc():
    root = Tk()
    root.title("Better Calculator")

    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    #e.insert(0, "")

    def button_click(number):
        #e.delete(0, END)
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clear():
        e.delete(0, END)

    def button_add():
        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        e.delete(0, END)

    def button_equal():
        second_number = e.get()
        e.delete(0, END)
        
        if math == "addition":
            e.insert(0, f_num + int(second_number))

        if math == "subtraction":
            e.insert(0, f_num - int(second_number))

        if math == "multiplication":
            e.insert(0, f_num * int(second_number))

        if math == "division":
            e.insert(0, f_num / int(second_number))

        

    def button_subtract():
        first_number = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)

    def button_multiply():
        first_number = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)

    def button_divide():
        first_number = e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        e.delete(0, END)


    # Define Buttons

    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
    button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
    button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
    button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
    button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
    button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
    button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

    # Put the buttons on the screen

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)
    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)
    root.mainloop()

def credits():
    pyCredits = '''
PYPROMPT v1.6 CREDITS:

Developer / Maker: joalricha869 | https://github.com/joalricha869
Termithon Kernel: idkDwij | https://github.com/idkDwij | https://github.com/idkDwij/Termithon
CLI Calculator FIX: BigBoyTaco | https://github.com/BigBoyTaco

Command Credits:

WEATHER                 Made by imkaka      | https://github.com/imkaka
BETTERCAL               Made by flatplanet  | https://github.com/flatplanet/Intro-To-Tkinter-Youtube-Course
    
Most Commands by hastagAB | https://github.com/hastagAB/Awesome-Python-Scripts

LICENSE: GPL 3.0 | https://www.gnu.org/licenses/gpl-3.0.en.html
    '''
    print(pyCredits)
    print(" ")
    print('Made by:' + joalricha + 'it says joalricha https://github.com/joalricha869')
    print(" ")
    print('Thanks to ' + taco + 'for help  https://github.com/BigBoyTaco')
    print(" ")
    print('Based on Termithon by' + dwij + 'https://github.com/IdkDwij/Termithon')
    print(" ")
    print("The source is at my GitHub page! 'https://github.com/joalricha869/PyPrompt'")
    print("Type in 'help' for the command list.")



y = "1.6.beta2"

# Changes from 1.6.beta1
# ____________________________________
# - Modified WEATHER from getting temperature in celcius to farenheit
# - Fixed WEATHER from always getting the weather from Sydney
# - Fixed magic8ball from crashing
# - String changes in CREDITS, HELP, & INTRO
# - New Intro screen! (Less bloated!)
# - Removed SSH (INEFFICIENT AND BUGGY)
# - Removed TROUBLESHOOT (ALL MODULES ARE BUILT IN BINARY)
# - PYVIM & PYINSTALLER / AUTO-PY-TO-EXE NOW REQUIRES PYTHON TO WORK


main(current_dir)
