import socket

#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9001

#bind
s.bind((host, port))

#listen
s.listen()
print('listening ...')

#accept
client, addr = s.accept()
print(f'connection received from {addr} ')

password = 'myuser' #initialize password

#receive password from client
passwd = client.recv(1024).decode().strip()

#Authenticate the client
if passwd == password: #check if client password matches server password
    client.sendall(str.encode('Authentication successful')) #send authentication message to client
    print('CLIENT>>> Authentication successful')
else:
    client.sendall(str.encode('Access denied'))
    client.close()
    print('Access denied')

#chat with client
while True:
    msg = client.recv(1024).decode() #receive chat from client
    print('CLIENT>>>', msg) #display client chat on server
    if msg == 'end':    #if client chat contians the word 'end' close the chat
        break
    data = input('Enter your message ...')  #accept input from server
    client.sendall(str.encode(data))    #send chat to client
    