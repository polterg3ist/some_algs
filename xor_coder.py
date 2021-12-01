def xor_coder(string, key): return ''.join([chr(x) for x in list(map(lambda x: x^key, [ord(x) for x in string]))])

    
print(xor_coder('ҚҷҾҾҽӾӲ҅ҽҠҾҶӳӳ', 1234))