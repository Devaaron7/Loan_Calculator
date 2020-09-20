
import wx
import Menu_GUI


## Changes to Discuss
# 1. Using Rounding Floats to get simple answers ( example 3.083212  --->  3.01)
# 2. Let use a static input when testing code so we're working with the same numbers 
## Ex:   loan amount = 10,000 , rate = 4 , years = 30  , hoa = 100

## Using this online calculator to compare our output - https://www.bankrate.com/calculators/managing-debt/annual-percentage-rate-calculator.aspx




## Class code for GUI        

class MainFrame2(Menu_GUI.MyFrame2):
    
    def __init__(self,parent): 
        Menu_GUI.MyFrame2.__init__(self,parent)
    
    def disp( self, event ):
        pass


class MainFrame(Menu_GUI.MyFrame1):
    def __init__(self,parent): 
        Menu_GUI.MyFrame1.__init__(self,parent)

    def Process_numb(self, event):
        #Reads the amount borrowed, interest rate and loan duration from the user
        loan_amt = int(frame1.m_textCtrl1.GetValue())
        rate = int(frame1.m_textCtrl2.GetValue())
        years = int(frame1.m_textCtrl3.GetValue())
        hoa = int(frame1.m_textCtrl4.GetValue())
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

        def display_num():
            return """The payment amount will be ${} per month.\nThe total cost of borrowing will be ${}.\nThe total cost spent from borrowing will be ${}.\nAdditional expense per month after HOA fee is {}.""".format(round(payment_amt, 2), round(total_int, 2), round(total_cost, 2), round(hoa_new, 2))

        frame2.Show(True)
        #frame2.m_textCtrl5.SetValue (display_num())
        frame2.m_textCtrl5.SetValue (display_num())


#This program will compute the payment amount for the loan, along with the total cost of borrowing.
#User will supply the amount borrowed, interest, rate and duration.




# Starts the GUI Window        
app = wx.App(False) 
frame1 = MainFrame(None)  
frame1.Show(True)
frame2 = MainFrame2(None)
app.MainLoop() 
