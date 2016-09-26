import string,re

#17
def palindrome(phrase):
    punctuation = string.punctuation + ' '

    clean_phrase = ""
    for letter in phrase:
        if letter not in punctuation:
            clean_phrase += letter.lower()

    return clean_phrase == clean_phrase[::-1]

# test
print(palindrome("Go hang a salami I'm a lasagna hog."))
print(palindrome("Was it a rat I saw?"))
print(palindrome("Step on no p"))

#18tggggggggggggggggggggggggggggggggggggggg
"""

A pangram is a sentence that contains all the letters of the English alphabet at least once,
 for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to
  check a sentence to see if it is a pangram or not.
"""

def pangram(phrase):
    c = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters = ""
    for char in phrase:
        for letter in alphabet:
            print(char,letter)
            if char == letter and char not in phraseLetters:
                phraseLetters += char
                print(phraseLetters)
    for char in phraseLetters:
        for letter in alphabet:
            if char == letter:
                print(char,letter)
                c += 1
    if c == 26:
        return True
    else:
        print phraseLetters, alphabet
        return False
print(pangram("the quick brown fox jumps over the lazy dog"))

#19
"""99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall."""
def song():
    a=99
    for a in range(99,0,-1):
        print("%d bottles of beer on the wall, %d bottles of beer.Take one down, pass it around, %d bottles of beer on the wall")%(a,a,a-1)

song()

#20

dict = {"merry":"god", "christmas":"jul", "and":"och","happy":"gott", "new":"nytt", "year":"ar"}

def translate(words):
	return map(lambda x: dict[x.lower()], words)

print translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year'])

#21

def freq(s):
    freqdict = {}
    for c in s:
        if c in freqdict:
            freqdict[c] += 1
        else:
            freqdict[c] = 1
    return freqdict

print freq("abbabcbdbabdbdbabababcbcbab")
print freq("hello")

#22

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
def crypto(s):
    return map(lambda x: key[x.lower()], s)

print crypto("abcd")

#23
def cor(sr):
    correct_str=re.sub('\ +',' ',sr)
    correct_str=re.sub('\.','. ',correct_str)
    return correct_str
print cor("This   is  very funny  and    cool.Indeed!. But      you should.try  this also")

#24
def plural(word):
    se={ 'o', 'ch', 's', 'sh', 'x', 'z'}
    if word.endswith('y'):
        return re.sub('y$', 'ies', word)
    elif word.endswith(se):
        return word + 'es'
    else:
        return word + 's'

print plural('ray')