import socket
import time
import hashlib
from pwinput import pwinput
from pyfiglet import Figlet
from termcolor import colored  
def verify_user():
    print("\nHi! I'm 'MR. X.' I'm an AI designed to assist you with some automated attacks.")
    print("To access advanced tools, you need to verify yourself with credentials provided by Black Internet.\n")

    time.sleep(2)

    print("Do you want to proceed with the verification process?")
    print("1. Yes")
    print("2. No\n")

    res = int(input("Enter your option (1/2): "))

    if res == 1:
        print("\nThank you! You will be allowed to use my features after a few more steps...\n")

        time.sleep(1.5)

        name = "Dark10rd"
        print("For User:", name)

        passwd = str(pwinput(" password: ", "*"))
        hash_passwd = hashlib.md5(passwd.encode()).hexdigest()
        vpass = "dark10rd"
        hash_vpass = hashlib.md5(vpass.encode()).hexdigest()

        print("\nPlease wait for 5 seconds to get verified...")
        time.sleep(5)

        if hash_passwd == hash_vpass:
            print(name + ", you're completely verified to access my features.\n")
            body_func()
        else:
            print("Oops! Verification failed.\n")
            print("[a] Try again after some time")
            print("[b] Close the program\n")

            inuse = input("Option You select (a/b): ")

            if inuse == 'a':
                issue_func()
            elif inuse == 'b':
                print("Okay, the program is closing...")
                time.sleep(2)
                exit()

    elif res == 2:
        print("It's okay. You can access anytime.")
        time.sleep(5)
        exit()
    else:
        print("Invalid option. Please try again.")
        verify_user()

def body_func():
    while True:
        print("\n1. Features")
        print("2. Log Out")

        option = int(input("Enter your choice [1/2]: "))

        if option == 1:
            print("\nWelcome to the advanced tools Library!\n")
            op1 = "[1] Domain-2-IP & Automated NMAP"
            print(colored(op1, "green"))

            o_in = input("\n\nEnter the Feature You want to access: ")

            if o_in == "1":
                domain_2_IP()
            else:
                print("Invalid choice. Please try again.")
        elif option == 2:
            print("Logging out...")
            time.sleep(2)
            exit()
        else:
            print("Invalid choice. Please try again.")

def domain_2_IP():
    dn = input("Enter Your TARGET Domain: ")
    try:
        ip = socket.gethostbyname(dn)
        print("IP Address for {} is {}".format(dn, ip))
    except socket.gaierror:
        print("Invalid domain name or couldn't resolve the IP.")
    except Exception as e:
        print("An error occurred:", str(e))
    time.sleep(2)
    print("Do you want to scan the ip ?\n\n")
    yn = input("enter with y/n : ")
    if yn == 'y':   # X-map Scanner
        import nmap
        scanner = nmap.PortScanner()
        print("Welcome to The X-map")
        print("<------------------>\n\n")
        print("Select The type of Scan:\n\n[1] SYN ACK\n[2] UDP\n[3] Return to the menue\n\n")
        scr = input("Enter Your selection:  \n\n")
        if scr == '1':
            print("starting syn ack...")
            time.sleep(2)
            scanner.scan(ip, '1-1024', '-v -sS')
            print(scanner.scaninfo())
            print("IP Status: ", scanner[ip].state())
            print(scanner[ip].all_protocols())
            print("Open Ports : ", scanner[ip]['tcp'].keys())
        elif scr == '2':
            print("starting UDP Scan...")
            time.sleep(2)
            scanner.scan(ip, '1-1024', '-v -sU')
            print(scanner.scaninfo())
            print("IP Status: ", scanner[ip].state())
            print(scanner[ip].all_protocols())
            print("Open Ports : ", scanner[ip]['udp'].keys())
        else:
            body_func()
    elif yn == 'n':
        body_func()
    else:
        print("Invalide Options") 
        time.sleep(3)
        exit() 
                    
                                                        
def issue_func():
    time.sleep(2)
    passwd = str(pwinput("Enter your password: ", "*"))
    hash_passwd = hashlib.md5(passwd.encode()).hexdigest()
    vpass = "dark10rd"
    hash_vpass = hashlib.md5(vpass.encode()).hexdigest()

    if hash_passwd == hash_vpass:
        body_func()
    else:
        print("Verification failed. Try again after some time or close the program.")
        inuse = input("Option You select (a/b): ")
        if inuse == 'a':
            issue_func()
        elif inuse == 'b':
            print("Okay, the program is closing...")
            time.sleep(2)
            exit()

if __name__ == "__main__":
    banner = Figlet(font="isometric3").renderText("MR.X")
    print(colored(banner, "blue"))
    print(colored("*********Created By Black Internet && Dev is Dark10rd*********", "yellow"))
    verify_user()
