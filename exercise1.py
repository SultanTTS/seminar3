try:
     a=int(input("Первое число="))
     b=int(input("Второе число="))
     c=int(input("Третье число="))
     d=int(input("Четвертое число="))
except:
     print("Только число!")
     exit()
if (a>5) and (b>5) and (c%6==0) and (d % 3!= 0) :
     print("yes")
else:
     print("no")
