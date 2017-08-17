"""
Networking module
"""
import os
from modules.logger import Logger

class Networking(object):
    """
    Networking class
    """
    def __init__(self):
        return

    def run(self):
        self.logger = Logger()
        self.nics()
        self.get_tcpdump()
        self.get_networking_config_info()
        self.get_cached_network_info()
        self.get_users_and_hosts()

    def nics(self):
        """
        get network interfaces
        """
        self.logger.normal_output("Running network checks")
        nics = {}
        nics.update({"ifconfig": os.system("/sbin/ifconfig -a")})
        nics.update({"interfaces": os.system("cat /etc/network/interfaces")})
        nics.update({"network": os.system("cat /etc/sysconfig/network")})
        return nics

    def get_networking_config_info(self):
        """
        get networking configuration info, dhcp, etc.
        """
        self.logger.normal_output("Running network configuration checks")
        network_config = {}
        network_config.update({"resolv.conf": os.system("cat /etc/resolv.conf")})
        network_config.update({"sysconfig/network": os.system("cat /etc/sysconfig/network")})
        network_config.update({"networks": os.system("cat /etc/networks")})
        network_config.update({"iptables": os.system("iptables -L")})
        network_config.update({"hostname": os.system("hostname")})
        network_config.update({"dnsdomainname": os.system("dnsdomainname")})

        return network_config

    def get_users_and_hosts(self):
        """
        get users and hosts communicating with the system
        """
        self.logger.normal_output("Running users and hosts")
        users_and_hosts = {}
        users_and_hosts.update({"lsof": os.system("lsof -i")})
        users_and_hosts.update({"lsof port 80": os.system("lsof -i :80")})
        users_and_hosts.update({"services on 80": os.system("grep 80 /etc/services")})
        users_and_hosts.update({"netstat -antup": os.system("netstat -antup")})
        users_and_hosts.update({"netstat -antpx": os.system("netstat -antpx")})
        users_and_hosts.update({"netstat - tulpn": os.system("netstat -tulpn")})
        users_and_hosts.update({"chkconfig --list": os.system("chkconfig --list")})
        users_and_hosts.update({"chkconfig -- run level and enabled": os.system("chkconfig --list | grep 3:on")})
        users_and_hosts.update({"last": os.system("last")})
        users_and_hosts.update({"w": os.system("w")})
        return users_and_hosts

    def get_cached_network_info(self):
        """
        get cached networking configuration info
        """
        self.logger.normal_output("Running cached network info")
        cached_network_info = {}
        cached_network_info.update({"arp -e": os.system("arp -e")})
        cached_network_info.update({"route": os.system("route")})
        cached_network_info.update({"route -nee": os.system("/sbin/route -nee")})
        return cached_network_info

    def get_tcpdump(self, host):
        """
        try to get a tcp dump
        """
        self.logger.normal_output("Running tcpdump")
        tcp_dump = {}
        tcp_dump.update("tcpdump output": os.system("tcpdump tcp dst " + host + " 80 and tcp dst 10.5.5.252 21")})
        return tcp_dump