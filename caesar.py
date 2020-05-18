def encrypt(text,key):
    encrypt_list = []     
    for item in text:
        if ord(item)>=97 and ord(item)<=122: #a~z
            encrypt_item = chr((ord(item)-ord('a')+key)%26+ord('a'))
            encrypt_list.append(encrypt_item)
            
        if ord(item)>=65 and ord(item)<= 90: #A~Z
            encrypt_item = chr((ord(item)-ord('A')+key)%26+ord('A'))
            encrypt_list.append(encrypt_item)
            
        if ord(item)>=48 and ord(item)<=57: #0~9
            encrypt_item = chr((ord(item)-ord('0')+key)%10+ord('0'))
            encrypt_list.append(encrypt_item)
        
    print(encrypt_list)
    encrypt_str="".join([str(i) for i in encrypt_list])
    
    
    return encrypt_str
def decrypt(text,key):
    decrypt_list = []     
    for item in text:
        if ord(item)>=97 and ord(item)<=122: #a~z
            decrypt_item = chr((ord(item)-ord('a')-key)%26+ord('a'))
            decrypt_list.append(decrypt_item)
            
        if ord(item)>=65 and ord(item)<= 90: #A~Z
            decrypt_item = chr((ord(item)-ord('A')-key)%26+ord('A'))
            decrypt_list.append(decrypt_item)
            
        if ord(item)>=48 and ord(item)<=57: #0~9
            decrypt_item = chr((ord(item)-ord('0')-key)%10+ord('0'))
            decrypt_list.append(decrypt_item)
        
    decrypt_str="".join([str(i) for i in decrypt_list])
    
    
    return decrypt_str

if __name__ == "__main__":
    plain_text = "afgh123AWQHF" 
    print("平文":,plain_text)
    encrypt_text = encrypt(plain_text,13)
    print("暗号文":,encrypt_text)
    decrypt_text = decrypt(encrypt_text,13)
    print("複号文":,decrypt_text)
    print("平文==複号文":,decrypt_text==plain_text)
