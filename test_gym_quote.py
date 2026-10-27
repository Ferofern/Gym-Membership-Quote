"""Tests for the gym membership quote calculator."""

from decimal import Decimal

from gym_quote import GymMembership


gym = GymMembership()




# DEVELOPER 2
# R4 - Tests members discounts
def test_member_discount():
    """R4: two or more members receive a 10% discount."""
    discount = gym.calculate_member_discount(
        Decimal("100"),
        2,
    )

    assert discount == Decimal("15")


def test_member_discount_for_more_members():
    """R4: three or more members also receive the discount."""
    discount = gym.calculate_member_discount(
        Decimal("200"),
        3,
    )

    assert discount == Decimal("20")


def test_no_member_discount_for_one_member():
    """R4: one member does not receive the discount."""
    discount = gym.calculate_member_discount(
        Decimal("100"),
        1,
    )
    assert discount == Decimal("0")


# DEVELOPER 2
# R5 - Tests: threshold discount
def test_no_threshold_discount():
    """R5: amounts up to 200 receive no threshold discount."""
    assert gym.calculate_threshold_discount(
        Decimal("200"),
    ) == Decimal("0")


def test_twenty_dollar_threshold_discount():
    """R5: amounts above 200 receive a 20 dollar discount."""
    assert gym.calculate_threshold_discount(
        Decimal("250"),
    ) == Decimal("20")


def test_fifty_dollar_threshold_discount():
    """R5: amounts above 400 receive a 50 dollar discount."""
    assert gym.calculate_threshold_discount(
        Decimal("450"),
    ) == Decimal("50")


def test_only_one_threshold_discount():
    """R5: the 20 and 50 dollar discounts are not cumulative."""
    assert gym.calculate_threshold_discount(
        Decimal("450"),
    ) == Decimal("50")


# DEVELOPER 2
# R6 - Tests premium surcharge

def test_premium_surcharge():
    """R6: premium extras add a 15% surcharge."""
    surcharge = gym.calculate_premium_surcharge(
        Decimal("300"),
        ["SPA"],
    )

    assert surcharge == Decimal("45")


def test_specialized_program_surcharge():
    """R6: specialized program also triggers the surcharge."""
    surcharge = gym.calculate_premium_surcharge(
        Decimal("300"),
        ["SPECIALIZED_PROGRAM"],
    )

    assert surcharge == Decimal("45")


def test_no_premium_surcharge():
    """R6: non-premium extras do not add a surcharge."""
    surcharge = gym.calculate_premium_surcharge(
        Decimal("300"),
        ["GROUP_CLASSES"],
    )

    assert surcharge == Decimal("0")
