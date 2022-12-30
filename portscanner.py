import pyfiglet
import sys
import socket
from datetime import datetime


target = input(str('ip alvo: '))

print('=' * 80)
print('Escaneando o alvo:' + target)
print('iniciando às:' + str(datetime.now()))
print('=' * 80)

try:
	for port in range(1, 12000):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(1)

		res = s.connect_ex((target, port))
		if  res == 0:
			print(' port {} está aberta'.format(port))
			s.close()

except KeyboardInterrupt:
	print('	\n exiting:...')
	
except socket.error:
	print('\host não respondendo')
	sys.exit()


	


