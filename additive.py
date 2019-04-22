def encrypt(text,s): 
	result = "" 
	for i in range(len(text)): 
		char = text[i] 
		result += chr((ord(char) + s) % 26 + 65) 
	return result 
text = "ATTACKATONCE"
s = 4
print("Text : " + text )
print("Shift : " + str(s))
print("Cipher: " + encrypt(text,s))
