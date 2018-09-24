# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
    	continue
    num = float(line[20:])
    total = total + num
    count = count + 1
aver = total/count
print("Average spam confidence:", aver)
