# Iss text ko question3.txt ke naam ki file mein save karo. Iss file mein dhyaan se dekhoge toh ek insaan ka naam aur ek sheher ka naam milegaYeh sheher woh sheher hai jisme woh insaaan rehta hai. Ab aapne ek aisa code likhna hai jo: 1. Delhi mein rehne waale logon ko ek alag file mein daale. Delhi waali file ka naam "delhi.txt" hona chaiye. 
# 2. Shimla mein rehne waale logon ko ek alag file mein daale. Shimla waali file na naam "shimla.txt" hona chaiye 3. Aur saare log jo delhi aur shimla mein nahi rehte, unko ek alag file mein daale. Iss file ka naam "others.txt" hona chaiye

my_file=open("people1_exercise.txt","r")
for i in my_file:
    if "delhi"in i:
        a=open("delhi.txt","a")
        a.write(i)
    elif "shimla"in i:
        a=open("shimla.txt","a")
        a.write(i)

    else:
        a=open("other.txt","a")
        a.write(i)