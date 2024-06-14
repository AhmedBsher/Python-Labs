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
for w in all_words:
 unique_words[w] += 1
 
Max = 0
mostFrequent = ''
for i in unique_words:
 if unique_words[i] > Max:
    Max = unique_words[i]
 mostFrequent = i 
print(f'most frequent word is {mostFrequent}')