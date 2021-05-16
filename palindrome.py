
def pal(str):
	rev = str[::-1]

	if (rev == str):
		#print("\nPalindrome!")
		return True
	#print("\nNot a palindrome.")
	return False

try: input = raw_input
except NameError: pass
inp = input("Enter a string to check if it is a palindrome: ")
pal(inp)
