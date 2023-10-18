# Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length jyaada hogi use print karega aur agar dono strings ki length equal hui to dono ko line by line print karega . 
# Hint :- use len() builtin function.. Input:- Output :-
def Sangeeta (list) :
    i=0
    a=0
    while i<len(list):
        if a<len(list[i]):
            a=len(list[i])
            k=list[i]
        i=i+1
    print(k)
list=["sonam","poja","amisha"]
Sangeeta(list)


