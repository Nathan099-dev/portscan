import socket
import sys
from datetime import datetime
import json

def save_results(results, filename="scan_results.json"): 
   with open(filename, 'w') as file: 
     json.dump(results, file, indent=4)

def scanner(target, i):
  target = str(input('Digite o seu alvo:' + ' '))

  total_ports_opened = 0
  
  print("=" * 100)
  print(f'Escaneando alvo: {target}')
  print("escaneando alvo em" + ' ' + str(datetime.now()))
  print("=" * 100)

  try:
    for i in range(1, 65535):
      s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(.1)
      response = s.connect_ex((target, i))

      if response == 0:
        print("Porta {} esta aberta".format(i))
        total_ports_opened = total_ports_opened + 1
      else:
          pass
      
  except KeyboardInterrupt:
    print(f'Atalho CTRL + C pressionado... Interrompendo escaneamento')
    print('Durante o escaneamento foram encontradas um total de {} portas abetas'.format(total_ports_opened))
    s.close()
    sys.exit()

  except socket.gaierror:
      print('O nome do host não pode ser resolvido... Encerrando')
      s.close()
      sys.exit()

  except socket.error: 
    print('Não foi possíveo conectar  com o servidoer do site... Encerrando escaner')
    s.close()
    sys.exit()

scanner(target='', i='')
