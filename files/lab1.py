#!/usr/bin/env python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink


def topology():
    net = Mininet(controller=RemoteController,
                  link=TCLink, switch=OVSKernelSwitch)
    net = Mininet(controller=Controller, switch=OVSSwitch)
    # Initialize topology
    Topo.__init__(net)
    # Add hosts and switches
    h1 = net.addHost('h1', ip='10.1.1.10/24', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', ip='10.1.1.20/24', mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', ip='10.1.2.30/24', mac='00:00:00:00:00:03')
    h4 = net.addHost('h4', ip='10.1.2.40/24', mac='00:00:00:00:00:04')
    s1 = net.addSwitch('s1')
    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)
    net.build()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()

topos = {'lab1': (lambda: topology())}
