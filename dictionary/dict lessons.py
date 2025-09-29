# If you had the list ["cat", "dog", "elephant"], what would the dictionary look like if you mapped word → length?:
words = ["cat", "dog", "elephant"]
# use a dict comp to make each of the words value the length of its key:
#name the value expression
#name the key expression
#the for loop should be you looping over the  list and counting each string in it as the key value:
#the value expression is the length of each individual word while the for loop tells it the words
word_length = {word : len(word) for word in words}
print(word_length)

# word_length = {word : len(word) for word in words}
