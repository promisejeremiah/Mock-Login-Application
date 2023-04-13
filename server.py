import socket
import bcrypt

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
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) #hash the password


passwd = client.recv(1024).decode() #receive password from client

#Authenticate the client
if bcrypt.checkpw(passwd.encode(), hashed): #check if client password matches server password
    client.sendall(str.encode('Access granted')) #send authentication message to client
    print('CLIENT>>> Access granted')
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
    
