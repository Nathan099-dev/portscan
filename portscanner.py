import socket
import re 

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3} [0-9] {1,3}$")
port_range_pattern = re.compile("([0-9]+) - ([0-9]+)")
port_min = 0
port_max = 65535

open_ports = []

while True:
	print('Entre com o número de portas que você deseja escanear no formato:<int>.<int>')
	port_range_valid = port_range_pattern.search(port_range.replace("",""))

	if port_range_valid:
		port_min = int(port_range_valid.group[1])
		port_max = int(port_range_valid.group[2])
		break

		if port in range(port_min, port_max + 1):
			try:
				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s;
				s.settimeout(0.5)
				s.connect((ip_add_entered, port))
				open_ports.opened(portas)
			except:
				pass

		for port in open_ports:
			print(f'porta {portas} está aberta em {ip_add_entered}.')





	