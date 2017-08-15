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
        return subprocess.call(["cat", "/etc/issue"])

    def get_releases(self):
        """
        get os releases
        """
        self.logger.normal_output("[*] Grabbing releases")
        return subprocess.call("cat", "/etc/*-release")

    def get_kernel(self):
        """
        get kernel info
        """
        self.logger.normal_output("[*] Grabbing Kernel information")
        kernel = subprocess.call(["cat", "/proc/version"])
        kernel += subprocess.call(["uname", "-a"])
        kernel += subprocess.call(["uname", "-mrs"])
        kernel += subprocess.call(["rpm", "-q kernel"])
        kernal += subprocess.call(["dmesg | grep Linux"])
        kernel += subprocess.call(["ls", "/boot | grep vmlinuz-"])
        
        return kernel

    def get_environment(self):
        """
        get system environment variables
        """
        self.logger.normal_output("[*] Grabbing environment variables")
        env =  subprocess.call(["cat", "/etc/profile"])
        env += subprocess.call(["cat", "/etc/bashrc"])
        env += subprocess.call(["cat", "~/.bash_profile"])
        env += subprocess.call(["cat", "~/.bashrc"])
        env += subprocess.call(["cat", "~/.bash_logout"])
        env += subprocess.call(["env"])
        env += subprocess.call(["set"])

    def get_printers(self):
        """
        get any printers
        """
        self.logger.normal_output("[*] Grabbing printers")
        return subprocess.call(["lpstat", "-a"])
