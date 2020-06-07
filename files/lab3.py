from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )
    # Add hosts and switches
    h1 = net.addHost('h1', ip="10.1.1.10/24", mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', ip="10.1.1.20/24", mac="00:00:00:00:00:02")
    h3 = net.addHost('h3', ip="10.1.2.30/24", mac="00:00:00:00:00:03")
    h4 = net.addHost('h4', ip="10.1.2.40/24", mac="00:00:00:00:00:04")

    # Add Hosts
    # h5 10.1.3.50/24 mac 00:00:00:00:00:05
    # h6 10.1.3.60/24 mac 00:00:00:00:00:06
    h5 = net.addHost('h5', ip="10.1.3.50/24", mac="00:00:00:00:00:05")
    h6 = net.addHost('h6', ip="10.1.3.60/24", mac="00:00:00:00:00:06")

    r1 = net.addHost('r1')
    s1 = net.addSwitch('s1')

    # Add switch s2
    s2 = net.addSwitch('s2')

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    net.addLink(r1,s1)
    net.addLink(h1,s1)
    net.addLink(h2,s1)
    net.addLink(h3,s1)
    net.addLink(h4,s1)

    # Add Link s2 <---> r1
    # Add Link s2 <---> h5
    # Add Link s2 <---> h6
    net.addLink(r1,s2)
    net.addLink(h5,s2)
    net.addLink(h6,s2)

    net.build()
    c0.start()
    s1.start([c0])

    #start s2
    s2.start([c0])

    r1.cmd("ifconfig r1-eth0 0")
    r1.cmd("ifconfig r1-eth1 0")
    r1.cmd("ifconfig r1-eth0 hw ether 00:00:00:00:01:00")
    # Add another interface with new mac address on R1
    r1.cmd("ifconfig r1-eth1 hw ether 00:00:00:00:02:00")
    r1.cmd("ip addr add 10.1.1.1/24 brd + dev r1-eth0")
    r1.cmd("ip addr add 10.1.2.1/24 brd + dev r1-eth0")

    # set ip address 10.1.3.1
    r1.cmd("ip addr add 10.1.3.1/24 brd + dev r1-eth1")

    r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    h1.cmd("ip route add default via 10.1.1.1")
    h2.cmd("ip route add default via 10.1.1.1")
    h3.cmd("ip route add default via 10.1.2.1")
    h4.cmd("ip route add default via 10.1.2.1")

    # configure default routes on h5 and h6
    h5.cmd("ip route add default via 10.1.3.1")
    h6.cmd("ip route add default via 10.1.3.1")

    s1.cmd("ovs-ofctl add-flow s1 dl_type=0x0806,actions=flood")
    s1.cmd("ovs-ofctl add-flow s1 dl_type=0x0800,actions=normal")

    # Add flow autorisation arp and IP traffic
    s2.cmd("ovs-ofctl add-flow s2 dl_type=0x0806,actions=flood")
    s2.cmd("ovs-ofctl add-flow s2 dl_type=0x0800,actions=normal")


    print "*** Running CLI"
    CLI( net )
    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

topos = {'lab3':(lambda:topology())}
