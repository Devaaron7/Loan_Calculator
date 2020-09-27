## Changes to Discuss
# 1. Using Rounding Floats to get simple answers ( example 3.083212  --->  3.01)
# 2. Let use a static input when testing code so we're working with the same numbers 
## Ex:   loan amount = 10,000 , rate = 4 , years = 30  , hoa = 100

## Using this online calculator to compare our coutput - https://www.bankrate.com/calculators/managing-debt/annual-percentage-rate-calculator.aspx

<<<<<<< Updated upstream

#This program will compute the payment amount for the loan, along with the total cost of borrowing.
#User will supply the amount borrowed, interest, rate and duration.
=======
#Calculates the amount paid towards the principal of the loan, this is the formula paying the principal on the loan after interest bruh bruh.
'''
def principal_payment(price, down_payment, interest, loan_term, x):
    r = interest / 1200.0
    N = loan_term * 12.0
    P = price - down_payment
    payment = np.ppmt(r, x, N, P)
    return payment * (-1)
'''
#Calculates the current monthly expenses   
def expenses(price, taxes, insurance, maintenance, management, growth, vacancy, rent, x):
>>>>>>> Stashed changes

#Reads the amount borrowed, interest rate and loan duration from the user

<<<<<<< Updated upstream
loan_amt = float(input("Enter the Loan Amount: "))
rate = float(input("Enter the annual interest rate percentage EX: 3.25 for 3.25%: "))
years = int(input("How many years will take to repay the loan? "))
hoa = float(input("Enter the HOA fee per month: "))

=======
#Calculates the .....
>>>>>>> Stashed changes

#Compute the interest rate per payment period and the number of payments
period_rate = rate / 12 / 100  #rate / 12 payments per year
num_payments = years * 12


#Compute the payment amount
payment_amt = period_rate * loan_amt / (1-(1 + period_rate) ** - num_payments) # ** is exponential operator

#Compute the total cost of borrowing
total_cost = num_payments * payment_amt - loan_amt

#Computing additional expense after HOA fee
hoa_new = payment_amt + hoa #need to work on this 


#Display the results
#print("The payment amount will be $", payment_amt, "per month.")  #works good!
#print("The total cost of borrowing will be $", total_cost, ".") # works good! - in other words, this is the interest in Dollars owed on top of the original loan
#print("Additional expense per month after HOA fee", hoa_new, ".") # Adjusted this since I understand it to be the monthly payments ( including interest) + the monthly HOA fee

<<<<<<< Updated upstream
print("The payment amount will be $", round(payment_amt, 2), "per month.")  #This is using the rounding function to display number
print("The total cost of borrowing will be $", round(total_cost, 2), ".") #This is using the rounding function to display number
print("Additional expense per month after HOA fee", round(hoa_new, 2), ".") #This is using the rounding function to display number
=======
input()

## Output Code


'''
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
'''
print('******************************************************************************************')
print('Welcome to Rental Property Calculator')
print(Display)
input()
>>>>>>> Stashed changes
