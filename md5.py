import hashlib 
result = hashlib.md5('GeeksforGeeks') 
print("The byte equivalent of hash is : ", end ="") 
print(result.digest())
