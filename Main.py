import time
start_time = time.time()

import BankReader
import Translate
from nltk.corpus import cmudict
arpabet = cmudict.dict()

# initialization time
print("--- Total initialization time = %s seconds ---\n" % (time.time() - start_time))

def ends_with(pronun, suffix):
    #print "pronunciation:\t'"+pronun+"'\t\tsuffix:\t'"+suffix+"'"
    index = pronun.find(suffix)
    if index == -1:
        return False
    if index + len(suffix) == len(pronun):
        return True
    return False


def getRhyming(given_word, count=-1):
    rhyming_words = set()

    # TO DO: ADD SELECTION FOR WHICH PRONUNCIATION THEY'D PREFER TO USE
    
    pronun = Translate.convert_to_string(arpabet[given_word][0])
    print pronun
    
    nemes = pronun.split()

    index = len(nemes)-1
    while index >= 0:
        if nemes[index][0] in ['A','E','I','O','U']:
            break
        index -= 1

    #print "last vowel sound:",nemes[index]
    
    last_vowel_sound_index = 0
    for n in nemes:
        if n != nemes[index]:
            #print last_vowel_sound_index,'\t', n, '\t',last_vowel_sound_index+len(n)+1
            last_vowel_sound_index += len(n) + 1
        else:
            break

    rhyme_string = pronun[last_vowel_sound_index:]
    print "Rhyming all words that end with '" + rhyme_string + "'"
    
    # simpleton brute force search method
    for word in Translate.word_to_pronunciations:
        if word != given_word:
            for pro in Translate.getPronunciations(word):
                if ends_with(pro, rhyme_string):
                    rhyming_words.add(word)
                
    return rhyming_words



user_word = raw_input("What word would you like to rhyme with? ")

print 'Words that rhyme with "' + user_word + '"'
start_time = time.time()
words = getRhyming(user_word)
end_time = time.time()
print words
# initialization time
print("\n--- Rhyming lookup time = %s seconds ---\n" % (end_time - start_time))





