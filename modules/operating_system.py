"""
Operating system enumeration
"""
import platform
import os
from subprocess import CalledProcessError
from subprocess import check_output
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
        self.releases = {}
        self.kernel = {}

    def run(self):
        """
        run all modules
        """
        self.logger.debug("Running OS")
        self.get_issues()
        self.get_releases()
        self.get_kernel()

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
        except Exception as ex:
            self.logger.error(ex)
            self.platform = "Windows"

    def get_issues(self):
        """
        get linux issue file
        """
        self.logger.normal_output("Grabbing /etc/issue")
        try:
            self.issues.update({"issue": check_output(["cat", "/etc/issue"])})
        except (CalledProcessError), error:
            # self.issues.update({"issue": os.system("cat /etc/issue")})
            self.logger.error("Error getting /etc/issue: " + error.output)

        

    def get_releases(self):
        """
        get os releases
        """
        self.logger.normal_output("Grabbing releases")
        self.releases.update({"releases": os.system("ls -l /etc/*-release")})

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
