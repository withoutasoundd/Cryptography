import os
def aton(letter):	
	switcher={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
		'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,
		'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
	return switcher.get(letter)

def ntoa(num):
	switcher={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
		 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14:'O', 15: 'P', 16: 'Q',
		 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
	return switcher.get(num)
	
def cypher_cesar(string):	
	temp=''
	for i in range(0,len(string)):
		temp+=ntoa((aton(string[i])+3)%26)	
	return temp

def decypher_cesar(string):
	temp=''
	for i in range(0,len(string)):
		temp+=ntoa((aton(string[i])-3)%26)	
	return temp

def lpolybe(letter):
	switcher={'A':11,'B':12,'C':13,'D':14,'E':15,
		'F':21,'G':22,'H':23,'I':24,'J':24,'K':25,
		'L':31,'M':32,'N':33,'O':34,'P':35,
		'Q':41,'R':42,'S':43,'T':44,'U':45,
		'V':51,'W':52,'X':53,'Y':54,'Z':55}
	return switcher.get(letter)
def npolybe(n):
	switcher={11:'A',12:'B',13:'C',14:'D',15:'E',
		21:'F',22:'G',23:'H',24:'I',24:'J',25:'K',
		31:'L',32:'M',33:'N',34:'O',35:'P',
		41:'Q',42:'R',43:'S',44:'T',45:'U',
		51:'V',52:'W',53:'X',54:'Y',55:'Z'}
	return switcher.get(n)

def cypher_polybe(string):
	temp=''
	for i in range(0,len(string)):
		temp+=str(lpolybe(string[i]))
	return temp

def decypher_polybe(string):
	r=''
	for i in range(0,len(string),2):
		a=string[i]
		b=string[i+1]
		c=a+b
		r+=str(npolybe(int(c)))
	return r
	        
def cypher_affine(string):
	print("Give two numbers a and b with PGCD(a,26) must equal 1 :\n")
	a=int(input("a = "))
	b=int(input("b = "))
	r,u,v=inv_modulaire(a,26)
	while (r!=1):
		print("Wrong, give 2 numbers again with PGCD(a,26)=1\n")
		a=int(input("a = "))
		b=int(input("b = "))
		r=pgcd(a,26)
	print("PGCD(a,26) validated "+str(a)+"("+str(u)+")"+" + "+str(b)+"("+str(v)+")"+" =1\n")
	temp=''
	for i in range(0,len(string)):
		r=int(a*aton(string[i])+b)%26
		temp+=str(ntoa(r))
	return temp

def inv_modulaire(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd,x,y
    
def decypher_affine(string):
	temp=''
	print("Give your key (a,b) :\n")
	a=int(input("a = "))
	b=int(input("b = "))
	pp,iv,pp=inv_modulaire(a,26)
	for i in range(0,len(string)):
		pos=int(aton(string[i]))
		temp+=str(ntoa((iv*(pos-b))%26))
	return temp 

def cypher_delastelle(string):
	l1=[]
	l2=[]
	for i in range(0,len(string)):
		n=str(lpolybe(string[i]))
		l1.append(n[0:1])
		l2.append(n[1:2])
	l3=l1+l2
	temp=''
	for i in range(0,len(l3)):
		temp+=l3[i]
	return temp

def decypher_delastelle(string):
	i2=int(len(string)/2)
	end=i2
	temp=''
	for i in range(0,end):
		a=string[i]
		b=string[i2]
		r=a+b
		temp+=str(npolybe(int(r)))
		i2+=1
	return temp
					
#menu screen part
k=1

while(k!=0):
	print("\n	Welcome to the message Encrypter / Decrypter\n")
	r=int(input("Do you want to : \n	1 : Encrypt ?\n	2 : Decrypt ?\n	3 : Leave?\n"))
	if (r==1):
		os.system("clear")
		a=int(input("Choose your option\n\n	1 : Cesar's_encryption\n	2 : Polyb's _encryption\n	3 : Affine's encryption\n	4 : Delastelle's encryption\n	5 : Previous screen\n	6 : Quit\n"))
		if (a==1):
			msg=input('\nType your clear message here\n')
			print('Your crypted message is : '+cypher_cesar(msg))
			print("\n")
		elif (a==2):
			msg=input('\nType your clear message here\n')
			print('Your crypted message is : '+cypher_polybe(msg))
			print("\n")
		elif(a==3):
			msg=input('\nType your clear message here\n')
			msge=cypher_affine(msg)
			print('Your crypted message is : '+msge)
		elif(a==4):
			msg=input('\nType your clear message here\n')
			msge=cypher_delastelle(msg)
			print('Your crypted message is : '+msge)
		elif (a==5):
			os.system("clear")
		elif (a==6):
			k=0
			os.system("clear")
	elif(r==2):
		os.system("clear")
		a=int(input("Choose your option\n\n	1 : Decrypt Cesar\n	2 : Decrypt Polyb\n	3 : Affine's decryption\n	4 : Delastelle's decryption\n 	5 : Previous screen\n	6 : Quit\n"))
		if (a==1):
			msg=input('\nType your crypted message here\n')
			print('Your clear message is : '+decypher_cesar(msg))
			print("\n")
		elif (a==2):
			msg=input('\nType your crypted message here\n')
			print('Your clear message is : '+decypher_polybe(msg))
			print("\n")
		elif(a==3):
			msg=input('\nType your crypted message here\n')
			msge=decypher_affine(msg)
			print('Your clear message is : '+msge)
		elif(a==4):
			msg=input('\nType your crypted message here\n')
			msge=decypher_delastelle(msg)
			print('Your clear message is : '+msge)
		elif (a==5):
			os.system("clear")
		elif (a==6):
			k=0
			os.system("clear")
	
	else:
		k=0
		os.system("clear")
	
	







