"""
Networking module
"""
import os
from modules.logger import Logger

class Networking(object):
    logger = Logger()
    """
    Networking class
    """
    def __init__(self):
        self.nics = {}
        self.network_config = {}
        self.cached_network_info = {}
        self.users_and_hosts = {}
        self.tcp_dump = {}

    def run(self):
        """
        run all modules
        """
        self.get_nics()
        self.get_tcpdump("test")
        self.get_networking_config_info()
        self.get_cached_network_info()
        self.get_users_and_hosts()

    def get_nics(self):
        """
        get network interfaces
        """
        self.logger.normal_output("Running network checks")
        self.nics.update({"ifconfig": os.system("/sbin/ifconfig -a")})
        self.nics.update({"interfaces": os.system("cat /etc/network/interfaces")})
        self.nics.update({"network": os.system("cat /etc/sysconfig/network")})

    def get_networking_config_info(self):
        """
        get networking configuration info, dhcp, etc.
        """
        self.logger.normal_output("Running network configuration checks")
        self.network_config.update({"resolv.conf": os.system("cat /etc/resolv.conf")})
        self.network_config.update({"sysconfig/network": os.system("cat /etc/sysconfig/network")})
        self.network_config.update({"networks": os.system("cat /etc/networks")})
        self.network_config.update({"iptables": os.system("iptables -L")})
        self.network_config.update({"hostname": os.system("hostname")})
        self.network_config.update({"dnsdomainname": os.system("dnsdomainname")})

    def get_users_and_hosts(self):
        """
        get users and hosts communicating with the system
        """
        self.logger.normal_output("Running users and hosts")
        self.users_and_hosts.update({"lsof": os.system("lsof -i")})
        self.users_and_hosts.update({"lsof port 80": os.system("lsof -i :80")})
        self.users_and_hosts.update({"services on 80": os.system("grep 80 /etc/services")})
        self.users_and_hosts.update({"netstat -antup": os.system("netstat -antup")})
        self.users_and_hosts.update({"netstat -antpx": os.system("netstat -antpx")})
        self.users_and_hosts.update({"netstat - tulpn": os.system("netstat -tulpn")})
        self.users_and_hosts.update({"chkconfig --list": os.system("chkconfig --list")})
        self.users_and_hosts.update({"chkconfig -- run level and enabled": os.system("chkconfig --list | grep 3:on")})
        self.users_and_hosts.update({"last": os.system("last")})
        self.users_and_hosts.update({"w": os.system("w")})

    def get_cached_network_info(self):
        """
        get cached networking configuration info
        """
        self.logger.normal_output("Running cached network info")
        self.cached_network_info.update({"arp -e": os.system("arp -e")})
        self.cached_network_info.update({"route": os.system("route")})
        self.cached_network_info.update({"route -nee": os.system("/sbin/route -nee")})

    def get_tcpdump(self, host):
        """
        try to get a tcp dump
        """
        self.logger.normal_output("Running tcpdump")
        self.tcp_dump = {}
        self.tcp_dump.update({"tcpdump output": os.system("tcpdump tcp dst " + host + " 80 and tcp dst 10.5.5.252 21")})