letter='''Dear |<NAME>|
You are selected!
|<DATE>|'''
print(letter)
name=str(input("Enter the Name"))
date=input("Enter date")
letter=letter.replace("|<NAME>|",name)
letter=letter.replace("|<DATE>|",date)
print(letter)