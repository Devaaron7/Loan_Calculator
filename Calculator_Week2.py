#This program will compute the payment amount for the loan, along with the total cost of borrowing.
#User will supply the amount borrowed, interest, rate and duration.

#Reads the amount borrowed, interest rate and loan duration from the user

loan_amt = float(input("Enter the Loan Amount: "))
rate = float(input("Enter the annual interest rate percentage EX: 3.25 for 3.25%: "))
years = int(input("How many years will take to repay the loan? "))
hoa = float(input("Enter the HOA fee per month: "))


#Compute the interest rate per payment period and the number of payments
period_rate = rate / 12 / 100  #rate / 12 payments per year
num_payments = years * 12

#Compute the payment amount
payment_amt = period_rate * loan_amt / (1-(1 + period_rate) ** - num_payments) # ** is exponential operator

#Compute the total cost of borrowing
total_cost = num_payments * payment_amt - loan_amt

#Computing additional expense after HOA fee
hoa = num_payments + payment_amt #need to work on this 


#Display the results
print(" The payment amount will be $", payment_amt, "per month.")
print("The total cost of borrowing will be $", total_cost, ".")
print("Additional expense per month after HOA fee", payment_amt + hoa, ".") # this is wrong it should be 621

#principal_payment: {}
#Income:	"""+ Monthly_Rent + """
#Mortgage Pay:	{}
#Property Tax:	{}
#Total Insurance:	{}
#Maintenance Cost:	{}
#Other Cost:	{}
#Cash Flow:	{}

