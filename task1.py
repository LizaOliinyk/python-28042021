x=int(input("Вага Богдана: "))
y=int(input("Вага Наталки: "))

if x>y:
    max=x
    max_name="Богдан"
else:
    max=y
    max_name="Наталка"
  
print("Більше важить",max_name,"(",max,"кг.)")
