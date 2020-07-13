tray = ["vanilla cupcake", "chocolate cupcake", "chocolate cupcake", "vanilla cupcake"]
for index, cupcake in enumerate(tray):
  print(cupcake,"is at index",index)
  if(cupcake == "vanilla cupcake"):
    tray[index] = "vanilla cupcake with vanilla frosting"
  elif(cupcake == "chocolate cupcake"):
    tray[index] = "chocolate cupcake with chocolate frosting"
print(tray)


