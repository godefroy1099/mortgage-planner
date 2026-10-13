import pytest

from mortgage_planner.mortgage import (
    calculate_monthly_payment,
    calculate_total_interest,
    calculate_new_payment,
    calculate_new_duration,
    calculate_investment_value,
)


def test_monthly_payment():
    payment = calculate_monthly_payment(150_000, 3.5, 20)
    assert payment == pytest.approx(869.94, abs=0.02)


def test_total_interest():
    interest = calculate_total_interest(150_000, 3.5, 20)
    assert interest > 0


def test_new_payment_is_lower():
    original = calculate_monthly_payment(150_000, 3.5, 20)
    new = calculate_new_payment(150_000, 3.5, 20, 20_000)
    assert new < original


def test_new_duration_is_shorter():
    months = calculate_new_duration(150_000, 3.5, 20, 20_000)
    assert months < 240


def test_investment_growth():
    value = calculate_investment_value(20_000, 4, 15)
    assert value == pytest.approx(36_018.87, abs=0.02)


def test_invalid_capital():
    with pytest.raises(ValueError):
        calculate_monthly_payment(0, 3.5, 20)
