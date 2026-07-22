loan = input("Enter the loan amount: ")
intrest_rate = input("Enter the interest rate: ")
number_of_years_for_loan = input("Enter the number of years for the loan: ")
monthly_payment = 0
number_of_payments = 0
number_of_payments = number_of_years_for_loan * 12
monthly_payment = (float(loan)) * (float(intrest_rate)) * (1 + float(intrest_rate)) * (float(number_of_payments)) / (1 + float(intrest_rate)) * (float(number_of_payments)-1)
print("Your monthly payment will be $%.2f" % monthly_payment) 