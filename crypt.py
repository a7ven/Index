import string 
def crypt(data , key) : 
    arr = list(string.ascii_lowercase[key:] + string.ascii_lowercase[ : key ]) 
    arralpha = list(string.ascii_lowercase) 
    crypt = ""
    for x in data : 
        for j in range(len(arralpha)) : 
            if x == arralpha[j] : 
                crypt += arr[j]
    return crypt 


def decrypt(data , key) : 
    arr = string.ascii_lowercase[key:] + string.ascii_lowercase[ : key ] 
    arr = list(arr) 
    arralpha = list(string.ascii_lowercase) 
    decrypt = ""
    for x in data : 
         
        for j in range(len(arr)) : 
            if x == arr[j] : 
                decrypt += arralpha[j]
    return decrypt 

def get_key(data) : 
    arr = []
    for x in range(27):
        arr.append(decrypt(data , x))  
    return arr      

print(decrypt("jrmjuvxqjvnmnuvjrw" , 9 ))