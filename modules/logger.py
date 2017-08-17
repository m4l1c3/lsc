"""
Logging module
"""
from termcolor import colored

class Logger(object):
    """
    Logging object for writing status to command line
    """
    def __init__(self):
        return

    def error(self, output):
        """
        log error message to console
        """
        print colored("[*] " + output, "red")

    def warning(self, output):
        """
        log warning to console
        """
        print colored("[*] " + output, "yellow")

    def debug(self, output):
        """
        log debug to console
        """
        print colored("[*] " + output, "green")

    def normal_output(self, output):
        """
        log normal output
        """
        print colored("[*] " + output, "cyan")
