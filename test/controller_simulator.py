import socket
server_addr = ('<broadcast>', 6454)   #set Port here

def create_artnet_poll_message():
    # Art-Net packet header
    header = bytearray(b"Art-Net\x00")
    opcode = bytearray([0x00, 0x20])  # ArtPoll message opcode
    
    # Art-Net packet data
    data = bytearray(10)
    data[0] = 0x00  # ArtPollTalkToMe priority
    data[1] = 0x00  # ArtPollTalkToMe talk_to_me_mask
    data[2] = 0x00  # ArtPollTalkToMe talk_to_me_interval
    data[3] = 0x00  # ArtPollTalkToMe talk_to_me_request
    
    # Send the Art-Net packet
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(header + opcode + data, server_addr)


def create_artnet_opoutput_message():
    # Art-Net packet header
    header = bytearray(b"Art-Net\x00")
    opcode = bytearray([0x00, 0x50])  # OpOutput message opcode
    protver = bytearray([0x00, 0x0e])  # Protocol version
    sequence = bytearray([0x00])  # Packet sequence number
    physical = bytearray([0x00])  # Physical port number
    universe = bytearray([0x05, 0x00])  # Universe number lo-hi
    length = bytearray([0x02, 0x00])  # Packet length hi=lo
    # Art-Net packet data
    data = bytearray(512)
    
    off=4
    for i in range(128):  
        data[off*i]=255
        data[off*i+1]=255
        data[off*i+2]=255
        data[off*i+3]=255
    

    # print(str(data))
    # Send the Art-Net packet
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(header + opcode + protver + sequence + physical + universe + length + data, server_addr)


def create_artnet_OpIpProg_message():
     # Art-Net packet header
    header = bytearray(b"Art-Net\x00")
    opcode = bytearray([0x00, 0xf8])  # OpIpProg opcode  0x00f8
    protver = bytearray([0x00, 0x0e])  # Protocol version
    padding = bytearray([0x00])
    cammand = bytearray([0b10000000])
    ip = bytearray([0x00, 0x0e, 0x11, 0x12])
    subnet=  bytearray([255,255,255,0])
    port=  bytearray([0x19,0x36])   #Set port 6454
    gateway=  bytearray([192,168,161,199])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(header + opcode + protver + padding + padding + cammand + padding + ip + subnet + port + gateway + padding, server_addr)
    data = sock.recv(1024)
    print(data)

def sendArtAddress():
       # Art-Net packet header
    header = bytearray(b"Art-Net\x00")
    opcode = bytearray([0x00, 0x60])  # OpIpProg opcode  0x00f8
    protver = bytearray([0x00, 0x0e])  # Protocol version
    netSwitch = bytearray([0x0E]);
    bindIndex = bytearray([0x00])
    shortName = bytearray(18)
    # sName= b'Hello'
    # shortName[0:len(sName)]= sName
    longName=  bytearray(64)
    # lName= b'Hello there'
    # longName[0:len(lName)]= lName
    swIn=  bytearray([0x22, 0x22, 0x22, 0x22])   
    swOut=  bytearray([0x33, 0x33, 0x33, 0x33])   
    subSwitch = bytearray([0x03])  
    acnPriority =  bytearray([66])
    command =  bytearray([0x02])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    packet = header + opcode + protver + netSwitch + bindIndex + shortName + longName + swIn + swOut + subSwitch + acnPriority + command

    sock.sendto(header + opcode + protver + netSwitch + bindIndex + shortName + longName + swIn + swOut + subSwitch + acnPriority + command, server_addr)
# create_artnet_poll_message()
# create_artnet_opoutput_message()
create_artnet_OpIpProg_message()
# sendArtAddress()
