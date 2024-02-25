import json
import socket
import time
import random
import redis

# connect to redis
client = redis.Redis(host='redis', port=6379, health_check_interval=30, decode_responses=True)

print("here")

BUFFERSIZE = 128
LOCALIP = ''
LOCALPORT = 3002
UDP_REFRESH_TIME = 0.005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LOCALIP, LOCALPORT))  # Le indico que reciba de todos y en el puerto definido.
sock.setblocking(0)  # para que no se bloquee aunque no reciba por el socket

dictionary = {
    "0310": "2306124567210341",
    "0090": "2304124567210341",
    "00f0": "2304124567210000",
    "00f1": "2304124567210000",
    "00f2": "2304124567210000",
    "00a2": "0000000000000000",
    "0001": "2304124567210341",
    "0311": "BE12456721034178",
    "01cf": "0000010000000000",
    "02cf": "2783563298457345",
    "01ce": "0794385729875348",
    "02ce": "3452704389528393",
    "024f": "0000000000000000",
    "034f": "0000000000000000",
    "024e": "0000000000000000",
    "034e": "0000000000000000",
    "028f": "0000000000000000",
    "038f": "0000000000000000",
    "028e": "0000000000000000",
    "038e": "0000000000000000",
    "020e": "0000000000000000",
    "040e": "0000000000000000",
    "020f": "0000000000000000",
    "040f": "0000000000000000",
    "0122": "0000000000000000",
    "0181": "0000000000000000"
}

for i in dictionary:
    client.set(i, dictionary[i])

while True:
    #empiece=time.time()
    #print('Vamo')
    try:
        #data,addr = sock.recvfrom(BUFFERSIZE)
        #print(data)
        #sock.close()
        #msg = str(data.hex())

        #id = msg[0:4]
        int = random.randint(0, 4)
        id = ['0310', '0001', '00a2', '00f1', '0311']
        id = id[int]
        data = str(random.randint(100000, 999999)) + '0000000000'
        # set a key
        client.set(id,data)
        #client.set(str(id), str(''.join(map(str, msg[4:]))).removeprefix('c2'))
        time.sleep(0.05)
        #dictionary.update({str(id) : str(''.join(map(str, msg[4:]))).removeprefix('c2')})
        #print(dictionary)
        #print(id)
    except TimeoutError:
        pass
    except AttributeError:
        pass
    except BlockingIOError:
        #print("No rec")
        pass
    except ValueError:
        pass
    except IndexError:
        pass
    with open("data.json", "w") as outfile:
        json.dump(dictionary, outfile)
    #fin = time.time()