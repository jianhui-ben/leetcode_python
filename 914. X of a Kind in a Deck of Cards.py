# 914. X of a Kind in a Deck of Cards
# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
#
# Each group has exactly X cards.
# All the cards in each group have the same integer.

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        find if the common factor >= 2

        """
        stored = list(set([fre for _, fre in collections.Counter(deck).items()]))
        for k in range(2, min(stored) + 1):
            for i in stored:
                if i % k:
                    break
            else:
                return True
        return False
