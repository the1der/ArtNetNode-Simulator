import socket
import src.opcodes as opCodes
import src.node_data as nodedata

class ArtNetModule:
    PROTOCOL_ID = b"Art-Net\0"
    PORT = 6454
    sock = 0
    node_data = nodedata.NodeData()

    def __init__(self):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', self.PORT))
        self.node_data = nodedata.NodeData()

    def node_server(self):
        print('Server started')
        while True:
            print('Listing ..')
            data, address = self.sock.recvfrom(1024)
            if data[:8] == self.PROTOCOL_ID:
                opcode = (data[9] << 8) + data[8]
                
                if opcode == opCodes.OpPoll:
                    print("ArtPoll recieved")
                    tx_data = self.gen_artpollreply()
                    self.sock.sendto(tx_data,address)
                    print("ArtPollReply sent")
                    continue
                
                if opcode == opCodes.OpIpProg:
                    print("OpIpProg recieved")
                    self.decOpIpProgReply(data)
                    tx_data = self.genOpIpProgReply()
                    self.sock.sendto(tx_data,address)
                    print("OpIpProgReply sent")
                    continue

                print(f'Unhalled opCode: {hex(opcode)}')


    def gen_artpollreply(self):
        st = 0x40 if self.node_data.dhcp_capable else 0x00
        st = st | 0x20 if self.node_data.dhcp_enable else st
        data = bytearray(213)
        header = bytearray(self.PROTOCOL_ID)
        opCode = bytearray([0x00, 0x21])
        ipAddress = bytearray(self.node_data.ip)
        port=  bytearray([0x36,0x19])
        vers = bytearray([0x00, 0x00])
        unused1= bytearray([0x00, 0x00, 0x00, 0x00, 0x00])
        status1 = bytearray([0x00])
        unused2= bytearray([0x00, 0x00])
        shortname= bytearray(18)
        shortname[0:len(self.node_data.short_name)]= bytearray(self.node_data.short_name.encode())
        longname= bytearray(64)
        longname[0:len(self.node_data.long_name)]= bytearray(self.node_data.long_name.encode())
        unused3= bytearray(93)
        mac=bytearray(self.node_data.mac_address)
        bindipAddress = bytearray(self.node_data.ip)
        unused4 =  bytearray([0x00])
        status2 =  bytearray([st])
        unused5= bytearray(26)
        print(st)
        return header + opCode + ipAddress + port + vers + unused1 + status1 + unused2 + shortname + longname + unused3 + mac + bindipAddress + unused4 + status2 + unused5

    def genOpIpProgReply(self):
        
        header = bytearray(self.PROTOCOL_ID)
        opCode = bytearray([0x00, 0xf9])
        vers = bytearray([0x00, 0x00])
        unused1= bytearray(4)
        ipAddress = bytearray(self.node_data.ip)
        subnet = bytearray(self.node_data.netmask)
        port=  bytearray([0x19,0x36])
        status= bytearray([64])
        gw = bytearray(self.node_data.gateway)
        unused2= bytearray(2)
        return header + opCode + vers + unused1 + ipAddress + subnet + port + status + status + gw + unused2

    def decOpIpProgReply(self, rx_buff):
        cmd = rx_buff[14] 
        print(cmd)


if __name__ == "__main__":
    
    # create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # bind socket to Art-Net port
    sock.bind(('0.0.0.0', 1234))
    
    while 1:

        # receive Art-Net packet
        data, address = sock.recvfrom(1024)
        # extract opcode
        opcode = (data[9] << 8) + data[8]
        # print opcode
        print('OpCode:', hex(opcode) , ",from: ", address)
        if opcode  == 0x2000:
            print("ArtPoll recieved")
            # data= gen_artpollreply()
            sock.sendto(data,("0.0.0.0", 6454))
            # print(data)
            # time.sleep(0.2)
            # data = gen_artpollrepl2()
            # sock.sendto(data,("0.0.0.0", 6454))
            # print(len(data))

        if opcode == 0xf800:
            print("IpProg recieved")
            data = genArtIpProg()
            sock.sendto(data,("0.0.0.0", 6454))
            # time.sleep(0.2)
            # data = genArtIpProg2()
            # sock.sendto(data,("0.0.0.0", 6454))

