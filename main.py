from hashlib import md5
import socket
import sys

PORT = 4545

def do_send():
    print("You selected: sending files.\n")
    file_name = ""
    while True:
        file_name = input("Enter the file you want to send, along with its relative path: ")
        try:
            f = open(file_name, "r")
            f.close()
            break
        except FileNotFoundError:
            print("We couldn't find that file, try again.")
        except Exception as e:
            print("There was an error trying to access the file. Close any programs using it and try again.")
            print("If the error persists, report it with the following error message:")
            print(e.with_traceback())
            print("\n")
    print("File {} found successfully.".format(file_name))
    
    ip = input("Enter the IP of the computer you want to send the file to: ")

    ready = input("Are you ready to send file {} to IP {}? Enter 'Y' to confirm, or anything else to cancel: ".format(file_name, ip))
    if not (ready == "Y" or ready == "y"):
        print("Transfer cancelled.")
        return
    
    print("Connecting to {}...".format(ip))
    sock = None
    try:
        sock = socket.socket()
        sock.connect((ip, PORT))
    except Exception as e:
        print("Error occured when attempting to connect to IP.")
        print(e.with_traceback())
        return

    with open(file_name, "rb") as f:
        sock.sendfile(f)
        sock.close()
        print("File sent. Thank you for transferring.")
        f.close()
        return

def do_recv():
    file_name = input("Where do you want to store the transferred file? ")
    f = open(file_name, "wb")

    print("Please wait...")
    sock = socket.socket()
    sock.bind(("0.0.0.0", PORT))
    sock.listen(1)
    sock2, address = sock.accept()
    print("Connection received from {}".format(address))
    try:
        while True:
            a = sock2.recv(1)
            f.write(bytes(a))
            if sock2.fileno() == -1:
                print("Transfer finished. Exiting...")
                sock.close()
                f.close()
                return
    except Exception as e:
        print("Something happened, the file might be transferred, maybe an error happened.")
        print("Whatever happened was: ")
        print(e.with_traceback())
        

def main():
    print("Bevan Transfer\n(C) Copyright 2022 Bevan Ellis\nReleased under the MIT License\n")
    while True:
        action = input("Are you sending (enter 'SEND') or receiving (enter 'RECV') files? ")
        if action == "SEND":
            sys.exit(do_send())
        elif action == "RECV":
            sys.exit(do_recv())
        else:
            print("Sorry, that's not one of the options! Try again with either 'SEND' or 'RECV' (without the quotes).")

if __name__ == "__main__":
    sys.exit(main())