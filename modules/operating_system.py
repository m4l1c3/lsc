"""
Operating system enumeration
"""
import platform
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
        return check_output(["cat", "/etc/issue"])

    def get_releases(self):
        """
        get os releases
        """
        self.logger.normal_output("Grabbing releases")
        releases = check_output(["ls", "-l", "/etc/*-release"]).rstrip()
        releases = check_output(["cat", "/etc/*-release"])
        self.logger.debug("Releases:" + releases)

    def get_kernel(self):
        """
        get kernel info
        """
        self.logger.normal_output("Grabbing Kernel information")
        kernel = check_output(["cat", "/proc/version"])
        kernel += check_output(["uname", "-a"])
        kernel += check_output(["uname", "-mrs"])
        kernel += check_output(["rpm", "-q kernel"])
        kernel += check_output(["dmesg | grep Linux"])
        kernel += check_output(["ls", "/boot | grep vmlinuz-"])
        
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
