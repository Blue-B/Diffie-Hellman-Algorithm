#공개키
p = 564646416516
g = 2


#비밀키
a = 6456
b = 1561
h = 546


print(f"공개키 p : {p}, g:{g}")
print(f"A의 비밀키: {a}\nB의 비밀키: {b}\n해커의 비밀키: {h}")

#각자 A,B,H의 공개키 생성
print()
print('A와 B는 비밀키를 사용하여 y=g^a mod p 계산하고 h도 비밀키를 사용하여 공개키를 계산하였다')
A = pow(g, a, p)
B = pow(g, b, p)
H = pow(g, h, p)
print("이때 해커가 메세지를 가로채어 A와 B의 키는 자신이 받고 해커의 공개키H를 A와 B에게 전송한다")


#공개용 비밀키 생성 (전달받은 공개 키,자신의 비밀키, mod p)
#A와 해커
print()
print("A는 이 사실을 모르고 해커에게 받은 공개키(H)로 공개용 비밀키를 생성한다")
Akey = pow(H, a, p)#A
print("해커는 A의 가로챈 공개키를 사용하여 공개용 비밀키를 생성한다 ")
AHkey = pow(A, h, p) #H


print()
#B와 해커
print("B는 이 사실을 모르고 해커에게 받은 공개키(h)로 공개용 비밀키를 생성한다")
Bkey = pow(H, b, p)#B
print("해커는 B의 가로챈 공개키를 사용하여 비밀키를 생성한다 ")
BHkey = pow(B, h, p)#H


print()
print(f"Akey: {Akey}\nAHkey :{AHkey}")
print("Akey와 AHkey의 결과값이 일치하며 해커는 A의 내용을 옅볼수있다")

print()
print(f"Bkey: {Bkey}\nAHkey :{BHkey}")
print("Bkey와 BHkey의 결과값이 일치하며 해커는 B의 내용을 옅볼수있다")