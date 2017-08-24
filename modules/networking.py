"""
Networking module
"""
from modules.logger import Logger
from modules.execute_command import ExecuteCommand

class Networking(object):
    """
    Networking class
    """
    logger = Logger()
    executor = ExecuteCommand()

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
        self.logger.normal_output("Running network")
        self.get_nics()
        # self.get_tcpdump("test")
        self.get_networking_config_info()
        self.get_cached_network_info()
        self.get_users_and_hosts()

    def get_nics(self):
        """
        get network interfaces
        """
        self.logger.normal_output("Running network checks")
        self.nics.update({"ifconfig": self.executor.execute_command("/sbin/ifconfig -a")})
        self.nics.update({"interfaces": self.executor.execute_command("cat /etc/network/interfaces")})
        self.nics.update({"network": self.executor.execute_command("cat /etc/sysconfig/network")})

    def get_networking_config_info(self):
        """
        get networking configuration info, dhcp, etc.
        """
        self.logger.normal_output("Running network configuration checks")
        self.network_config.update({"resolv.conf": self.executor.execute_command("cat /etc/resolv.conf")})
        self.network_config.update({"sysconfig/network": self.executor.execute_command("cat /etc/sysconfig/network")})
        self.network_config.update({"networks": self.executor.execute_command("cat /etc/networks")})
        self.network_config.update({"iptables": self.executor.execute_command("iptables -L")})
        self.network_config.update({"hostname": self.executor.execute_command("hostname")})
        self.network_config.update({"dnsdomainname": self.executor.execute_command("dnsdomainname")})

    def get_users_and_hosts(self):
        """
        get users and hosts communicating with the system
        """
        self.logger.normal_output("Running users and hosts")
        self.users_and_hosts.update({"lsof": self.executor.execute_command("lsof -i")})
        self.users_and_hosts.update({"lsof port 80": self.executor.execute_command("lsof -i :80")})
        self.users_and_hosts.update({"services on 80": self.executor.execute_command("grep 80 /etc/services")})
        self.users_and_hosts.update({"netstat -antup": self.executor.execute_command("netstat -antup")})
        self.users_and_hosts.update({"netstat -antpx": self.executor.execute_command("netstat -antpx")})
        self.users_and_hosts.update({"netstat - tulpn": self.executor.execute_command("netstat -tulpn")})
        self.users_and_hosts.update({"chkconfig --list": self.executor.execute_command("chkconfig --list")})
        self.users_and_hosts.update({
            "chkconfig -- run level and enabled": self.executor.execute_command("chkconfig --list | grep 3:on")
        })
        self.users_and_hosts.update({"last": self.executor.execute_command("last")})
        self.users_and_hosts.update({"w": self.executor.execute_command("w")})

    def get_cached_network_info(self):
        """
        get cached networking configuration info
        """
        self.logger.normal_output("Running cached network info")
        self.cached_network_info.update({"arp -e": self.executor.execute_command("arp -e")})
        self.cached_network_info.update({"route": self.executor.execute_command("route")})
        self.cached_network_info.update({"route -nee": self.executor.execute_command("/sbin/route -nee")})

    def get_tcpdump(self, host):
        """
        try to get a tcp dump
        """
        self.logger.normal_output("Running tcpdump")
        self.tcp_dump = {}
        self.tcp_dump.update(
            {
                "tcpdump output":
                self.executor.execute_command(
                    "tcpdump tcp dst " + host + " 80 and tcp dst 10.5.5.252 21"
                )
            }
        )
