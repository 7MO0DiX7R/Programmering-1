score = 0
print ("hello")
name = input("what is your name? ")
print (f"hello {name}, and welcome to my quiz about the best country China ")
Answer1 = input("which country is the strongest? ").capitalize()
if Answer1 == "China":

     score += 1500

     print(score, "Social credit")

else:
    score -= 1500
    print(score)

Answer2 = input("Is taiwan a country? ")
if Answer2 == "no" : 
   score += 1500 
   print(score, "Social credit")

else:
    score -= 1500
    print(score, "social credit")


print("A. Andrew tate\nB. Xi Jingping\nC. Kim Jong-Un")

Answer3 = input("who is china's President?").capitalize() 

if Answer3 == "Xi Jingping" or Answer3 == "B":
   score += 1500 
   print(score, "Social credit")
else:
    score -= 1500
    print(score, "social credit")

Answer4 = input("Who is the Top G? (first name only) ").capitalize()
if Answer4 == "Andrew":

     score += 1500

     print(score, "Social credit")

else:
    score -= 1500
    print(score)
if score == 6000:
    print("Good job, you got everything correct! ")
else:
    print (f"you got {score}/6000")