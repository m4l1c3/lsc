"""
Environment object
"""
from modules.logger import Logger
from modules.execute_command import ExecuteCommand

class Environments(object):
    """
    Environment object
    """
    logger = Logger()
    executor = ExecuteCommand()

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
        self.env.update({"profile": self.executor.execute_command("cat /etc/profile")})
        self.logger.normal_output("Grabbing bashrc")
        self.env.update({"bashrc": self.executor.execute_command("cat /etc/bashrc")})
        self.logger.normal_output("Grabbing bash profile")
        self.env.update({"bashprofile": self.executor.execute_command("cat ~/.bash_profile")})
        self.logger.normal_output("Grabbing bashrc")
        self.env.update({"bashrc": self.executor.execute_command("cat ~/.bashrc")})
        self.logger.normal_output("Grabbing logout")
        self.env.update({"bash logout": self.executor.execute_command("cat ~/.bash_logout")})
        self.logger.normal_output("Grabbing env")
        self.env.update({"env": self.executor.execute_command("env")})
        self.logger.normal_output("Grabbing set")
        self.env.update({"set": self.executor.execute_command("set")})
