#공개키
p=2465623456 
g=1236556

#비밀키 
a=4562  #A
b=153  #B

print(f"공개키 : p: {p}, g: {g}") 
print(f"A의 비밀키 :{a}") 
print(f"B의 비밀키 :{b}\n") 

#y = g^x mod p 이산대수문제의 어려움
#Akey=(g**a) % p   , Bkey=(g**b) % p
Akey=pow(g,a,p) 
Bkey=pow(g,b,p)
print("A는 비밀키를 사용하여 Akey=p**a % g의 계산결과를 B에게 전달") #A>b
print("B는 비밀키를 사용하여 Bkey=p**b % g의 계산결과를 A에게 전달\n") #B>A


print(f"A는 B로부터 계산된 Bkey: {Bkey}를 전달받음") #A
print(f"B는 A로부터 계산된 Akey: {Akey}를 전달받음\n") #B


KA=pow(Bkey,a,p)#B에게 받은 Bkey와 자신의 비밀키 a와 공개키 P를 사용하여 계산한다
print(f"B에게 받은 Bkey와 자신의 비밀키,공개키를 사용하여 계산한결과: {KA}")  #A

KB=pow(Akey,b,p)#A에게 받은 Akey와 자신의 비밀키 b와 공개키 p를 사용하여 계산한다
print(f"A에게 받은 Akey와 자신의 비밀키,공개키를 사용하여 계산한결과: {KB}\n") #B


print(f"KA : {KA}\nKB : {KB}")
print("KA와 KB의 결과는 일치하며 이값을 K로 데이터를 주고받는 암호키로 사용한다")
