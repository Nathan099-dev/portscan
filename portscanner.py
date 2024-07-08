import pyfiglet
import socket
import sys
import os
import colorama
from colorama import Fore, init
from datetime import datetime

ascii_banner = pyfiglet.figlet_format('Python portscan')
print(ascii_banner)

init()
GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX

def scanner(target, i):
  target = str(input('Digite o seu alvo:' + ' '))
  
  print("=" * 100)
  print(f'Escaneando alvo: {target}')
  print("escaneando alvo em" + ' ' + str(datetime.now()))
  print("=" * 100)

  try:
    for i in range(1, 65535):
      s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(.15)
      response = s.connect_ex((target, i))

      if response == 0:
        print(f' {GREEN} [+] {i}' + ' ' + 'opened')
      else:
          pass

  except KeyboardInterrupt:
    print(f'{GRAY} Atalho CTRL + C pressionado... Interrompendo escaneamento')
    sys.exit()

  except SystemError: 
    sys.exit()

scanner(target='', i='')
