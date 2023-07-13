##YDR TO JOAAT PYTHON CONVERTER##
##BY ICMP & JZERSCHE##
##JUST DROP YOUR YDR INTO A FOLDER##
##CHANGE THE folder_path BELOW##

import os
import time

def int32(i:int)->int:
    return i & 0xFFFFFFFF

def signedInt32(i:int)->int:
    return i | (-(i & 0x80000000))

def signedInt8(i:int)->int:
    return i | (-(i & 0x80))

def unsignedInt(i:int)->int:
    return i if i >= 0 else i + (1 << 32)

def hexToStr(h:int)->str:
    return str(h)[2:].upper().rjust(8, "0")

def intToStr(i:int)->str:
    return str(hex(unsignedInt(i)))[2:].upper().rjust(8, "0")

def unsignedHex(h:int)->int:
    return hex(unsignedInt(h))

def strToHex(s:str)->int:
    return hex(int32(int("0x" + s.rjust(8, "0"), 16)))

def joaat(s:str)->dict:
    hash = 0
    for c in s.strip().lower().encode("utf8"):
        hash = int32(hash + signedInt8(c))
        hash = int32(hash + (hash << 10))
        hash = int32(hash ^ (hash >> 6))
    hash = int32(hash + (hash << 3))
    hash = int32(hash ^ (hash >> 11))
    hash = int32(hash + (hash << 15))

    return {
        "unsigned": hash,
        "signed": signedInt32(hash),
        "hex": hex(hash),
        "str": hexToStr(hex(hash)),
    }

def get_file_names(folder_path):
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_name_without_extension = os.path.splitext(file_name)[0]
            joaat_hash = joaat(file_name_without_extension)['unsigned']
            file_names.append((file_name_without_extension, joaat_hash))
    return file_names

# Example usage
folder_path = 'C:\\Users\\ICMP\\Desktop\\TryingShit\\ydrtest'  # Replace with the actual folder path
file_names = get_file_names(folder_path)
for file_name, joaat_hash in file_names:
    print(f"File Name: {file_name}, JOAAT Hash: {joaat_hash}")
time.sleep(120) 
