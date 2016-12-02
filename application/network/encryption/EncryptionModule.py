from Crypto.Cipher import AES
from application import Config

class EncryptionModule:
    def __init__(self, key):
        self.m_key = key
        self.m_iv = 'k5G9Lkf$h8Uz6Bl9'
        self.pad = lambda s: s + (Config.ENC_BLOCK_SIZE - len(s) % Config.ENC_BLOCK_SIZE) * chr(Config.ENC_BLOCK_SIZE - len(s) % Config.ENC_BLOCK_SIZE)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encryptData(self, data):
        cryptomod = AES.new(self.m_key, AES.MODE_CBC, self.m_iv)
        return cryptomod.encrypt(self.pad(data))

    def decryptData(self, data):
        cryptomod = AES.new(self.m_key, AES.MODE_CBC, self.m_iv)
        return self.unpad(cryptomod.decrypt(data))
