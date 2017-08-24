"""
Printers
"""
from modules.logger import Logger
from modules.execute_command import ExecuteCommand

class Printers(object):
    """
    Printer checking object
    """
    logger = Logger()
    executor = ExecuteCommand()

    def __init__(self):
        self.printers = {}

    def run(self):
        """
        default run method
        """
        self.logger.normal_output("Running Printers")
        self.get_printers()

    def get_printers(self):
        """
        get any printers
        """
        self.logger.normal_output("Grabbing printers")
        self.printers.update({"printers lpstat": self.executor.execute_command("lpstat -a")})
