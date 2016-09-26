#7
def reverse(s):
    return s[::-1]
print reverse("abc")
#8

def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
print palindrome("rara")

#9
lis={1,2,3}
def ismember(a,list):
    if a in list:
        return True
    else:

        return False

print ismember(2,lis)

#10
def overlapping(a,b):
   return

#11
def generate_n_chars(n,c):

    return n*c
print generate_n_chars(2,'o')

#12

def histo(a):
    for x in a:
        s=''
        n=x
        while(n>0):
            s = 'x'+s
            n-=1
        print(s)

histo(lis)


#13
def maxlist(a):
    return (max(a))
print maxlist(lis)

#14
strlis=['ab','aaa','rter','uuiu']
def map(a):
    new=[]
    for x in a:
        new.append(len(x))

    return new

print map(strlis)

#15
print(max(map(strlis)))
print"gfgjk"
#16
def filter(a,n):
    lise=[]
    for i in range(len(a)):
        if (len(a[i])>n):
            lise.append(a[i])
    return lise

print(filter(strlis,3))

