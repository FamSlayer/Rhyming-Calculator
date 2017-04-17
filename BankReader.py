import time
# globally defined word bank. To access this, call Reader.getWords() rather than access Reader.words directly
words = set()

def parse ( silent=True, word_count=10000 ):
    start_time = time.time()
    fname = 'data/top_10000_tv_words.txt'

    if not silent:
        print "Parsing " + fname + " and creating word bank..."
    
    # define words that will be ignored and not added to the bank    
    words_to_ignore = ['o','mm','mmm','re','ed','y',"'em",'ok','shhh','ohh','ohhh','hm','hmmm','wh','lt',"y'know",'aah']

    # define abbreviations and what they will be substituted with
    abbreviations = {}
    abbreviations['mr.'] = 'mister'
    abbreviations['mrs.'] = 'missus'
    abbreviations['ms.'] = 'miss'
    abbreviations['dr.'] = 'doctor'
    abbreviations['st.'] = 'street'
    abbreviations['jr.'] = 'junior'

    # define the file name, open it, read it, and split it into a list of lines
    
    fh = open(fname,'r').read().split('\n')

    # define word_counter to 0, and parsing line by line
    word_counter = 0
    while word_counter < word_count and word_counter < len(fh):
        pieces = fh[word_counter].split()
        word = pieces[1].lower()
        
        if '.' in word:
            if word in abbreviations:
                words.add(abbreviations[word])
            elif not silent:
                pass
                #print "The following abbreviation was ignored:",word
        elif word in words_to_ignore:
            if not silent:
                print "   the following word was ignored:",word
        else:
            words.add(word)

        word_counter += 1

    if not silent:
        print ("--- Done in %s seconds ---" % (time.time() - start_time))

def getWords():
    if len(words) == 0:
        parse(False)
    return words

