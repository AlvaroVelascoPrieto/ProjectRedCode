
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP

client.bind(("", 37020))
while True:
    # Thanks @seym45 for a fix
    data, addr = client.recvfrom(1024)
    print(data.hex().zfill)
    #with open("data.json", "w") as outfile:
        #json.dump(dictionary, outfile)
    #fin = time.time()
    #print(fin-empiece)
