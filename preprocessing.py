# so we have to read in the harry porter file as per labs instructions.

# modules
import re 

# this is the function to extract unique words from a sentence
# it will return a list of unique words in lower case
# punctuation is removed from the words
# this function will be used to extract unique words from each line of the file
def extract_unique_words(sentence):
      unique_words = set()
      words = sentence.split(' ')
      for word in words:
            cleaned_word = re.sub(r'[^\w\s]', '', word)
            if cleaned_word not in unique_words:
                  unique_words.add(cleaned_word)
      results = []      
      for word in unique_words:
            results.append(word)
      return results
     

with open('harry_potter/HP1.txt', 'r') as harry_porter_file:

      for line in harry_porter_file:
            
            unique_words = extract_unique_words(line)
            print(unique_words[-1])


