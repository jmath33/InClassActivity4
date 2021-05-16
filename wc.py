def count(str):
	words = len(str.split())
	return words

try: input = raw_input
except NameError: pass
inp = input("Enter a sentence to see how many words are in it: ")
count(inp)
