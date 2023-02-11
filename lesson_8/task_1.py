"""Декодировать строку в байтовое значение"""

strr = b'r\xc3\xa9sum\xc3\xa9'
print(strr)
strr = strr.decode('utf-8')
print(strr)
strr = strr.encode('Latin1')
print(strr)
strr = strr.decode('Latin1')
print(strr)
