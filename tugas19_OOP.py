kesempatan = 3

while kesempatan > 0:
      username = input("username : ")
      password = input("password : ")
 
if  username == "admin" and password =="123":
      print("login berhasil")
break
else:
    kesempatan -=1
    print("login gagal")
    print("sisa kesempatan :", ksempatan)
    
kesempatan = 3

while kesempatan >0:
    username = input("username :")
    password = input("password")
    
if username == "admin" and password == "123":
       print("login berhasil")
       break
else:
       kesempatan -= 1
       print("login gagal")
       print("sisa kesempatan :", kesempatan)
       
     
