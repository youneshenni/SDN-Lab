from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink


def topology():
    net = Mininet(controller=RemoteController,
                  link=TCLink, switch=OVSKernelSwitch)
    # Add hosts and switches
    h1 = net.addHost('h1', ip="10.1.1.10/24", mac="00:00:00:00:00:01")
    h2 = net.addHost('h2', ip="10.1.1.20/24", mac="00:00:00:00:00:02")
    h3 = net.addHost('h3', ip="10.1.2.30/24", mac="00:00:00:00:00:03")
    h4 = net.addHost('h4', ip="10.1.2.40/24", mac="00:00:00:00:00:04")
    r1 = net.addHost('r1')
    s1 = net.addSwitch('s1')
    net.addLink(r1, s1)
    net.addLink(r1, s1)
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)
    net.build()
    net.start()
    r1.cmd("ifconfig r1-eth0 0")
    r1.cmd("ifconfig r1-eth1 0")
    r1.cmd("ifconfig r1-eth0 hw ether 00:00:00:00:01:00")
    r1.cmd("ifconfig r1-eth1 hw ether 00:00:00:00:02:00")
    r1.cmd("ip addr add 10.1.1.1/24 brd + dev r1-eth0")
    r1.cmd("ip addr add 10.1.2.1/24 brd + dev r1-eth0")
    r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    h1.cmd("ip route add default via 10.1.1.1")
    h2.cmd("ip route add default via 10.1.1.1")
    h3.cmd("ip route add default via 10.1.2.1")
    h4.cmd("ip route add default via 10.1.2.1")
    s1.cmd("ovs-ofctl add-flow s1 dl_type=0x0800,actions=normal")
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()

topos = {'lab2': (lambda: topology())}
