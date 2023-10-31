#Tips calculating
Bill=float(input("Enter the total bill \n"))
Tip=int(input("Enter how much tip do you want give 10 12 or 15?\n"))
People=int(input("How many people ?\n"))
total_bill_with_tip=((Bill*Tip)/100)+Bill
per_people=(total_bill_with_tip)/People
print(per_people)
