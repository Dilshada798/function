def questions():
    question_list = [
        "How many continents are there?",              # pehla question
        "What is the capital of India?",            
        "NG mei kaun se course padhaya jaata hai?"    
    ]
    return question_list
questions_new=questions()

def options():
    options_list = [
        #pehle question ke liye options
        ["Four", "Nine", "Seven", "Eight"],
        #second question ke liye options
        ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
        #third question ke liye options
        ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
    ]
    return options_list
options_new=options()

def solution():
    solution_list = [3, 4,1]
    return solution_list

solution_new=solution()


def answers():
    answer_list=[
        ["1 four","3 seven"],
        ["2 Bhopal","4 Delhi"],
        ["1 software engineering","4 agriculture"]
     
    ]
    return answer_list
answers_new=answers()

print("KAUN BANAYGA CODEPATI (KBC)")
i=0
s=0
count=0
while i<len(questions_new):
    print(questions_new[i])
    a=0
    b=i
    while a<len(options_new[i]):
        k=options_new[b][a]
        print(a+1,k)
        a=a+1
    if count<1:
        num1=input("do you want 5050 lifeline")

        if num1=="yes":
            k=0
            while k<len(answers_new[i]):
                print(answers_new[b][k])
                k+=1
            # print(answers_new[b])
            num2=int(input("enter your answer"))
            if num2==solution_new[i]:
                s+=10000
                print("your answer is correct")
                print ("you win Rs/",s)
            else:
                print("incorrect answer")
                print("you can't play again")
                print("you win Rs/",s)
                break
            count+=1
            
        else:
            pass
            m=int(input("enter your answer:"))
            if m==solution_new[i]:
                print("congrats your answer is right")
                s+=10000
                print("you win Rs/",s)
            else:
                print("No chance")
                print("your answer is wrong")
                print("you win",s)
                break
              
    else:
        pass
        k=int(input("enter your answer"))
        if k==solution_new[i]:
            print("right answer")
            s+=10000
            print("you win Rs/",s)
        else:
            print("no chance")
            print("your answer is wrong")
            print("you win Rs/",s)
            break
    i=i+1
    print("______congrulation you are a part of____KON BANAYGA CODEPATI___")
    print("you win Rs/",s)
    print("THANKYOU BEING PART OF KBC")

            
            


