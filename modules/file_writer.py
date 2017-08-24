"""
file writer module
"""
from modules.logger import Logger
class FileWriter(object):
    """
    filewriter object
    """
    logger = Logger()

    def __init__(self, filename):
        self.filename = filename

    def write_output(self, command_output):
        """
        output
        """

        try:
            with open(self.filename, "w") as text_file:
                for output in command_output:
                    text_file.write("Command: {0}\nOutput: {1}\n\n".format(output, str(command_output[output]).rstrip()))
        except OSError as error:
            self.logger.error("Error writing output file{0}".format(error.message))
