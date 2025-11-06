""" 4. Calculate simple interest"""
""" SI = (Principle amount * time in years * rate of interest)/100"""

principle_amount = int(input("Enter the amount borrowed:"))
time_years =  int(input("Enter the time in years:"))
rate_of_interest =  int(input("Enter the rate of interest:"))

def calculate_interest(p, t, r):
    si =  (p * t * r)/100
    return si

print(calculate_interest(principle_amount, time_years, rate_of_interest))
