# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna

from calendar import c
from re import A


def best(name):
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
    print(f"{name} is da best")

best("Mohammed")
best("En till Mohammed")
best("Samma Mohammed")

def square(number):
    # TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut
    return number**2

print (square(9))
print (square(6))
print (square(3))


def sums(a, b):
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
    return a + b

print (sums(2, 5))
print (sums(1, 6))
print (sums(3, 4))

# Nu blir det lite svårare


def maximum(a, b, c):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    if a > b and a > c:
     return a
    elif b < c:
     return c
    else: 
     return b
print (maximum(3,5,12))
    
def palindrom(ord):
    l = len(ord)
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    if ord[0] = ord[-1] and ord[1] = -2 and 2 = -3 and 3 = -4

palindrom("anna")

 


def prime(nr):
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut
    pass