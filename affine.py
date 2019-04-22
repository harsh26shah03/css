def affine_encrypt(text, key):
    for i in text: print(chr(((key[0]*ord(i) + key[1] ) % 26)+65))
    

def main():
	text = input("Enter message to encrypt : ")
	key = [17, 20]
	affine_encrypt(text, key)

if __name__ == '__main__': 
	main()
