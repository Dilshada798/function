# def harshad(num):
#     i=1
#     sum=0
#     while i<1000:
#         if i%i==0:
#             sum=sum+i
#             if num==sum:
#                 print("perfect number",i)
#             else:
#                 print("not perfect number",i)
#         i=i+1
# num1=int(input("enter the number"))
# harshad()




def harshad ():
    i=1
    while i<1000:
        a=i%10
        b=(i//10)%10
        c=(i//10)//10
        d=a+b+c
        if i%d==0:
            print("harshad num",i)
        else:
            print("not harshad num",i)
        i=i+1
# num1=int(input("enter the number"))
harshad()

