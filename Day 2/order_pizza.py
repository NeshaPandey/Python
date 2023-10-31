print("Welcome!")
size=input("Enter which pizza do you want to order'L','M','S'?")
extra_chilli=input("Do you want extra chilli 'Y','N'?")
extra_cheese=input("Do you want extra cheese 'Y','N'?")
if size=='L':
  bill=100
  if extra_chilli=='Y':
    bill+=1
  if extra_cheese=='Y':
    bill+=3

if size=='M':
  bill=90
  if extra_chilli=='Y':
    bill+=1
  if extra_cheese=='Y':
    bill+=2

if size=='S':
  bill=80
  if extra_chilli=='Y':
    bill+=1
  if extra_cheese=='Y':
    bill+=1
print(f"You total bill is {bill}")
   