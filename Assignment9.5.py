name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
	if not line.startswith("From "): 
			continue
	line = line.rstrip()
	line = line.split()	
	time = line[5]
	hour = time.split(":")
	new_hour = hour[0]
	counts[new_hour] = counts.get(new_hour, 0) + 1

for key, value in sorted(counts.items()):
	print(key, value)