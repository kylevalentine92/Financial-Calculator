# CapStone Project 1

## The Financial Calculator

This python code simulates the use of the financial calculator. Currently as coded the financial calculator has two features. One to calculate simple and compound interest. The second is a bond calculator that determines the repayment of a bond after a specified amount of time.

## Who is this program for

This program is useful for beginner programmers learning to write and grasp python. The program consist of a plethora of different statements used in basic python, such as assigning variables, basic control structures and learning to think like a programmer. If you are interested in finances you will also gain basic knowledge of simple and compound interest.

## Basic financial forumalas used

The basic formula for compound and simple interest is as follows:

The total amount when simple interest is applied is calculated with the formula below:
**A = P ( 1 + r * t)**

Using python syntax to rewrite the above formula **A = P * math.pow( (1 + r), t).**

**In the formulas above:**
* 'r' is the interest rate.
* 't' is the number of years the money is invested for.
* 'P' is the principle amount deposited.
* 'A' is the total amount after the investment.

The bond repayment as said before calculates the amount that a person will have to pay back on their home loan each month.

### The formula for to calculate your monthly bond repayments:
**x = ( i.P ) / ( 1 - ( 1 + i ) ^( -n ) )**

**In the formula above:**
* 'P' is the Present Value.
* 'i' is the monthly interest rate on the home loan(which is calculated using the annual interest rate divided by 12).
* 'n' is the number of years the home loan is taken out for.
* 'x' is the monthly bond repayment.

## How to get the program to run

Firstly the program would request the user to which feature of the calculator you would like to use. The bond calculator or the interest calculator.

**If the bond calculator is selected the user will be reqested to enter the following:**
* The present value.
* The interest rate. 
* The number of months the bond needs to be paid for. 

The code will then output the monthly bond repayments.

**If the interest is selected the user will be rquested to enter the following:**

* The interest rate.
* Principle amount. 
* The amount of time they want to invest for. 
* They would also be requested to enter whether this is simple of compound interest.

The code will then calculate the total amount of the investment at the time entered.
