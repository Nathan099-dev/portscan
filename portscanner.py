import socket
import sys

def scann(target_ip, portas):
	target_ip = str(input('Digite o seu alvo'))
	try:
		for portas in range(1, 65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect_ex((target_ip, portas))

		if portas == 0:
			print('porta, {} ====> ABERTA'.format(portas)) 

	except KeyboardInterrupt:
		print('interrompido')
		sys.exit()

	except socket.gaierror:
		print('Não resolvido')
		sys.exit()

scann()



