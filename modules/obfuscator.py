"""
Obfuscation module
"""

import base64
# import hashlib

class Obfuscation(object):
    """
    Obfuscation object
    """
    def __init__(self):
        #todo possibly hash to conceal length?
        return

    @staticmethod
    def obfuscate(message):
        """
        obfuscate a message
        todo encrypt and encode data to send back
        """
        return base64.b64encode(message)

    @staticmethod
    def deobfuscate(message):
        """
        deobfuscate a message
        todo decode and decrypt data upon retrieval
        """
        return base64.b64decode(message)
