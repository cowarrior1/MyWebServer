import socket

HOST, PORT = '', 8888

# Create listening and accepting sockets for TCP connection
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1) #successful TCP connection
print 'Serving HTTP on port %s ...' % PORT
while True: #loop for establising connection between client and web socket
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request #creating HTTP request while connection.establish = True

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""

    client_connection.sendall(http_response) #sending HTTP response
    client_connection.close()
