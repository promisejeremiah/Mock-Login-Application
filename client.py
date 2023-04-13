import socket

#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9001

#connect
s.connect((host, port))

passwd = input('Enter your password ') #accept password from client
s.sendall(passwd.encode()) #send password to server for authentication
msg = s.recv(1024).decode() #receive authentication message from server
print('SERVER>>>', msg)

#chat with server
while True:
    data = input('Enter your message...') #accepts input from client
    s.sendall(str.encode(data)) #send client chat to server
    msg = s.recv(1024).decode() #receive chat from server
    print('SERVER>>>', msg) #display server chat
    if msg == 'end': #if server chat contians the word 'end' close the chat
        break