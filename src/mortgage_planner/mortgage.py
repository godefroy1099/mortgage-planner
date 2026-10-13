import math


def calculate_monthly_payment(
    principal: float,
    annual_interest_rate: float,
    years: int,
) -> float:
    """Calculate the monthly payment of a fixed-rate amortizing mortgage."""

    if principal <= 0:
        raise ValueError("The principal must be greater than zero.")

    if annual_interest_rate < 0:
        raise ValueError("The interest rate cannot be negative.")

    if years <= 0:
        raise ValueError("The loan term must be greater than zero.")

    number_of_payments = years * 12
    monthly_rate = annual_interest_rate / 100 / 12

    if monthly_rate == 0:
        return principal / number_of_payments

    payment = (
        principal * monthly_rate / (1 - (1 + monthly_rate) ** (-number_of_payments))
    )

    return payment


def calculate_total_interest(
    principal: float,
    annual_interest_rate: float,
    years: int,
) -> float:
    """Calculate the total interest over the full mortgage term."""

    monthly_payment = calculate_monthly_payment(
        principal,
        annual_interest_rate,
        years,
    )

    total_payments = monthly_payment * years * 12
    total_interest = total_payments - principal

    return total_interest


def calculate_new_payment(
    principal: float,
    annual_interest_rate: float,
    years: int,
    available_capital: float,
) -> float:
    """Calculate the new monthly payment after a partial repayment."""

    if available_capital < 0:
        raise ValueError("The available capital cannot be negative.")

    if available_capital >= principal:
        raise ValueError("The available capital must be less than the principal.")

    remaining_principal = principal - available_capital

    return calculate_monthly_payment(
        remaining_principal,
        annual_interest_rate,
        years,
    )


def calculate_new_duration(
    principal: float,
    annual_interest_rate: float,
    years: int,
    available_capital: float,
) -> int:
    """Estimate the remaining months after partial repayment,
    keeping the original monthly payment.
    """

    if available_capital < 0 or available_capital >= principal:
        raise ValueError(
            "The early repayment must be at least zero and less than the principal."
        )

    original_payment = calculate_monthly_payment(
        principal,
        annual_interest_rate,
        years,
    )

    remaining_principal = principal - available_capital
    monthly_rate = annual_interest_rate / 100 / 12

    if monthly_rate == 0:
        return math.ceil(remaining_principal / original_payment)

    months = -math.log(
        1 - (remaining_principal * monthly_rate / original_payment)
    ) / math.log(1 + monthly_rate)

    return math.ceil(months)


def calculate_investment_value(
    initial_capital: float,
    annual_return_rate: float,
    years: int,
) -> float:
    """Estimate investment value with annual compound growth."""

    if initial_capital < 0:
        raise ValueError("The initial investment cannot be negative.")

    if annual_return_rate <= -100:
        raise ValueError("The annual return rate must be greater than -100%.")

    if years < 0:
        raise ValueError("The investment term cannot be negative.")

    final_value = initial_capital * (1 + annual_return_rate / 100) ** years

    return final_value
