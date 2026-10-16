print("welcome to quiz game !")

play = input("Do you want to play ?")

if play.lower() != "yes":
    quit()

print("let's start the game ")

score = 0

# question 1
question = input("what does cpu stands for? ")
if question.lower() == 'central processing unit':
    print("correct !")
    score += 1
else:
    print("incorrect! ") 

# question 2

question = input("what does ram stands for? ")
if question.lower() == 'random access memory':
    print("correct !")
    score += 1
else:
    print("incorrect! ") 

# question 3


question = input("what does rom stands for? ")
if question.lower() == 'read only memory':
    print("correct !")
    score += 1
else:
    print("incorrect! ") 

# question 4

question = input("what does html stands for? ")
if question.lower() == 'hyper text markup language':
    print("correct !")
    score += 1
else:
    print("incorrect! ") 


# question 5

question = input("what does css stands for? ")
if question.lower() == 'Cascading Style Sheet':
    print("correct !")
    score += 1
else:
    print("incorrect! ") 


#  question 6

question = input("what does http stands for? ")
if question.lower() == 'hyper text transfer protocol ':
    print("correct !")
    score += 1
else:
    print("incorrect! ") 

 # question 7

question = input("what does https stands for? ")
if question.lower() == 'hyper text transfer protocol secure':
    print("correct !")
    score += 1
else:
    print("incorrect! ")  


print("your got" + str(score) +"questions correct!")
print("your got" + str((score/7)*100) + "%")    