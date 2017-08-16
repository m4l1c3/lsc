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
        self.logger.normal_output("Running linux security check")
        op_sys = OperatingSystem()
        op_sys.run()
        


scanner = LCS()
scanner.main()