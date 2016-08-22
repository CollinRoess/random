plaintext=raw_input("Enter plaintext to be encrypted here: ")
alphabet=[]
for char in "abcdefghijklmnopqrstuvwxyz":
	alphabet.append(char)

ciphertext=[]
for char in plaintext:
	ciphertext.append(alphabet[(alphabet.index(char)+13)%26])
	
ciphertext=''.join(ciphertext)
print ciphertext