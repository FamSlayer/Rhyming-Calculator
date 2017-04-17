import time
import BankReader
from nltk.corpus import cmudict


def convert_to_string ( phonemes ):
    w = phonemes[0]
    for syl in phonemes[1:]:
        w += " " + syl
    return w

def buildDictionaries(arpabet, word_bank, silent=True):
    
    start_time = time.time()
    
    if not silent:
        print "Building dictionaries..."
        
    word_to_arpabet = {}
    arpabet_to_word = {}
    for word in word_bank:
        # some words like 'lookin' 
        if word in arpabet:
            alternate_pronunciations = []
            # save the word under all its pronunciations
            for alt in arpabet[word]:
                # convert the list of phonemes into a string
                converted = convert_to_string(alt)
                # add the pronunciation to the list of all pronunciations
                alternate_pronunciations.append(converted)
                # save the word as the result of this pronunciation
                arpabet_to_word[converted] = word

            # save all pronunciations for the word        
            word_to_arpabet[word] = alternate_pronunciations

    if not silent:
        print ("--- Done in %s seconds ---" % (time.time() - start_time))
    
    return word_to_arpabet, arpabet_to_word


word_to_pronunciations, pronunciations_to_word = buildDictionaries(cmudict.dict(), BankReader.getWords(), False)

def getPronunciations(word):
    if not word in word_to_pronunciations:
        print "The word '" + word + "' is not in the word bank"
        return []
    return word_to_pronunciations[word]

def getWord(pronun, list_given=False):
    if list_given:
        pronun = convert_to_string(pronun)
    if not pronun in pronunciations_to_word:
        print "The given pronunciation '" + pronun + "' matches no word in the word bank"
        return ""
    return pronunciations_to_word[pronun]

