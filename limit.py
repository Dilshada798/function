# def a(limit):
#     i=0
#     sum=0
#     while i<=limit:
#         if i%3==0 or i%5==0:
#             sum=sum+i
#         i=i+1
#     print(sum)
# a(10)

# if False:
#     print("false")
# print("true")


# a=[20,2,30,90,50,56]
# b=a[0]
# c=a[0]
# i=0
# while i<len(a):
#     if b<a[i]:
#         b=a[i]
#     if c>=a[i]:
#         c=a[i]
#     i=i+1
# print(b)
# print(c)

a=[1,2,3,4,5,6,7,8]
b=[]
c=[]
d=[]
e = []
i=0 
while i<len(a):

    if i <2:
        b.append(a[i])
    elif i < 4:
        c.append(a[i])
    elif i < 6:
        d.append(a[i])
    else:
        e.append(a[i])
    i = i + 1
print(b,c,d,e)


    # x=a[0],a[1]
    # s=a[2],a[3]
    # b.append([x])
    # c.append([s])
    # print(b)
    # i=i+1
# print(b,c)









# num=int(input("enter the number"))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i=i+1

# num=int(input("enter the number"))
# n=int(input("enter the number"))
# i=num
# while i<=n:
#         j=1
#         while j<=10:
#             print(i,"*",j,"=",i*j,end=" ") 
#             j=j+1        
#         i=i+1 



# num=int(input("entetr the no."))
# num2=int(input("enter the year"))
# i=num
# while i<=num2:
#     a=i
#     if a%4==0 or a%400==0 or a%100==0:
#         print(a,"leap year")
#     else:
#         print(a,"not a leap year")
#     i=i+1


# # # a=int(input("enter the no."))
# # # b=int(input("enter the npo."))
# # # i=1
# # # while i<=b:
# # #     j=1
# # #     while j<=10:
# # #         print(i,"*",j,"=",(i*j),end=" ")
# # #         j=j+1
# # #     print()
# # #     i=i+1