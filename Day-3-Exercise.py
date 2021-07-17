# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Way 1
true = love = 0
both = (name1 + name2).lower()w
true += both.count("t")
true += both.count("r")
true += both.count("u")
true += both.count("e")

love += both.count("l")
love += both.count("o")
love += both.count("v")
love += both.count("e")

print(f"Your score is {str(true) + str(love)}")

# Way 2
true = love = 0
both = (name1 + name2).lower()
string1 = "true"
string2 = "love"
for x in range(len(both)):
    for y in range(len(string1)):
        if both[x] == string1[y]:
            true += 1
    for z in range(len(string2)):
        if both[x] == string2[z]:
            love += 1
print(f"Your score is {str(true) + str(love)}")
