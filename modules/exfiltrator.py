"""
Exfiltration module
"""
import os
from modules.execute_command import ExecuteCommand
from modules.logger import Logger

class Exfiltration(object):
    """
    Exfiltration object
    """
    executor = ExecuteCommand()
    logger = Logger()

    def __init__(self):
        return

    def exfiltrate(self):
        """
        exfiltrate a message
        todo flesh out, probably something like determine a route home and push, nc wget, curl, etc.
        """
        filename = "data.tar.gz"

        try:
            Exfiltration.cleanup(filename)
            self.executor.execute_command("tar -czvf data.tar.gz ./lsc_*.lsc")

            if not Exfiltration.validate_output(filename):
                raise Exception("File archive not created.")
        except OSError as error:
            self.logger.error("Erroring archiving output: " + error.message)

    def find_channel(self):
        """
        determine channel or protocol to send through
        """
        return self

    @staticmethod
    def cleanup(filename):
        """
        cleanup exisiting output archive
        """

        if os.path.isfile("./" + filename):
            os.remove(filename)

    @staticmethod
    def validate_output(filename):
        """
        validate archive was created
        """
        if os.path.isfile("./" + filename):
            return filename
        return False
