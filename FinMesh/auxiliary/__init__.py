from nltk.corpus import words


def pick_bad_apples(word,ignore_list):
    ## Determines whether or not to ignore certain words
    ignore = False
    for n in range(len(ignore_list)):
        for i in ignore_list:
            if i in word:
                ignore = True
    return ignore
pick_bad_apples.__doc__= "Determines whether or not to ignore certain words."

def real_word_frequency(file):
    ## Returns a list fo real words sorted by use frequency
    with open(file,'r') as f:
        word_list = words.words()
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        file_words = []
        # Quick sieve that is used in bad_apples function to quickly throw out obvious unreal words
        ignore = ['-','_','/','=',':',';','<','>','#','$','@','*','\\']
        lines = f.readlines()
        word_freq = {}
        final_checked = {}
        # Iterate lines from file
        for line in lines:
            words = line.lower().strip().split(' ')
            # Iterate words from line
            for word in words:
                if not pick_bad_apples(word, ignore):
                    file_words.append(word)
        # Iterate words that pass bad apple check
        for w in file_words:
            if not w == '':
                length = len(w)-1
                # Checks if the first and last letter are in the alphabet
                if w[0] and w[length] in alphabet:
                    w.replace('.','').strip('\"')
                    if w in word_freq.keys():
                        word_freq[w] += 1
                    else:
                        word_freq[w] = 1

        # Runs a final check against an actual dictionary
        for key in word_freq.keys():
            if key in word_list:
                val = word_freq.get(key)
                final_checked[key] = val

        # Sort the words by frequency
        final_checked_sorted = {k: v for k, v in sorted(final_checked.items(), key=lambda item: item[1])}

        return final_checked_sorted
real_word_frequency.__doc__='Returns a list fo real words sorted by use frequency.'
