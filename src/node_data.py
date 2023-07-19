
import json

class NodeData:
    short_name = ""
    long_name = ""
    ip = []
    mac_address = []
    netmask = []
    gateway = []
    dhcp_enable = False
    dhcp_capable = False
    def __init__(self) :
        self.read_data()

    def read_data(self):
        with open('./node_data.json') as f:
            data = json.load(f)
            self.short_name = data['short_name']
            self.long_name = data['long_name']
            self.ip = data['ip']
            self.netmask = data['netmask']
            self.gateway = data['gateway']
            self.mac_address = data['mac_address']
            self.dhcp_enable = data['dhcp_enable']
            self.dhcp_capable = data['dhcp_capable']

    def write_data(self):
        data = {
                "short_name" : self.short_name,
                "long_name" : self.long_name,
                "mac_address" : self.mac_address,
                "ip" : self.ip,
                "gateway" : self.gateway,
                "netmask" : self.netmask,
                "dhcp_enable" : 1 if self.dhcp_enable else 0, 
                "dhcp_capable" : 1 if self.dhcp_capable else 0,
                }
        with open('./node_data.json', 'w') as f:
            json.dump(data, f)

if __name__ == "__main__":
    nodeData = NodeData()
    print("node data:")
    print("short name: " + nodeData.short_name)
    print("long name: " + nodeData.long_name)
    print("mac_address: " + ':'.join('{:02X}'.format(num) for num in nodeData.mac_address))
    print("ip: " + '.'.join('{}'.format(num) for num in nodeData.ip))
    print("gateway " + '.'.join('{}'.format(num) for num in nodeData.gateway))
    print("netmaks: " + '.'.join('{}'.format(num) for num in nodeData.netmask))
    print("DHCP enable: " + str(nodeData.dhcp_enable))
    print("DHCP capable: " + str(nodeData.dhcp_capable))

    nodeData.dhcp_enable = True
    nodeData.gateway = [192, 168, 1, 1]
    nodeData.write_data()