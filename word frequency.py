# word frequency
sentence = input('Enter a sentece:')
# asking for a sentence

def removal(setning):
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

removal(sentence)
# calling the function 
