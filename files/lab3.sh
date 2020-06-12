sudo ovs-ofctl add-flow s1 priority=1,arp,actions=flood # Floods ARP traffic to all interfaces
sudo ovs-ofctl add-flow s1 priority=65535,ip,dl_dst=00:00:00:00:01:01,actions=output:1 # Forward traffic destined to the router's MAC address to switch interface 1
sudo ovs-ofctl add-flow s1 priority=10,ip,nw_dst=10.0.1.10,actions=output:2 # Forward traffic destined to h1 to switch interface 2
sudo ovs-ofctl add-flow s1 priority=10,ip,nw_dst=10.0.1.20,actions=output:3 # Forward traffic destined to h3 to switch interface 3
# Repeat for switch 2 and hosts h2 h4
sudo ovs-ofctl add-flow s2 priority=1,arp,actions=flood
sudo ovs-ofctl add-flow s2 priority=65535,ip,dl_dst=00:00:00:00:01:02,actions=output:1
sudo ovs-ofctl add-flow s2 priority=10,ip,nw_dst=10.0.2.10,actions=output:2
sudo ovs-ofctl add-flow s2 priority=10,ip,nw_dst=10.0.2.20,actions=output:3


h1 ip route add default via 10.0.1.1
h2 ip route add default via 10.0.2.1
h3 ip route add default via 10.0.1.1
h4 ip route add default via 10.0.2.1