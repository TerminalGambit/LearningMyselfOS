# The purpose of this file is to document the different functions that can be used in the socket module in Python.
# This is a preparation for the final project, a game between a server and clients similar to the game killer chat.

# The socket module in Python provides access to the BSD socket interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.
# The socket module has a lot of functions, but the most important ones are:
# socket() - creates a new socket object
# bind() - binds a socket to an address
# listen() - listens for connections made to the socket
# accept() - accepts a connection made to the socket
# connect() - connects to a remote socket at the address
# send() - sends data to the socket
# recv() - receives data from the socket
# close() - closes the socket
# gethostname() - returns the hostname of the machine
# gethostbyname() - returns the IP address of the hostname

# The socket() function creates a new socket object. The first parameter is the address family, which should be AF_INET for IPv4 or AF_INET6 for IPv6.
# The second parameter is the socket type, which should be SOCK_STREAM for TCP or SOCK_DGRAM for UDP.
# The third parameter is the protocol, which is usually zero and can be omitted.
# The socket object has the following methods:
# bind() - binds the socket to an address
# listen() - listens for connections made to the socket
# accept() - accepts a connection made to the socket
# connect() - connects to a remote socket at the address
# send() - sends data to the socket
# recv() - receives data from the socket
# close() - closes the socket
# gethostname() - returns the hostname of the machine
# gethostbyname() - returns the IP address of the hostname

# The bind() function binds a socket to an address. The address should be a tuple containing the hostname and port number.
# The hostname should be a string containing the hostname or IP address of the machine.
# The port number should be an integer between 0 and 65535.
# The bind() function returns None.

# The listen() function listens for connections made to the socket. The backlog parameter specifies the maximum number of queued connections.
# The listen() function returns None.

# The accept() function accepts a connection made to the socket. It returns a new socket object and the address of the client.
# The new socket object can be used to send and receive data from the client.
# The address of the client is a tuple containing the hostname and port number of the client.

# The connect() function connects to a remote socket at the address. The address should be a tuple containing the hostname and port number of the remote socket.
# The hostname should be a string containing the hostname or IP address of the remote machine.
# The port number should be an integer between 0 and 65535.
# The connect() function returns None.

# The send() function sends data to the socket. The data should be a bytes object containing the data to send.
# The send() function returns the number of bytes sent.

# The recv() function receives data from the socket. The size parameter specifies the maximum number of bytes to receive.
# The recv() function returns a bytes object containing the data received.

# The close() function closes the socket. It returns None.

# The gethostname() function returns the hostname of the machine. It returns a string containing the hostname.

# The gethostbyname() function returns the IP address of the hostname. The hostname should be a string containing the hostname or IP address.
# The gethostbyname() function returns a string containing the IP address.

# Example of a simple server using the socket module:
import socket

# Create a new socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the address family for IPv4, and SOCK_STREAM is the socket type for TCP

# Bind the socket to an address
server_socket.bind(('localhost', 12345)) # The address is a tuple containing the hostname and port number

# Listen for connections made to the socket
server_socket.listen(5) # The backlog parameter specifies the maximum number of queued connections

# Accept a connection made to the socket
client_socket, client_address = server_socket.accept() # Returns a new socket object and the address of the client

# Receive data from the client
data = client_socket.recv(1024) # The size parameter specifies the maximum number of bytes to receive

# Send data to the client
client_socket.send(b'Hello, client!') # The data should be a bytes object

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
