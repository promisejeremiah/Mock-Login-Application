# Mock-Login and Chat-Application
This repo contains a mock login and chat application built in python using sockets.

The server.py has the password.

When clients connect they first type a password and it is sent to the server.

The server check to ensure that this password matches.

If the password does not match, the connection closes and it sends a message to the client stating 'access denied'

if the password DOES match, it allows the client access to chat with the server.

If the client sends 'end' to the server, the connection ends.
