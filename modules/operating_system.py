"""
Operating system enumeration
"""
import subprocess
from modules.logger import Logger

"""
Class Operating system
"""
class OperatingSystem(object):
    """
    constructor
    """
    def __init__(self):
        self.logger = Logger()
        return

    def get_issues(self):
        """
        get linux issue file
        """
        self.logger.normal_output("[*] Grabbing /etc/issue")
        return subprocess.call(["cat /etc/issue"])

    def get_releases(self):
        """
        get os releases
        """
        self.logger.normal_output("[*] Grabbing releases")
        return subprocess.call("cat /etc/*-release")

    def get_kernel(self):
        """
        get kernel info
        """
        self.logger.normal_output("[*] Grabbing Kernel information")
        kernel = subprocess.call(["cat /proc/version", "uname -a", "uname -mrs", "rpm -q kernel", "dmesg | grep Linux", "ls /boot | grep vmlinuz-"])
        
        return kernel

    def get_environment(self):
        """
        get system environment variables
        """
        self.logger.normal_output("[*] Grabbing environment variables")
        return subprocess.call(["cat /etc/profile", "cat /etc/bashrc", "cat ~/.bash_profile", "cat ~/.bashrc", "cat ~/.bash_logout", "env", "set"])

    def get_printers(self):
        """
        get any printers
        """
        self.logger.normal_output("[*] Grabbing printers")
        return subprocess.call(["lpstat -a"])
