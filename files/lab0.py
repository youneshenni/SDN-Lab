#!/usr/bin/env python
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch, OVSSwitch
from mininet.node import Controller, RemoteController, OVSController


class MyTopo(Topo):
    "Empty topology."

    def __init__(self):
        "Create custom topo."
        net = Mininet(controller=Controller, switch=OVSSwitch)
        # Initialize topology
        net.build()
        CLI(net)
        net.stop()


topos = {'lab0': (lambda: MyTopo())}
