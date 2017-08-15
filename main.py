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
        op_sys.get_issues()
        op_sys.get_releases()
        # op_sys.get_kernel()
        # op_sys.get_environment()
        # op_sys.get_printers()
        self.logger.normal_output("Running linux security check")


scanner = LCS()
scanner.main()