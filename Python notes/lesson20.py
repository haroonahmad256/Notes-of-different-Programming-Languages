#kon bna ga kror pati
print("This is the game Kon Bne Ga krore pati")
print("There will be total 10 Questions")
print("For each correct answer 1 crore will re rewarded")
print("And if you give all anwers correct you will win 15 crore")
Questions_kbc= []
question_options= []
Answers_kbc= [3, 2, 4, 2, 1, 1, 3, 2, 2, 2]
question1= "Q1 Which of these is the name of kind of shot in badmintion?"
question2= "Q2 What is the national flower of Pakistan??"
question3= "Q3. Which is the largest ocean in the world?"
question4= "Q4. What is the largest organ of the human body?"
question5= "Q5. What was the first capital of Pakistan?"
question6= "Q6. How far is the Sun from Earth (approx.)?"
question7= "Q7. Who founded Microsoft?"
question8= "Q8. Which is the largest country in the world (by area)?"
question9= "Q9. What is the chemical formula of water?"
question10= "Q10. Which is the highest peak in Pakistan?"

Questions_kbc.append(question1)
Questions_kbc.append(question2)
Questions_kbc.append(question3)
Questions_kbc.append(question4)
Questions_kbc.append(question5)
Questions_kbc.append(question6)
Questions_kbc.append(question7)
Questions_kbc.append(question8)
Questions_kbc.append(question9)
Questions_kbc.append(question10)


option1= "1.Bounce      2.Yorker    3.Drop      4.Bout"
option2= "1.Rose        2.Jasmine   3.Lotus     4.Sunflower"
option3= "1.Indian Ocean    2. Atlantic Ocean   3. Southern Ocean   4. Pacific Ocean"
option4= "1.Brain       2. Skin     3. Liver    4. Heart"
option5= "1.Karachi     2. Lahore   3. Peshawar 4. Islamabad"
option6= "1.93 million miles    2. 50 million miles    3. 150 million miles    4. 200 million miles"
option7= "1.Mark Zuckerberg   2. Larry Page   3. Bill Gates   4. Elon Musk"
option8= "1.China       2. Russia   3. India    4. USA"
option9= "1.CO₂           2. H₂O      3. O₂       4. H₂SO₄"
option10= "1.Nanga Parbat   2. K2   3. Rakaposhi    4. Broad Peak"
question_options.append(option1)
question_options.append(option2)
question_options.append(option3)
question_options.append(option4)
question_options.append(option5)
question_options.append(option6)
question_options.append(option7)
question_options.append(option8)
question_options.append(option9)
question_options.append(option10)


anwers_marked= []
count=0
for i in range(0,10):
    print(Questions_kbc[i])
    print(question_options[i])
    solution= int(input("Enter answer of question(1-4) or 0 to quit: "))
    anwers_marked.append(solution)
    if(anwers_marked[i]==0):
        break
    elif (Answers_kbc[i]== anwers_marked[i]):
        print("Conguratulation! Your answer is correct")
        count+=1
    elif (Answers_kbc[i]!= anwers_marked[i]):
        count=0
    else:
        print("Your answer is not correct")

    

print(f"Your correct answers: {count}")

prize_money=0
if (count==1):
    prize_money= 1
elif (count==2):
    prize_money=2
elif (count==3):
    prize_money=3
elif (count==4):
    prize_money=4
elif (count==5):
    prize_money=5
elif (count==2):
    prize_money=6
elif (count==7):
    prize_money=7
elif (count==8):
    prize_money= 8
elif (count==9):
    prize_money=9
elif (count==10):
    prize_money=10
elif(count==0):
    print("Sorry You have won nothing")

print(f"Conguratulations! You have won {prize_money} crore")
