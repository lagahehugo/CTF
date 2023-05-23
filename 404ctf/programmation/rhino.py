import socket
#nc challenges.404ctf.fr 31420

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    #s.sendall(content)
    
    while 1:
        data = s.recv(7000) #1024
        if len(data) == 0:
            break
        #print("Received:", repr(data))
        #print(data)
        rhino=0
        l = ""
        i=0
        # print(data)
        while l != "Combien":
            # print("i ",i)
            # print("char ",chr(data[i]))
            l = l+chr(data[i])
            if "~c`\xc2\xb0^)" in l:
                rhino = rhino+1
                # print("Le nombre de rhinos est de :",rhino)
                l=""
            elif "Combien" in l:
                # print('sortie')
                break
            i = i+1
        print("Envoie :",rhino)
        res = str(rhino).encode()
        print("envoie de res :",res)
        s.sendall(res)
        data = s.recv(7000) #1024
        if len(data) == 0:
            print("no data")
            break
        print(data)
    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()

def main():
    hostname = "challenges.404ctf.fr"
    port = 31420
    content = ""
    netcat(hostname, port, content)


main()