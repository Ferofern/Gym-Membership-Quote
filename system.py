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


