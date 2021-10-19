import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  #ip of device (laptop, rpi, etc)
port = 8080
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  from_client = ''
  print ('Got connection from',addr)
  while True:
    data = c.recv(4096)
    if not data: break
    from_client = data
    print(from_client.decode('ascii'))
    c.send('I am SERVER'.encode())
  c.close()
  print("Client disconnected")
