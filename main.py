import sys
import time
import pyfiglet
import colorama
from colorama import *
colorama.init(autoreset=True)

print('\n\n')
appname = pyfiglet.figlet_format("BloodGroupInfo")
companyname = pyfiglet.figlet_format("By  Technophilia  Limited", font='digital')
print(appname)
print(companyname)
print(f"{Fore.RED}I{Fore.YELLOW}N{Fore.GREEN}S{Fore.BLUE}T{Fore.MAGENTA}R{Fore.RED}U{Fore.YELLOW}C{Fore.GREEN}T{Fore.BLUE}I{Fore.MAGENTA}O{Fore.RED}N{Fore.YELLOW}S{Fore.GREEN}:")
print('''1. To check you Blood Group Compatability type in your Blood Group and press Enter.
2. To quit the MediTree App type 'exit' and press Enter.''')

def loading_function():
    counter = 0
    while counter <= 3:
        sys.stdout.write('\rClosing The Blood Compatibility Checker Terminal App..... loading | ')
        time.sleep(0.1)
        sys.stdout.write('\rClosing The Blood Compatibility Checker Terminal App..... loading / ')
        time.sleep(0.1)
        sys.stdout.write('\rClosing The Blood Compatibility Checker Terminal App..... loading - ')
        time.sleep(0.1)
        sys.stdout.write('\rClosing The Blood Compatibility Checker Terminal App..... loading \\ ')
        time.sleep(0.1)
        counter += 1
    sys.stdout.write('\rMediTree Blood Compatibility Checker Terminal App Closed.                                                                     ')
    print(f"\n{Fore.RED}{Back.BLACK}{Style.NORMAL}Thanks for using {Fore.RED}M{Fore.YELLOW}E{Fore.GREEN}D{Fore.BLUE}I{Fore.MAGENTA}T{Fore.RED}R{Fore.YELLOW}E{Fore.GREEN}E")
    print("\n\n")

while True:
    try:
        userinput = input("\n\nEnter your Blood Group(or 'exit' to quit): ")
        if userinput.lower() == "exit":
            print("\n\n")
            loading_function()
            sys.exit()
        elif userinput.lower().strip().replace(' ',''):
            if userinput.lower().replace(" ","") == 'o-':
                print(r"3% of the World Population has O- Blood Group.")
                print("You can receive from: O-\nYou can donate to: A+ ,A- ,B+ ,B- ,O+ ,O- ,AB+ ,AB-")
            elif userinput.lower().replace(" ","") == 'o+':
                print(r"42% of the World Population has O+ Blood Group.")
                print("You can receive from: O+, O-\nYou can donate to: O+, A+, B+, AB+ ")
            elif userinput.lower().replace(" ","") == 'a-':
                print(r"2.50% of the World Population has A- Blood Group.")
                print("You can receive from: A-, O-\nYou can donate to: A+, A-, AB+, AB-")
            elif userinput.lower().replace(" ","") == 'a+':
                print(r"31% of the World Population has A+ Blood Group.")
                print("You can receive from: A+, A-, O+, O-\nYou can donate to: A+, AB+")
            elif userinput.lower().replace(" ","") == 'b+':
                print(r"15% of the World Population has B+ Blood Group.")
                print("You can receive from: B+, B-, O+, O-\nYou can donate to: B+, AB+")
            elif userinput.lower().replace(" ","") == 'b-':
                print(r"1% of the World Population has B- Blood Group")
                print("You can receive from: B-, O-\nYou can donate to: B+, B-, AB+, AB-")
            elif userinput.lower().replace(" ","") == 'ab+':
                print(r"5% of the World Population has AB+ Blood Group.")
                print("You can receive from: A+ ,A- ,B+ ,B- ,O+ ,O- ,AB+ ,AB-\nYou can donate to: AB+")
            elif userinput.lower().replace(" ","") == 'ab-':
                print(r"0.50% of the World Population has AB- Blood Group.")
                print("You can receive from: AB-, A-, B-, O-\nYou can donate to: AB+ , AB-")
            else:
                print("Sorry, Blood Group Not Recognized!")
        print("To learn more about Blood Groups visit: https://en.wikipedia.org/wiki/Blood_type")
    except Exception as e:
        print(f"Oops! Something went wrong!\nDetails: {e}")