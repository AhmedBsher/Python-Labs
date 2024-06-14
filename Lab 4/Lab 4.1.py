name = input('Enter file: ')
handle = open (name, 'r')

all_words = list()
for line in handle:
    words = line.split()
    for word in words:
         all_words.append(word)

print (len (all_words))