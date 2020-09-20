
import wx
import Menu_GUI


## Changes to Discuss
# 1. Using Rounding Floats to get simple answers ( example 3.083212  --->  3.01)
# 2. Let use a static input when testing code so we're working with the same numbers 
## Ex:   loan amount = 10,000 , rate = 4 , years = 30  , hoa = 100

## Using this online calculator to compare our output - https://www.bankrate.com/calculators/managing-debt/annual-percentage-rate-calculator.aspx


#This program will compute the payment amount for the loan, along with the total cost of borrowing.
#User will supply the amount borrowed, interest, rate and duration.

def display_num():

    print("Test Output for GUI")
    #print("The payment amount will be $", round(payment_amt, 2), "per month.")  #This is using the rounding function to display number
    #print("The total cost of borrowing will be $", round(total_int, 2), ".") #This is using the rounding function to display number
    #print("The total cost spent from borrowing will be $", round(total_cost, 2), ".") #This is using the rounding function to display number
    #print("Additional expense per month after HOA fee", round(hoa_new, 2), ".") #This is using the rounding function to display number

## Class code for GUI
class MainFrame(Menu_GUI.MyFrame1):
    def __init__(self,parent): 
        Menu_GUI.MyFrame1.__init__(self,parent)

    def Process_numb(self, event):
        frame2.Show(True)
        self.m_textCtrl5.SetValue(display_num())
        

class MainFrame2(Menu_GUI.MyFrame2):
    
    def __init__(self,parent): 
        Menu_GUI.MyFrame2.__init__(self,parent)
    
    def disp( self, event ):
        pass



# Starts the GUI Window        
app = wx.App(False) 
frame1 = MainFrame(None)  
frame1.Show(True)
frame2 = MainFrame2(None)

app.MainLoop() 

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
total_cost = num_payments * payment_amt

#Compute the total Interest of borrowing
total_int = num_payments * payment_amt - loan_amt

#Computing additional expense after HOA fee
hoa_new = payment_amt + hoa #need to work on this 

#Display the results
#print("The payment amount will be $", payment_amt, "per month.")  #works good!
#print("The total cost of borrowing will be $", total_cost, ".") # works good! - in other words, this is the interest in Dollars owed on top of the original loan
#print("Additional expense per month after HOA fee", hoa_new, ".") # Adjusted this since I understand it to be the monthly payments ( including interest) + the monthly HOA fee

#display_num()
