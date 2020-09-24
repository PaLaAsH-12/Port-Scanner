#Modules and other beauty

import pyfiglet, sys, socket
from datetime import datetime

banner = pyfiglet.figlet_format("Port Scanner")
print(banner)

#Taking CLI Inputs

usage = "Invalid Argument. \n Correct Usgae is: python ps.py <host> <start_port> <end_port>"

if len(sys.argv) != 4:
	print(usage)
	sys.exit()

# Main Logic 

ip = sys.argv[1]
orgip = socket.gethostbyname(ip)
host = orgip
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
start_time = datetime.now()

print("""

-----------------------------------------------------------------
	Please Wait while scanning is going on.\n It make take a minute or hour depens on number of ports
-----------------------------------------------------------------
	""")

#Error handling with scanning

try:
	for port in range(start_port, end_port + 1):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP for UDP socket.DGRAM
		result = sock.connect_ex((host, port))
		sock.settimeout(2)
		if result == 0:
			print("\n[Found] Port {} is open on host {}".format(port, host))
			sock.close()
		else:
			print("\n[Error] Port {} is not open on host {}".format(port, host))
except Exception as error:
	print(error)
	sys.exit()
except socket.gaierror:
	print("\n In line 18, 19, 20 in module, host name invalid.")
	sys.exit()
except KeyboardInterrupt:
	print("\nYou pressed Ctrl + C")
	sys.exit()

end_time = datetime.now()

total_scan_time = end_time - start_time

print(" \n Total scanning time is : {}".format(total_scan_time))
