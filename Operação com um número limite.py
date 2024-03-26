# s1= (1+2...+100)*2
# s2= 1**2 + 2**2 .... + 100**2
# r = s1 - s2
n=int(input('Digite um valor para ser colocado um limite: '))
s1= 0
x= 1 
while x <= n:
    s1= s1 + x
    x= x + 1
s1= s1**2  

print('=-'*100)
s2=0
x=1
while x <= n:
    s2= s2 + x**2
    x= x + 1 

r= s1 - s2 

print(r)



