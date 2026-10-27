"""Gym membership quote calculator."""

from decimal import Decimal

PLANS = {
    "BASIC": Decimal("30"),
    "STANDARD": Decimal("45"),
    "PREMIUM": Decimal("70"),
}

EXTRAS = {
    "GROUP_CLASSES": Decimal("15"),
    "PERSONAL_TRAINING": Decimal("25"),
    "SPA": Decimal("30"),
    "SPECIALIZED_PROGRAM": Decimal("40"),
}

PREMIUM_EXTRAS = {
    "SPA",
    "SPECIALIZED_PROGRAM",
}


class GymMembership:
    """Calculate gym membership quotes."""

    #DEVELOPER 1
    # R1. The user chooses one plan from the table. Any other plan is invalid.
    


    # DEVELOPER 2

    # R4 - Group discount. With 2 or more members, the subtotal gets a 10% discount.
    def calculate_member_discount(self, subtotal, members):
        """Calculate the 10% discount for two or more members."""
        if members >= 2:
            return subtotal * Decimal("0.10")

        return Decimal("0")

    # R5 - Special offer. Applied to the amount after R4.
    def calculate_threshold_discount(self, amount):
        """Calculate the threshold discount."""

        if amount > Decimal("400"):
            return Decimal("50")

        if amount > Decimal("200"):
            return Decimal("20")

        return Decimal("0")


    # R6 - Recargo por extra Premium
    def calculate_premium_surcharge(self, amount, extras):
        """Calculate the 15% surcharge for premium extras."""

        if any(extra in PREMIUM_EXTRAS for extra in extras):
            return amount * Decimal("0.15")

        return Decimal("0")
