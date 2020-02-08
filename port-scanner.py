import socket
import subprocess
import sys
from datetime import datetime

# Clear terminal's screen 
subprocess.call('clear', shell=True)

# Get user input
remoteServer    = input("Enter a remote host to scan: ")
showClosedPorts = input("Print closed ports? y/n")
startPortRange  = int(input("Start port range"))
endPortRange    = int(input("End port range"))

# get remove server ip from host name 
remoteServerIP  = socket.gethostbyname(remoteServer)

# print a banner 
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()


try:
    for port in range(startPortRange,endPortRange+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        elif result == 10060 and showClosedPorts == "y":
            print("Port {}: Closed".format(port))
        else:
            pass
        sock.close()

except KeyboardInterrupt:
    print("User session terminated")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Qutting...')
    sys.exit()

except socket.error:
    print("Couldn't connect to server. Quitting...")
    sys.exit()

# Printing the information to screen
print('Scanning Completed in: ',  datetime.now() - t1)
