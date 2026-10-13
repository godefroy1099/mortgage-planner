from .mortgage import (
    calculate_monthly_payment,
    calculate_total_interest,
    calculate_new_payment,
    calculate_new_duration,
    calculate_investment_value,
)

capital = 276_000
interest_rate = 3.35
years = 30

monthly_payment = calculate_monthly_payment(
    capital,
    interest_rate,
    years,
)

print("MORTGAGE - SIMULATION")
print("-------------------")
print(f"Principal: {capital:,.2f} euros")
print(f"Annual interest rate: {interest_rate:.2f}%")
print(f"Term: {years} years")
print(f"Monthly payment: {monthly_payment:,.2f} euros")

total_payments = monthly_payment * years * 12

total_interest = calculate_total_interest(
    capital,
    interest_rate,
    years,
)

print(f"Total payments: {total_payments:,.2f} euros")
print(f"Total interest: {total_interest:,.2f} euros")


available_capital = 20_000

new_payment = calculate_new_payment(
    capital,
    interest_rate,
    years,
    available_capital,
)

print()
print("EARLY REPAYMENT SIMULATION")
print("--------------------------------")
print(f"Available capital: {available_capital:,.2f} euros")
print(f"New monthly payment: {new_payment:,.2f} euros")
print(f"Monthly payment reduction: {monthly_payment - new_payment:,.2f} euros")


new_duration_months = calculate_new_duration(
    capital,
    interest_rate,
    years,
    available_capital,
)

print()
print("LOAN TERM REDUCTION SIMULATION")
print("----------------------------")
print(f"New term: {new_duration_months} months")
print(f"Original term: {years * 12} months")
print(f"Months saved: {years * 12 - new_duration_months}")
print(f"Years saved: {(years * 12 - new_duration_months) / 12:.1f}")


annual_return = 4.0

investment_value = calculate_investment_value(
    available_capital,
    annual_return,
    years,
)

print()
print("INVESTMENT SIMULATION")
print("------------------------")
print(f"Initial capital: {available_capital:,.2f} euros")
print(f"Assumed annual return: {annual_return:.2f}%")
print(f"Final value: {investment_value:,.2f} euros")
print(f"Gross gain: {investment_value - available_capital:,.2f} euros")
