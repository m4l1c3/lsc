"""
Operating system enumeration
"""
import platform
from modules.execute_command import ExecuteCommand
from modules.logger import Logger
from modules.file_writer import FileWriter

"""
Class Operating system
"""
class OperatingSystem(object):
    """
    constructor
    """
    logger = Logger()
    executor = ExecuteCommand()
    file_writer = FileWriter()
    # exfiltrator = Exfiltration("operating_system.lsc")

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
        except OSError as ex:
            self.logger.error("Error defining OS" + ex.message)
            self.platform = "Windows"

    def get_issues(self):
        """
        get linux issue file
        """
        self.logger.normal_output("Grabbing /etc/issue")
        self.issues.update({"issue": self.executor.execute_command("cat /etc/issue")})
        self.file_writer.write_output("lsc_issues.lsc", self.issues)

    def get_releases(self):
        """
        get os releases
        """
        self.logger.normal_output("Grabbing releases")
        self.releases.update({"releases": self.executor.execute_command("cat /etc/*-release")})
        self.file_writer.write_output("lsc_releases.lsc", self.releases)

    def get_kernel(self):
        """
        get kernel info
        """
        self.logger.normal_output("Grabbing Kernel information")
        self.kernel.update({"proc/version": self.executor.execute_command("cat /proc/version")})
        self.kernel.update({"uname -a": self.executor.execute_command("uname -a")})
        self.kernel.update({"uname -mrs": self.executor.execute_command("uname -mrs")})
        # this needs to be done in case of redhat or centos based distro
        # kernel += check_output(["rpm", "-q kernel"])
        # this appears to require root or sudo in debian
        # kernel += check_output(["dmesg | grep Linux"])
        # this appears to be weird
        self.kernel.update({"/boot": self.executor.execute_command("ls /boot | grep vmlinuz-")})
        self.file_writer.write_output("lsc_kernel-info.lsc", self.kernel)
    