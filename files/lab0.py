from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink


def topology():
    net = Mininet(controller=RemoteController,
                  link=TCLink, switch=OVSKernelSwitch)
    # Add hosts and switches

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()

topos = {'lab0': (lambda: topology())}
