import pyfiglet
import socket
import sys
from datetime import datetime

ascii_banner = pyfiglet.figlet_format('Python portscan')
print(ascii_banner)

def scanner(target, i):
  target = str(input('Digite o seu alvo:' + ' '))

  print("=" * 100)
  print(f'Escaneando alvo: {target}')
  print("escaneando alvo em" + ' ' + str(datetime.now()))
  print("=" * 100)

  try:
    for i in range(1, 65535):
      s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(.5)
      res = s.connect_ex((target, i))

      if res == 0:
        print(f'{i}, opened')
      else:
          pass

  except KeyboardInterrupt:
    print('Atalho CTRL + C pressionado... Interrompendo escaneamento')
    sys.exit()

  except SystemError:
    sys.exit()

scanner(target='', i='')
