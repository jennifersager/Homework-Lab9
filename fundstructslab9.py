#question 1
listA = []
listB = []

n = int(input("Enter the number of elements: "))

for i in range(0, n):
    num = int(input("Enter number: "))
    listA.append(num)

listB.append(listA[0] + listA[1])

for i in range(1, n - 1):
    listB.append(listA[i - 1] + listA[i] + listA[i + 1])

listB.append(listA[-2] + listA[-1])

print(listB)


#question 2
numdays = int(input("Enter the number of days: "))
daypay = 0.01
total = 0

print("Day    |    Salary")

print(1 , "     |    $" , daypay)

for i in range(2, numdays + 1):
    daypay = daypay * 2
    if i < 10:
        print(i , "     |    $" , round(daypay, 2))
    elif i < 100:
        print(i , "    |    $" , round(daypay, 2))
    else:
        print(i , "   |    $" , round(daypay, 2))

    total = total + daypay

print("Total: $", round(total + 0.01, 2))


#question 3
def _encrypt(plaintext):
    cipher = " "
    for c in plaintext:
        if c.isupper():
            cipher += chr(ord('A') + ((ord(c) - ord('A') + 3 - 103) % 26))
        elif c.islower():
            cipher += chr(ord('a') + ((ord(c) - ord('a') + 3 - 103) % 26))
        else:
            cipher += c
    print(cipher)

def _decrypt(ciphertext):
    plaintext = " "
    for c in ciphertext:
        if c.isupper():
            plaintext += chr(ord('A') + ((ord(c) - ord('A') - 3 - 105) % 26))
        elif c.islower():
            plaintext += chr(ord('a') + ((ord(c) - ord('a') - 3 - 105) % 26))
        else:
            plaintext += c
    print(plaintext)


text1 = input("Enter a string to encrypt: ")
_encrypt(text1)

text2 = input("Enter a string to decrypt: ")
_decrypt(text2)


#question 4
#a
X = int(input("Enter a number: "))
sum = 0

for i in range(1, X + 1, 1):
    sum += i

print(sum)
print(" ")

#b
for n in range(1, X + 1, 1):
    sum = 0
    for i in range(1, n + 1, 1):
        sum += i
    print(sum)

 
#question 5
x = int(input("Enter a number for x: "))
a = int(input("Enter a number for a: "))
y = 0
z = 0
b = 0
c = 0

if x > 100:
    y = 20
    z = 40
if a < 10:
    b = 1
    c = 0
if a < 10:
    b = 0
else:
    b = 99

print(y, z, b, c)


#question 6
def vowcons(sentence):
    vowels = 0
    cons = 0
    spaces = 0
    
    for l in sentence:
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' or l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
            vowels += 1
        elif l == ' ':
            spaces += 1
        else:
            cons += 1

    print("Vowels:", vowels)
    print("Consonants:", cons)

sentence = input("Enter a sentence: ")
vowcons(sentence)


#question 7
def sequence(N):
    print("The first N numbers of the sequence: ")
    for i in range(N):
        print(fib(i))
    print("The Nth number is", fib(i))


def fib(N):
    if N <= 1:
        return 1
    else:
        return fib(N - 1) + fib(N - 2)

    #print(num)

N = int(input("Enter a number: "))
sequence(N)














