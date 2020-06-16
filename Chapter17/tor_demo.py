#Must have the TOR service running on port 9150 while running this
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())

