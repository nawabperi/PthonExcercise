from django.shortcuts import render

# Create your views here.
def max(a,b): #1
    if(a>b):
        return a
    else:
        return b

def length(strin):#3
    print len(strin)

length("abcd")


def vowel(s):#4
    if (s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'):
            return True
    else:
            return False

print vowel("a")

print max(6,9)

#5
def translate(s):
    consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for letters in s:
            if letters in consonant:
                print(letters+"O"+letters)
            else:
                return("Vowel")
translate("is")


#6

lis=[1,2,3]

def add(lis):
    s = 0
    for i in lis:
        s+=i
    return s

print add(lis)

def mul(lis):
    s = 0
    for i in lis:
        s+=i
    return s

print mul(lis)

