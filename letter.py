letter='''Dear <|NAME|>
You are selected!
<|DATE|>'''
<|NAME|>=str(input("Enter your name\n"))
<|DATE|>=str(input("Enter date\n"))
#letter=letter.replace("<|NAME|>",name)
#letter=letter.replace("<|DATE|>",date)
print(letter)