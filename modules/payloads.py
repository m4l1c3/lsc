"""
Payloads module
"""
import glob
import os
from modules.logger import Logger

class Payloads(object):
    """
    Payloads object
    """

    logger = Logger()

    def __init__(self, payload_name):
        self.payload_name = payload_name
        return

    def generate_payload(self):
        """
        create usable payload on end destination
        todo have this concat all the files that are generated
        with a config or init script into a single bundle
        """
        try:
            if os.path.exists("./" + self.payload_name):
                os.remove("./" + self.payload_name)

            files = [x for x in glob.glob("./modules/*.py") if x != "./modules/__init__.py"]

            with open(self.payload_name, "w") as outfile:
                for filename in files:
                    with open(filename) as infile:
                        for line in infile:
                            outfile.write(line)

            if os.path.exists("./" + self.payload_name):
                return True
        except OSError as error:
            self.logger.error("Error creating payload: " + error.message)

        return False

    def get_payload_type(self):
        """
        determine what type of payload to generate, php, java, ruby, etc.
        """
        return self
