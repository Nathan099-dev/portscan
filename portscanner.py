import pyfiglet
import socket
import sys
import os
import nmap 
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
  sys.argv[1]
  
  print("=" * 100)
  print(f'Escaneando alvo: {target}')
  print("escaneando alvo em" + ' ' + str(datetime.now()))
  print("=" * 100)

  nm = nmap.portscan()

for i in range(1,65535):
  try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      res = s.connect_ex((target, i))

      if res == 0:
          print(f' {GREEN} [+] {i}' + ' ' + 'opened')
          s.close()
      else:
        pass

  except KeyboardInterrupt:
    print(f'{GRAY} Atalho CTRL + C pressionado... Interrompendo escaneamento')
    s.close()
    sys.exit()
  
scanner(target='', i='')
