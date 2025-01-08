"""
Exports the Card class and the enums CardTypes, CardRankTypes, CardSuitTypes
"""

from enum import Enum


class CardTypes(Enum):
    """
    Enum for the possible card types of a playing card, with the possible values being
    - STANDARD: for the standard playing cards with ranks and of specific suits
    - JOKER: for the joker card
    - GUARANTEE: for the guarantee card
    """
    STANDARD = "standard"
    JOKER = "joker"
    GUARANTEE = "guarantee"


class CardSuitTypes(Enum):
    """
    Enum for the possible suit types of a standard playing card, with the possible values being
    - HEART
    - CLUB
    - SPADE
    - DIAMOND
    """
    HEART = "heart"
    CLUB = "club"
    SPADE = "spade"
    DIAMOND = "diamond"


class CardRankTypes(Enum):
    """
    This represents the rank of a standard playing card, we're representing it as a number.\n
    That is because, it is easier to deal with in the cases where we're deciding the pits.\n
    Note: ACE is set to be 1, since we all like counting from 1, don't we? :)\n
    Therefore, we go from ACE = 1, TWO = 2, ..., KING = 13
    """
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card: # pylint: disable=too-few-public-methods
    """
    This class represents a single playing card, also includes joker and guarantee cards
    """
    card_type: str = None # "standard", "joker" or "guarantee"
    suit: str = None # "heart", "club", "spade", "diamond"
    rank: str = None # "ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"

    ALLOWED_CARD_TYPES = [
        CardTypes.GUARANTEE,
        CardTypes.JOKER,
        CardTypes.STANDARD
    ]
    ALLOWED_SUIT_TYPES = [
        CardSuitTypes.CLUB,
        CardSuitTypes.DIAMOND,
        CardSuitTypes.HEART,
        CardSuitTypes.SPADE
    ]
    ALLOWED_RANK_TYPES = [
        CardRankTypes.ACE,
        CardRankTypes.TWO,
        CardRankTypes.THREE,
        CardRankTypes.FOUR,
        CardRankTypes.FIVE,
        CardRankTypes.SIX,
        CardRankTypes.SEVEN,
        CardRankTypes.EIGHT,
        CardRankTypes.NINE,
        CardRankTypes.TEN,
        CardRankTypes.JACK,
        CardRankTypes.QUEEN,
        CardRankTypes.KING
    ]


    def __init__(self, suit: str = None, rank: int = None, card_type: str = CardTypes.STANDARD):
        self.card_type = card_type
        self.suit = suit
        self.rank = rank


    @property
    def card_type(self):
        """
        The type of playing card we're considering:
        - standard: are the regular playing cards going from 2 to Ace and is of suits
        hearts, clubs, diamonds and spades
        - joker: the joker card (there's only one kind of joker in literature)
        - guarantee: the guarantee card
        """
        return self._card_type


    @card_type.setter
    def card_type(self, val):
        """
        If a card is a standard playing card and is converted to joker/guarantee,
        we simply delete the values of self.suit and self.rank, as a blank standard playing card,
        needs to be a state for us to set suit and rank of the playing card
        """
        if val not in self.ALLOWED_CARD_TYPES:
            raise ValueError(f"Invalid card type: {val}. Allowed card types are: {self.ALLOWED_CARD_TYPES}") # pylint: disable=line-too-long

        self._card_type = val
        if val != CardTypes.STANDARD:
            self._rank = None
            self._suit = None


    @property
    def suit(self):
        """
        The suit of the playing card. None if self.card_type != CardTypes.STANDARD
        else is of one of the types CardSuitTypes
        """
        return self._suit


    @suit.setter
    def suit(self, val):
        if self.card_type == CardTypes.STANDARD and val is None:
            raise ValueError(f"Invalid suit type, if card type is {CardTypes.STANDARD} then the suit type needs to be {self.ALLOWED_SUIT_TYPES}") # pylint: disable=line-too-long
        if self.card_type != CardTypes.STANDARD and val is not None:
            raise ValueError(f"Invalid suit type: {val} for card type: {self.card_type}, suit type needs to be None for a non-standard card") # pylint: disable=line-too-long
        if val not in self.ALLOWED_SUIT_TYPES:
            raise ValueError(f"Invalid suit type: {val}. Allowed suit types are: {self.ALLOWED_SUIT_TYPES}") # pylint: disable=line-too-long

        self._suit = val


    @property
    def rank(self):
        """
        The rank of the playing card. None if self.card_type != CardTypes.STANDARD
        else is of one of the types CardRankTypes
        """
        return self._rank


    @rank.setter
    def rank(self, val):
        if self.card_type == CardTypes.STANDARD and val is None:
            raise ValueError(f"""Invalid rank type, if card type is {CardTypes.STANDARD} then the rank type needs to be"{self.ALLOWED_RANK_TYPES}""") # pylint: disable=line-too-long
        if self.card_type != CardTypes.STANDARD and val is not None:
            raise ValueError(f"Invalid rank type: {val} for card type: {self.card_type}, rank type needs to be None for a non-standard card") # pylint: disable=line-too-long
        if val not in self.ALLOWED_RANK_TYPES:
            raise ValueError(f"Invalid rank type: {val}. Allowed rank types are: {self.ALLOWED_RANK_TYPES}") # pylint: disable=line-too-long

        self._rank = val


    def __str__(self):
        if self.card_type == CardTypes.STANDARD:
            # Dealing with blank standard cards
            if self.rank is None or self.suit is None:
                raise ValueError(f"Suit or Rank fields cannot be empty. The rank of the card is {self.rank} and suit of the card is {self.suit}") # pylint: disable=line-too-long

            return f"{self.rank.name} of {self.suit.value}"

        return f"{self.card_type.value}"
