#공개키
p=2465623456 
g=1236556

#비밀키 
a=4562  #A
b=153  #B

print(f"공개키 : p: {p}, g: {g}") 
print(f"A의 비밀키 :{a}") 
print(f"B의 비밀키 :{b}\n") 


#Akey=g**a % p
#Bkey=g**b % p
Akey=((pow(g,a))%p) #파이썬 내장 pow함수로 g의 a제곱 형태로 계산가능   제곱후 나눠야하기때문에 pow를 ()로 감싸 제일 먼저 계산후 나머지를 구하도록함
Bkey=((pow(g,b))%p)

print("A는 Akey=p**a % g의 계산결과 Akey를 B에게 전달")
print("B는 Bkey=p**b % g의 계산결과 Bkey를 A에게 전달\n")

print(f"A는 B로부터 계산된 Bkey: {Bkey}를 전달받음")
print(f"B는 A로부터 계산된 Akey: {Akey}를 전달받음\n")


#KA=Bkey**a%p  
KA=((pow(Bkey,a))%p)#B에게 받은 Bkey와 자신의 비밀키 a와 공개키 P를 사용하여 계산한다
print(f"B에게 받은 Bkey와 자신의 비밀키,공개키를 사용하여 계산한결과: {KA}")  #A

#KB=Akey**b%p  
KB=((pow(Akey,b))%p)#A에게 받은 Akey와 자신의 비밀키 b와 공개키 p를 사용하여 계산한다
print(f"A에게 받은 Akey와 자신의 비밀키,공개키를 사용하여 계산한결과: {KB}\n") #B


print("KA와 KB의 결과는 일치하며 이값을 K로 데이터를 주고받는 암호키로 사용한다") 
