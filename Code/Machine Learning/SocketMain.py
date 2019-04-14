import socket
import _thread
def onNewClient(clientSocket , addr):
    try:
	    while True:
		    clientSocket.send("Welcome to server".encode("utf-8"))
		    print(clientSocket.recv(1024).decode("utf-8"))
    except:
        print("Connection Lost")
S = socket.socket()
Host = ""
port = 12345

print("Server Started")
print("Waitting For Cleints")
S.bind((Host , port))
S.listen(5)
while True:
    Connection , Address = S.accept()
    _thread.start_new_thread(onNewClient,(Connection , Address))
s.close()