"""
Environment object
"""
import os
from modules.logger import Logger

class Environments(object):
    """
    Environment object
    """
    logger = Logger()

    def __init__(self):
        self.env = {}

    def run(self):
        """
        generic run method
        """
        self.get_environment()

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
