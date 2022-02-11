question_list = [
"How many continents are there?", # pehla question
"What is the capital of India?",# doosra question
"NG mei kaun se course padhaya jaata hai?"]# teesra question
options_list = [
#pehle question ke liye options
["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#second question ke liye options
["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#third question ke liye options
["1.Software Engineering", "2.conselling", "3.Tourism", "4.Agriculture"]]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
options_list2=[["Nine","Seven"],["Cheenai","De.lhi"],["Software engineering","Agriculture"]]
solution_list2=[2,2,1]
i=0
Count=0
while i<len(question_list):
    print(question_list[i])
    print(options_list[i])
    lil=input("you want a lifeline:yes or no")
    if lil=="yes":
        if Count==0:
            print(options_list2[i])
            ans=int(input("choose the option"))
            if ans==solution_list2[i]:
                print("correct answer")
                Count+=1
            elif ans!=solution_list2[i]:
                print("incorrect answer")
                print("you lose the game")
                break
        else:
            print("you don't have lifeline")
            ans=int(input("choose the option"))
            if ans==solution_list[i]:
                print("entered correct answer")
    else:
        ans=int(input("choose the option"))
        if ans==solution_list[i]:
            print("entered correct answer")
            # print("you won the game")
        elif ans!=solution_list[i]:
            print("incorrect answer")
            print("lose the game")
            break
    if i==2:
        if ans==solution_list[i] or ans==solution_list2[i]:
            print("congratulation! you won the game")
    i=i+1
    # print("you won the game")





