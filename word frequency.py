# word frequency
sentence = input('Enter a sentece:')
# asking for a sentence

def word_count(setning):
    setning = setning.strip()
    # clearing the sentence of unwanted white spaces
    symbols = ['!', '@', '#', '$', '%', '^', '&','*','(',')','-', '/', '?', ',', '.']
    
    for symbol in symbols:
        if symbol in setning:
            setning =  setning.replace(symbol, '')
        else: pass
    # removing symbols, to prevent 'em of being counted as words
    setning = setning.upper().split(' ')
    # uppercasing the sentence for a universalcountabillity 
    # and spliting each word, thus turning the sentence to a list
    
    word_requency = {}

    for word in setning:
        if word in word_requency:
            word_requency[word] += 1
            # if the word exists in the dictionary, it's frequency gets incremented
        else:
            word_requency[word] = 1
            # if the word doesn't exists in the dictionary, the word get's added in the
            # dictionary with the frequency of 1

    for key, value in word_requency.items():
        print(f'{key} : {value}' )
    # printing each word with it's respective frequency in a visually understandable way

word_count(sentence)
# calling the function 



#--------------------------------------------------------------------------------------------------------------------------------------------
# ALTERNATIVE
#============================================================================================================================================
from collections import Counter

def collections_word_counting(setning):
    setning = setning.strip()
    # clearing the sentence of unwanted white spaces
    symbols = ['!', '@', '#', '$', '%', '^', '&','*','(',')','-', '/', '?', ',', '.']
    
    for symbol in symbols:
        if symbol in setning:
            setning =  setning.replace(symbol, '')
        else: pass
    # removing symbols, to prevent 'em of being counted as words
    setning = setning.upper().split(' ')

    word_count_pair = Counter(setning).most_common(len(setning))
    # a list of tuples that contain each word and it's total count
    count = 0
    # functions as an index
    for i in word_count_pair:
        # looping through the tuple list 
        print(f'{count}) {i[0]}  :{i[1]}')
        # printing each pair and an index
        count += 1
        # increment the index for the next iteration
    
# remember to call the function
