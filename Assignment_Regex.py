import re
name = input("Enter file: ")
if len(name) < 1 : name = "regex_sum_80936.txt"
f = open(name, 'r')

# The basic outline of this problem is to read the file
# look for integers using the re.findall()
# looking for a regular expression of '[0-9]+'
# and then converting the extracted strings to integers and summing up the integers.

numbers = re.findall(r"\d+", f.read())
numbers = list(map(int, numbers))
print(sum(i for i in numbers))


