# Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length jyaada hogi use print karega aur agar dono strings ki length equal hui to dono ko line by line print karega . 
# Hint :- use len() builtin function.. Input:- Output :-
def sangeeta (lst) :
    i=0
    a=0
    while i<len(lst):
        if a<len(lst[i]):
            a=len(lst[i])
            k=lst[i]
        i=i+1
    print(k)
lst=["sonam","poja","amisha"]
sangeeta(lst)


