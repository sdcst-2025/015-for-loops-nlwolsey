"""
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51

"""
bal = input("enter your current balance")
totalbal = 0
totalpay = 0
totalpurc = 0
for i in range(1,1200):
    newpurc = float(input(f"enter TOTAL purchases for month {i}: "))
    totalpurc = totalpurc + newpurc
    newpay = float(input(f"enter TOTAL credit payments for month {i}: "))
    totalpay = totalpay + newpay
    totalbal = totalbal + totalpurc - totalpay
    intrst = totalbal * 0.02
    print(f"2% interest has been charged: {intrst}")
    print(f"Your closing balance is {totalbal-intrst}")
else:
    print("you are 100 years old... stop worrying about your debt!")