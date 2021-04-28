x=int(input("Вага Богдана: "))
y=int(input("Вага Наталки: "))
z=int(input("Вага Олесі: "))

if x>y:
    max=x
    max_name="Богдан"
else:
    max=y
    max_name="Наталка"
  
if z>max:
    max=z
    max_name="Олеся"
  
print("Більше важить",max_name,"(",max,"кг.)")
