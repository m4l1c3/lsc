"""
main module for scanner
"""
from modules.operating_system import OperatingSystem
from modules.networking import Networking
from modules.services import Services
from modules.printers import Printers
from modules.logger import Logger
from modules.environments import Environments
from modules.exfiltrator import Exfiltration

class LCS(object):
    """main class"""

    logger = Logger()
    op_sys = OperatingSystem()
    networking = Networking()
    services = Services()
    printers = Printers()
    environments = Environments()
    exfiltrator = Exfiltration()

    def __init__(self):
        self.main()

    def main(self):
        """
        main function for starting up scanner
        """
        self.logger.normal_output("Running linux security check")
        self.run()

    def run(self):
        """
        default run method
        """
        self.op_sys.run()
        # self.networking.run()
        # self.services.run()
        # self.environments.run()
        self.exfiltrator.exfiltrate()

LCS()
