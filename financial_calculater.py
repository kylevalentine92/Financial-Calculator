#-------------------------------------------------------------------------------
# Name:        financial_calculater
# Purpose:     capstone task 12
#
# Author:      Kyle Valentine
#
# Created:     11/04/2020
# Copyright:   (c) Kyle Valentine
#-------------------------------------------------------------------------------
#Importing needed libraries
import math

#Initialize all the variables i will be working with.
cal_select=input("Please enter which calculation you would like <Investment/Bond>?")
#If investment is selected request principle amount,interest rate,number of years and interest type(simple or compound)
#Total investment will be displayed
principle_amt=0
interest_rate=0
num_year=0
interest=""
total_invest=0
#If bond is selected request present value,interest rate,total months to repay
#Total bond will be displayed
present_value=0
bond_month=0
total_bond=0

#Validate the users input on which calculation they selected.

if (cal_select.lower()=="bond"):

    print("You have selected the bond calculation.")
    present_value=float(input("Please enter the present value of the bond?"))
    interest_rate=float(input("Please enter the interest rate of the bond?"))
    bond_month=int(input("Please enter the number of months you would take to repay the bond?"))
    total_bond=(interest_rate/12*present_value)/(1-math.pow((1+interest_rate/12),bond_month*-1))
    print(f"The total monthly bond repayments are {total_bond:.2f}")

elif (cal_select.lower()=="investment"):

    print("You have selected the investment calculation.")
    principle_amt=float(input("Please enter the initial amount you would like to deposit?"))
    interest_rate=float(input("Please enter the interest rate that you would like to invest at (as percentage without %)?"))
    num_year=float(input("Please enter the number of years you would like to invest for?"))
    interest=input("Please enter whether you want simple of compound interest?")

    if (interest.lower()=="simple"):

        total_invest=principle_amt*(1+(interest_rate/100*num_year))
        print(f"Your total investment if you choose simple interest is {total_invest:.2f}")

    elif (interest.lower()=="compound"):

        total_invest=principle_amt*math.pow((1+(interest_rate/100)),num_year)
        print(f"Your total investment if you choose compound interest is {total_invest:.2f}")

    else:

        print("You have not entered a valid type of interest.")

else:

    print("Sorry you have not selected a valid calculation.")