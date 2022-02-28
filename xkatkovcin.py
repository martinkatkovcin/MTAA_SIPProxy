import sipfullproxy
import logging
import socketserver
import socket

HOST, PORT = '0.0.0.0', 5060
output = ['y', 'Y', 'n', 'N']
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', 
    filename = 'dennik_hovorov.log', 
    level = logging.INFO, 
    datefmt = '%Y-%m-%d %H:%M:%S')

if input('Automatic IP address, type y/Y, otherwise n/N\n') in output[0:2]:
    ipaddress = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
else:
    ipaddress = input('Type IP address in type X.X.X.X:\n')

print('SIP Proxy running on address:', ipaddress + ":" + str(PORT))
logging.info(f'Telefonna ustredna (SIP Proxy) bezi na <{HOST}:{PORT}>') 
sipfullproxy.recordroute = 'Record-Route: <sip:%s:%d;lr>' % (ipaddress, PORT)
sipfullproxy.topvia = 'Via: SIP/2.0/UDP %s:%d' % (ipaddress, PORT)
server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
server.serve_forever()
