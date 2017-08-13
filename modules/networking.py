"""
Networking module
"""
import subprocess

class Networking(object):
    """
    Networking class
    """
    def __init__(self):
        return

    def nics(self):
        """
        get network interfaces
        """
        nics = subprocess.call("/sbin/ifconfig -a")
        nics += subprocess.call("cat /etc/network/interfaces")
        nics += subprocess.call("cat /etc/sysconfig/network")
        return nics

    def get_networking_config_info(self):
        """
        get networking configuration info, dhcp, etc.
        """

        network_config = subprocess.call("cat /etc/resolv.conf")
        network_config += subprocess.call("cat /etc/sysconfig/network")
        network_config += subprocess.call("cat /etc/networks")
        network_config += subprocess.call("iptables -L")
        network_config += subprocess.call("hostname")
        network_config += subprocess.call("dnsdomainname")

        return network_config

    def get_users_and_hosts(self):
        """
        get users and hosts communicating with the system
        """
        users_and_hosts = subprocess.call("lsof -i")
        users_and_hosts += subprocess.call("lsof -i :80")
        users_and_hosts += subprocess.call("grep 80 /etc/services")
        users_and_hosts += subprocess.call("netstat -antup")
        users_and_hosts += subprocess.call("netstat -antpx")
        users_and_hosts += subprocess.call("netstat -tulpn")
        users_and_hosts += subprocess.call("chkconfig --list")
        users_and_hosts += subprocess.call("chkconfig --list | grep 3:on")
        users_and_hosts += subprocess.call("last")
        users_and_hosts += subprocess.call("w")
        return users_and_hosts

    def get_cached_network_info(self):
        """
        get cached networking configuration info
        """
        cached_network_info = subprocess.call("arp -e")
        cached_network_info += subprocess.call("route")
        cached_network_info += subprocess.call("/sbin/route -nee")
        return cached_network_info

    def get_tcpdump(self, host):
        """
        try to get a tcp dump
        """
        return subprocess.call("tcpdump tcp dst " + host + " 80 and tcp dst 10.5.5.252 21")