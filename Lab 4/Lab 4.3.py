name = input('Enter file: ')
handle = open (name, 'r')
all_words = list()
for line in handle:
 words = line.split()
 for word in words:
     all_words.append(word)
unique_words = dict()
for w in all_words:
 unique_words[w] = 0
print (len(unique_words))