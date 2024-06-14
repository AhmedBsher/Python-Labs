name = input('Enter file : ')
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
word = input('Enter the word : ')
if word in unique_words:
 print(f'The word "{word}" was found 
{unique_words[word]} times in the file')
else:
 print('This word does not exist in file')
 
def reverseWords(string):
 words = string.split()
 reversedWords = words[::-1]
 reversedString = List2string(reversedWords)
 return reversedString

def List2string(reversedWords):
 string = ''
 for word in reversedWords:
    string += word + ' '
 return string[:-1]
 
def main():
 string = "Ahmad Mahmoud Kandil"
 reversedString = reverseWords(string)
 print(reversedString)
main()