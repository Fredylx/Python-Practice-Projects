Import socket



HOST = ‘’
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print (‘Socket created’)
s.bind((HOST, PORT))
print(‘Socket bind complete’)
s.listen(10)
print (‘Socket now listening’)
#wait to accept a connection - blocking call
conn, addr  = s.accept()
s.setblocking(0)
#display client information 
print(“Connected with’ + addr[0] + ‘.’ + str(addr[1]))
#now keep talking with the client
data = conn.racv(1024)
print(data)
conn.senddall(data)
print(data)
conn.sendall(data)
print(‘end test’)
conn.close()
s.close()
