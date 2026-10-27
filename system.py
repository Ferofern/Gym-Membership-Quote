from abc import ABC, abstractmethod


class Plan(ABC):
    """Base plan: every plan has a name and a price per member."""

    @property
    @abstractmethod
    def name(self):
        """Plan name."""

    @property
    @abstractmethod
    def price(self):
        """Price per member."""


class Basic(Plan):
    """BASIC plan."""
    name = "BASIC"
    price = 30


class Standard(Plan):
    """STANDARD plan."""
    name = "STANDARD"
    price = 45


class Premium(Plan):
    """PREMIUM plan."""
    name = "PREMIUM"
    price = 70


class Extra(ABC):
    """Base extra: name, price per member and whether it is premium."""

    @property
    @abstractmethod
    def name(self):
        """Extra name."""

    @property
    @abstractmethod
    def price(self):
        """Price per member."""

    @property
    @abstractmethod
    def premium(self):
        """True if it is a premium extra."""


class GroupClasses(Extra):
    """GROUP_CLASSES extra."""
    name = "GROUP_CLASSES"
    price = 15
    premium = False


class PersonalTraining(Extra):
    """PERSONAL_TRAINING extra."""
    name = "PERSONAL_TRAINING"
    price = 25
    premium = False


class Spa(Extra):
    """SPA extra."""
    name = "SPA"
    price = 30
    premium = True


class SpecializedProgram(Extra):
    """SPECIALIZED_PROGRAM extra."""
    name = "SPECIALIZED_PROGRAM"
    price = 40
    premium = True


class User:
    """User: has a plan and a list of extras."""
    plan
    extras = []


def start():
    """Start the program. """
    plans = [Basic(), Standard(), Premium()]
    try:
        plan = input("Enter plan (BASIC, STANDARD, PREMIUM): ").upper()
        plan = next(p for p in plans if p.name == plan)
    except StopIteration:
        print("Invalid plan. Please try again.")
        return
    user = User()
    user.plan = plan
    extras = [GroupClasses(), PersonalTraining(), Spa(), SpecializedProgram()]
    question = input("Do you want to add extras? (yes/no): ").lower()
    if question == "yes":
        extra_names = input("Enter extras (comma-separated, e.g., GROUP_CLASSES, SPA): ").upper().split(",")
        for extra_name in extra_names:
            extra_name = extra_name.strip()
            try:
                extra = next(e for e in extras if e.name == extra_name)
                user.extras.append(extra)
            except StopIteration:
                print(f"Invalid extra: {extra_name}. Please try again.")
                return
    
    
