
## Define Variables

#Calculates the amount paid towards the principal of the loan, this is the formula paying the principal on the loan after interest bruh bruh.
def principal_payment(price, down_payment, interest, loan_term, x):
    r = interest / 1200.0
    N = loan_term * 12.0
    P = price - down_payment
    payment = np.ppmt(r, x, N, P)
    return payment * (-1)

#Calculates the current monthly expenses   
def expenses(price, taxes, insurance, maintenance, management, growth, vacancy, rent, x):



#Calculates the .....

def mortgage():
    return int(pp) - int(dp)



pp = input("Enter Purchase Price\n")

dp = input("Enter Down Payment\n")

hoa = input("Enter Hoa\n")

print(" Your mortgage is:" + mortgage())

input()

## Output Code



Display = """
principal_payment: {}
Income:	"""+ Monthly_Rent + """	
Mortgage Pay:	{}
Property Tax:	{}
Total Insurance:	{}	
Maintenance Cost:	{}	
Other Cost:	{}	
Cash Flow:	{}	
"""

print('******************************************************************************************')
print('Welcome to Rental Property Calculator')
print(Display)
input()
