import time, os

from string import punctuation




#28
strList=['ab','abc','ahkh','w']
def find_longest_word(x):
    return len(x)
print max(map(find_longest_word,strList))

#29
def filter_long_words(words, n):
    return filter(lambda x: len(x) > n, words)

print filter_long_words(strList,2)

#30
eng = {"merry":"god", "christmas":"jul", "and":"och","happy":"gott", "new":"nytt", "year":"ar"}

def translate(i):
	return map(lambda x: eng[x.lower()], i)

print translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year'])

#32

def palindrome_io(file_, mode):
    stuff = "`~!@#$%^&*()_-=+[]{}\|;:,<.>/?"
    with open(file_, mode) as f:
        for line in f:
            for char in line:
                if char in stuff:
                    line = line.replace(char, "")
            if line.lower().strip() == line[::-1].lower().strip():
                print True
            else:
                print False
palindrome_io("/home/consultadd/Documents/x.txt","r+")




#33
def semordnilap(filepath,mode):
    file = open(filepath)
    words = file.read().split()
    results = []
    for w1 in words:
        for w2 in words:
            if w1 == w2[::-1]:
                results.append(w1)
    return results
print semordnilap("/home/consultadd/Documents/semo.txt","r+")


#34

def char_freq_table(filepath,mode):
    file = open(filepath)
    chars = file.read().lower().replace(" ", "").replace("\n", "")

    freqs = {key: 0 for key in chars}

    for char in chars:

        freqs[char] += 1
    for word in freqs:

        print "%s: %s" % (word, freqs[word])

char_freq_table("/home/consultadd/Documents/x.txt","r+")


#35

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
	 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',
	 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar',
	 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
	 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
	 'z':'zulu'}
w=[]
def icao(txt, icao_pause=1, word_pause=3):

	words = txt.split() # Take each word from provided string

	for word in words: # For every word in the provided string
		for char in word:

            # For every character in the word
			if char not in punctuation:
				w.append( d[char.lower()])
        return w
				#time.sleep(icao_pause) # The wait time after every letter
		#time.sleep(word_pause) # The wait time after every word


print icao("Hello world, hi, I'm Nick!", 0.10, 1)
print icao("The quick brown Fox jumps over the laZy Dog!")

#38
def wordAvg(file_name):
	with open(file_name, 'r') as f:
		for line in f:
			# Clean each line of punctuations, we want words only
			line = filter(lambda x: x not in punctuation, line)
			# We get only the length of the words
			words = map(len, line.split())
	print sum(words) / len(words)


wordAvg("/home/consultadd/Documents/x.txt")