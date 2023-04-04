import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Cripto:
    def __init__(self, key: bytes) -> None:
        self.key = key
        self.iv = secrets.token_bytes(16)

    def encryption(self, data: str) -> str:
        item_bytes = data.encode('utf-8')
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
        ct_bytes = cipher.encrypt(pad(item_bytes, AES.block_size))
        encod_string = ct_bytes + self.iv
        return encod_string.hex()

    def decoding(self, data: str) -> str:
        data_bytes = bytes.fromhex(data)
        ct_bytes = data_bytes[:-16]
        iv = data_bytes[-16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        pt_bytes = cipher.decrypt(ct_bytes)
        pt = unpad(pt_bytes, AES.block_size).decode()
        return pt
