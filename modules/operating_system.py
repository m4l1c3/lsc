"""
Operating system enumeration
"""
import subprocess

"""
Class Operating system
"""
class OperatingSystem(object):
    """
    constructor
    """
    def __init__(self):
        return

    def get_issues(self):
        """
        get linux issue file
        """
        print "[*] Grabbing /etc/issue"
        return subprocess.call("cat /etc/issue")

    def get_releases(self):
        """
        get os releases
        """
        print "[*] Grabbing releases"
        return subprocess.call("cat /etc/*-release")
        # cat /etc/lsb-release      # Debian based
        # cat /etc/redhat-release   # Redhat based

    def get_kernel(self):
        """
        get kernel info
        """
        print "[*] Grabbing Kernel information"
        kernel = subprocess.call("cat /proc/version")
        kernel += subprocess.call("uname -a")
        kernel += subprocess.call("uname -mrs")
        kernel += subprocess.call("rpm -q kernel")
        kernel += subprocess.call("dmesg | grep Linux")
        kernel += subprocess.call("ls /boot | grep vmlinuz-")
        return kernel

    def get_environment(self):
        """
        get system environment variables
        """
        environment = subprocess.call("cat /etc/profile")
        environment += subprocess.call("cat /etc/bashrc")
        environment += subprocess.call("cat ~/.bash_profile")
        environment += subprocess.call("cat ~/.bashrc")
        environment += subprocess.call("cat ~/.bash_logout")
        environment += subprocess.call("env")
        environment += subprocess.call("set")
        return environment

    def get_printers(self):
        """
        get any printers
        """
        return subprocess.call("lpstat -a")
