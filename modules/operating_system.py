"""
Operating system enumeration
"""
import platform
import os
from subprocess import check_output
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
        self.setup_os_info()
        return

    def setup_os_info(self):
        """
        Setup os info for use in other methods
        """
        try:
            self.system = platform.system()
            self.release = platform.release()
            self.version = platform.version()
            self.platform = platform.linux_distribution()
        except:
            self.platform = "Windows"
        
    def get_issues(self):
        """
        get linux issue file
        """
        self.logger.normal_output("Grabbing /etc/issue")
        issues = {}
        issues.update("issue", os.system("cat /etc/issue")
        return issues

    def get_releases(self):
        """
        get os releases
        """
        self.logger.normal_output("Grabbing releases")
        releases = {}
        releases.update("releases", os.system("ls -l /etc/*-release"))
        return releases
        # self.logger.debug("Releases:" + releases)

    def get_kernel(self):
        """
        get kernel info
        """
        self.logger.normal_output("Grabbing Kernel information")
        kernel = {}
        kernel.update("proc/version", os.system("cat /proc/version")
        kernel.update("uname -a", os.system("uname -a")
        kernel.update("uname -mrs", os.system("uname -mrs")
        # this needs to be done in case of redhat or centos based distro
        # kernel += check_output(["rpm", "-q kernel"])
        # this appears to require root or sudo in debian
        # kernel += check_output(["dmesg | grep Linux"])
        # this appears to be weird
        kernel.update("/boot", "ls /boot | grep vmlinuz-")
        
        return kernel

    def get_environment(self):
        """
        get system environment variables
        """
        self.logger.normal_output("Grabbing environment variables")
        env =  check_output(["cat", "/etc/profile"])
        env += check_output(["cat", "/etc/bashrc"])
        env += check_output(["cat", "~/.bash_profile"])
        env += check_output(["cat", "~/.bashrc"])
        env += check_output(["cat", "~/.bash_logout"])
        env += check_output(["env"])
        env += check_output(["set"])

    def get_printers(self):
        """
        get any printers
        """
        self.logger.normal_output("Grabbing printers")
        return check_output(["lpstat", "-a"])
