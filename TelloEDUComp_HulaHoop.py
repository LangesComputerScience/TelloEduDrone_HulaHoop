# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 8):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nBrian Kuhn - Team member: Mya Reynolds")
print("Program Name: Autonomous flight")
print("Date: 2.6.2024 ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")


        sendmsg('command', 0)
        sendmsg('battery?', 10)
        sendmsg('takeoff')

        # Pilot = Brian Kuhn - CoPilot = Mya Reynolds
        sendmsg('ccw 3')
        # sendmsg('up 55')
        # sendmsg('left 50')
        sendmsg('forward 225')

        # Pilot = Brian Kuhn - CoPilot = Mya Reynolds
        sendmsg('go 225 0 75 50', 10)

        # Pilot = Mya Reynolds - CoPilot - Brian Kuhn
        sendmsg('curve 125 125 0 0 250 0 50', 12)
        sendmsg('cw 180')
        sendmsg('forward 40', 10)

        #Pilot = Mya Reynolds - CoPilot - Brian Kuhn

        sendmsg('go 400 0 -100 50', 10)

        #Pilot = Brian Kuhn - CoPilot = (PERSONAL PROJECT NOT NECESSARY)
        sendmsg('go 215 0 85 100', 10)
        #curve
        sendmsg('curve 125 -135 -5 0 -270 -10 75', 12)
        sendmsg('forward 20')
        sendmsg('go 225 0 -75 50', 10)
        sendmsg('forward 20')

        sendmsg('land')
        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')
breakr = True
sock.close()