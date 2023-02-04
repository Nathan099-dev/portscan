import socket
import sys

def scann(target_ip, portas):
	target_ip = str("Digite seu alvo")
	portas = []

	try:
		for portas in range(1, 65535):
			sys.argv[1]
			sys.argv[2]

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

	return scann()



