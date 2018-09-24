# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
	if not line.startswith("From:"): 
			continue
	line = line.rstrip()
	line = line.split()	
	email = line[1]
	counts[email] = counts.get(email, 0) + 1

maxcount = 0
maxword = None
for word, count in counts.items():
	if count > maxcount:
		maxword = word
		maxcount = count
print(maxword, maxcount)

