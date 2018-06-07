# encontra as portas seriais no sistema

import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())

print('{:*^50}'.format(' portas comm encontradas '))
for p in ports:
    print(p.device)
