#!/usr/bin/env python
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch, OVSSwitch
from mininet.node import Controller, RemoteController, OVSController

class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."
        net = Mininet(controller=Controller, switch=OVSSwitch)
        # Initialize topology
        Topo.__init__(self)
        # Add hosts and switches
        h1=self.addHost('h1',ip='10.1.1.10/24',mac='00:00:00:00:00:01')
        h2=self.addHost('h2',ip='10.1.1.20/24',mac='00:00:00:00:00:02')
        h3=self.addHost('h3',ip='10.1.2.30/24',mac='00:00:00:00:00:03')
        h4=self.addHost('h4',ip='10.1.2.40/24',mac='00:00:00:00:00:04')
        s1=self.addSwitch('s1')

        # Add links
        self.addLink(h1,s1)
        self.addLink(h2,s1)
        self.addLink(h3,s1)
        self.addLink(h4,s1)
        net.stop()

topos = {'lab1':(lambda:MyTopo())}
