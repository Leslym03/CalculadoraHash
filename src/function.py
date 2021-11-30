import hmac 
import hashlib

def MD5(cad):
    hashObjectmd5 = hashlib.md5(cad.encode())
    resultmd5 = hashObjectmd5.hexdigest()
    return resultmd5

def MD4(cad):
    hashObjectmd4 = hashlib.new('md4', cad.encode())
    resultmd4 = hashObjectmd4.hexdigest()    
    return resultmd4

def SHA1(cad):
    hashObjectsha1 = hashlib.sha1(cad.encode())
    resultsha1 = hashObjectsha1.hexdigest()
    return resultsha1

def SHA256(cad):
    hashObjectsha256 = hashlib.sha256(cad.encode())
    resultsha256 = hashObjectsha256.hexdigest()    
    return resultsha256

