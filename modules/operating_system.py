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
    logger = Logger()

    def __init__(self):
        self.setup_os_info()
        self.issues = {}
        self.releases ={}
        self.kernel = {}
        self.env = {}
        self.printers = {}

    def run(self):
        """
        run all modules
        """
        self.get_issues()
        self.get_releases()
        self.get_kernel()
        self.get_environment()
        self.get_printers()

    def setup_os_info(self):
        """
        Setup os info for use in other methods
        """
        # todo refactor this into a subclass single property
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
        self.issues.update({"issue": os.system("cat /etc/issue")})

    def get_releases(self):
        """
        get os releases
        """
        self.logger.normal_output("Grabbing releases")
        self.releases.update({"releases": os.system("ls -l /etc/*-release")})
        # self.logger.debug("Releases:" + releases)

    def get_kernel(self):
        """
        get kernel info
        """
        self.logger.normal_output("Grabbing Kernel information")
        self.kernel.update({"proc/version": os.system("cat /proc/version")})
        self.kernel.update({"uname -a": os.system("uname -a")})
        self.kernel.update({"uname -mrs": os.system("uname -mrs")})
        # this needs to be done in case of redhat or centos based distro
        # kernel += check_output(["rpm", "-q kernel"])
        # this appears to require root or sudo in debian
        # kernel += check_output(["dmesg | grep Linux"])
        # this appears to be weird
        self.kernel.update({"/boot": os.system("ls /boot | grep vmlinuz-")})

    def get_environment(self):
        """
        get system environment variables
        """
        self.logger.normal_output("Grabbing environment variables")
        self.logger.normal_output("Grabbing profile")
        self.env.update({"profile": os.system("cat /etc/profile")})
        self.logger.normal_output("Grabbing bashrc")
        self.env.update({"bashrc": os.system("cat /etc/bashrc")})
        self.logger.normal_output("Grabbing bash profile")
        self.env.update({"bashprofile": os.system("cat ~/.bash_profile")})
        self.logger.normal_output("Grabbing bashrc")
        self.env.update({"bashrc": os.system("cat ~/.bashrc")})
        self.logger.normal_output("Grabbing logout")
        self.env.update({"bash logout": os.system("cat ~/.bash_logout")})
        self.logger.normal_output("Grabbing env")
        self.env.update({"env": os.system("env")})
        self.logger.normal_output("Grabbing set")
        self.env.update({"set": os.system("set")})

    def get_printers(self):
        """
        get any printers
        """
        self.logger.normal_output("Grabbing printers")
        self.printers.update({"printers lpstat": os.system("lpstat -a")})
