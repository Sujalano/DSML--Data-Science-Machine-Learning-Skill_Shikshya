from finance_tools import loan, tax

# Loan Calculation
p = 1000000
rate = 12
time = 5

monthly_payment = loan.calculate_emi(p, rate, time)
print(f"Your Monthly EMI is: {monthly_payment}")

# Tax Calculation
price = 50000
tax, total = tax.calculate_tax(price,tax_rate=13)

print(f"Base Price: Rs. {price}")
print(f"Tax (13%): Rs. {tax}")
print(f"Total to Pay: Rs. {total}")