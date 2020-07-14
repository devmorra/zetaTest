tray = ["vanilla cupcake", "chocolate cupcake", "chocolate cupcake", "vanilla cupcake"]
for cupcake in tray:
  if(cupcake == "vanilla cupcake"):
    cupcake+= " with vanilla frosting"
  elif(cupcake == "chocolate cupcake"):
    cupcake += " with chocolate frosting"
print(tray)

#Alternatively...
tray2 = ["vanilla cupcake", "chocolate cupcake", "chocolate cupcake", "vanilla cupcake"]
for i in range(len(tray2)):
  if(tray2[i]== "vanilla cupcake"):
    cupcake+= " with vanilla frosting"
  elif(tray2[i]== "chocolate cupcake"):
    cupcake+= " with chocolate frosting"
  print(i)
print(tray2)
