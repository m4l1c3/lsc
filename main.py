"""
main module for scanner
"""
from modules.operating_system import OperatingSystem
from modules.networking import Networking
from modules.logger import Logger

class LCS(object):
    """main class"""

    logger = Logger()

    def main(self):
        """
        main function for starting up scanner
        """
        self.logger.normal_output("Running linux security check")
        self.op_sys = OperatingSystem()
        self.networking = Networking()
        self.op_sys.run()
        self.networking.run()
        


scanner = LCS()
scanner.main()