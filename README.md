# Mock-Login-Application
This repo contains a mock login application built in python using sockets.

The server.py has the password.

When clients connect they first send a password that the user on the client types.

Your server check to ensure that this password matches.

If the password does not match, the connection closes and it sends a message to the client stating 'access denied'

if the password DOES match, it allows the client access to chat with the server.

If the client sends 'end' to the server, the connection ends.
