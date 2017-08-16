"""
Operating system enumeration
"""
import platform
import os
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
        issues.update({"issue": os.system("cat /etc/issue")})
        return issues

    def get_releases(self):
        """
        get os releases
        """
        self.logger.normal_output("Grabbing releases")
        releases = {}
        releases.update({"releases": os.system("ls -l /etc/*-release")})
        return releases
        # self.logger.debug("Releases:" + releases)

    def get_kernel(self):
        """
        get kernel info
        """
        self.logger.normal_output("Grabbing Kernel information")
        kernel = {}
        kernel.update({"proc/version": os.system("cat /proc/version")})
        kernel.update({"uname -a": os.system("uname -a")})
        kernel.update({"uname -mrs": os.system("uname -mrs")})
        # this needs to be done in case of redhat or centos based distro
        # kernel += check_output(["rpm", "-q kernel"])
        # this appears to require root or sudo in debian
        # kernel += check_output(["dmesg | grep Linux"])
        # this appears to be weird
        kernel.update({"/boot": os.system("ls /boot | grep vmlinuz-")})
        return kernel

    def get_environment(self):
        """
        get system environment variables
        """
        self.logger.normal_output("Grabbing environment variables")
        env = {}
        self.logger.normal_output("Grabbing profile")
        env.update({"profile": os.system("cat /etc/profile")})
        self.logger.normal_output("Grabbing bashrc")
        env.update({"bashrc": os.system("cat /etc/bashrc")})
        self.logger.normal_output("Grabbing bash profile")
        env.update({"bashprofile": os.system("cat ~/.bash_profile")})
        self.logger.normal_output("Grabbing bashrc")
        env.update({"bashrc": os.system("cat ~/.bashrc")})
        self.logger.normal_output("Grabbing logout")
        env.update({"bash logout": os.system("cat ~/.bash_logout")})
        self.logger.normal_output("Grabbing env")
        env.update({"env": os.system("env")})
        self.logger.normal_output("Grabbing set")
        env.update({"set": os.system("set")})
        return env

    def get_printers(self):
        """
        get any printers
        """
        self.logger.normal_output("Grabbing printers")
        printers = {}
        printers.update({"printers lpstat": os.system("lpstat -a")})
        return printers
