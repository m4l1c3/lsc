"""
main module for scanner
"""
from modules.operating_system import OperatingSystem
from modules.logger import Logger

class LCS(object):
    """main class"""

    logger = Logger()

    def main(self):
        """
        main function for starting up scanner
        """
        op_sys = OperatingSystem()
        self.logger.normal_output("Running linux security check")


scanner = LCS()
scanner.main()