# Texas Hold'em is a Poker variant in which each player is given two "hole cards".
# Players then proceed to make a series of bets while five "community cards" are dealt.
# If there are more than one player remaining when the betting stops, a showdown takes
# place in which players reveal their cards. Each player makes the best poker hand
# possible using five of the seven available cards (community cards + the player's hole cards).
#
# Possible hands are, in descending order of value:
#
# Straight-flush (five consecutive ranks of the same suit). Higher rank is better.
# Four-of-a-kind (four cards with the same rank). Tiebreaker is first the rank, then the rank of the remaining card.
# Full house (three cards with the same rank, two with another). Tiebreaker is first the rank of the three cards,
# then rank of the pair.
# Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.
# Straight (five consecutive ranks). Higher rank is better.
# Three-of-a-kind (three cards of the same rank). Tiebreaker is first the rank of the three cards,
# then the highest other rank, then the second highest other rank.
# Two pair (two cards of the same rank, two cards of another rank). Tiebreaker is first the rank of the high pair,
# then the rank of the low pair and then the rank of the remaining card.
# Pair (two cards of the same rank). Tiebreaker is first the rank of the two cards, then the three other ranks.
# Nothing. Tiebreaker is the rank of the cards from high to low.
#
# Given hole cards and community cards, complete the function hand to return the type of hand (as written above,
# you can ignore case) and a list of ranks in decreasing order of significance, to use for comparison against other
# hands of the same type, of the best possible hand.
def straight_flush_check(pool):
    cards_rank = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    d_cards_rank = {y: x for x, y in zip([x for x in range(14, 0, -1)], cards_rank)}
    suits = [x[2] for x in pool]
    flush_suit = [pool[x[0]] for x in enumerate(suits) if suits.count(x[1]) >= 5]
    ranks = [x[0] for x in flush_suit]
    ans = [d_cards_rank[x[1]] - d_cards_rank[ranks[x[0] + 1]] == 1 for x in enumerate(ranks[:-1])]
    i = 0
    c = 0
    while i < len(ans):
        if ans[i]:
            c += 1
            if c == 4:
                break
        else:
            c = 0
        i += 1

    return ("straight-flush", ranks[i - 3: i + 2]) if c == 4 else False


def four_of_a_kind_check(pool):
    ranks, cards_num = [x[0] for x in pool], []
    count_ = [cards_num.append(ranks.count(x)) for x in ranks]
    if max(cards_num) == 4:
        if cards_num.index(4) == 0:
            return "four-of-a-kind", [ranks[0], ranks[4]]
        else:
            return "four-of-a-kind", [ranks[cards_num.index(4)], ranks[0]]
    return False


def full_house_check(pool):
    ranks, cards_num = [x[0] for x in pool], []
    count_ = [cards_num.append(ranks.count(x)) for x in ranks]
    three_of_a_kind, pair = 0, []
    for x in cards_num:
        if x == 3:
            three_of_a_kind = ranks[cards_num.index(3)]
        elif x == 2:
            pair.append(ranks[cards_num.index(2)])
            pair.append(ranks[::-1][cards_num[::-1].index(2)])
    if three_of_a_kind and pair:
        return 'full house', [three_of_a_kind, pair[0]]
    return False


def flush_check(pool):
    suits = [x[2] for x in pool]
    flush_suit = [pool[x[0]] for x in enumerate(suits) if suits.count(x[1]) >= 5]
    ranks = [x[0] for x in flush_suit[:5]]
    return ("flush", ranks) if ranks else False


def straight_check(pool):
    i, c, seq = 0, 1, set()
    while i < len(pool) - 1:
        if c == 5:
            break
        else:
            if pool[i][1] - 1 == pool[i + 1][1]:
                add_ = [seq.add(x) for x in [pool[i], pool[i + 1]]]
                c += 1
            else:
                if pool[i][1] == pool[i + 1][1]:
                    seq.discard(pool[i])
                else:
                    seq = set()
                    c = 1
            i += 1
    ranks = [x[0] for x in sorted(seq, key=lambda x:  x[1], reverse=True)]
    return ("straight", ranks) if len(ranks) == 5 else False


def three_of_a_kind_check(pool):
    ranks, cards_num = [x[0] for x in pool], []
    count_ = [cards_num.append(ranks.count(x)) for x in ranks]
    if max(cards_num) == 3:
        if cards_num.index(3) == 0:
            return "three-of-a-kind", [ranks[0], ranks[3], ranks[4]]
        elif cards_num.index(3) == 1:
            return "three-of-a-kind", [ranks[1], ranks[0], ranks[4]]
        else:
            return "three-of-a-kind", [ranks[cards_num.index(3)], ranks[0], ranks[1]]
    return False


def two_pair_check(pool):
    ranks, cards_num = [x[0] for x in pool], []
    count_ = [cards_num.append(ranks.count(x)) for x in ranks]
    if max(cards_num) == 2 and cards_num.count(2) == 4:
        first_pair = ranks[cards_num.index(2)]
        second_pair = ranks[len(cards_num) - 2 - cards_num[::-1].index(2)]
        remove_ = [ranks.remove(x) for x in [first_pair, first_pair, second_pair, second_pair]]
        return "two pair", [first_pair, second_pair, ranks[0]]
    return False


def pair_check(pool):
    ranks, cards_num = [x[0] for x in pool], []
    count_ = [cards_num.append(ranks.count(x)) for x in ranks]
    if max(cards_num) == 2 and cards_num.count(2) == 2:
        first_pair = ranks[cards_num.index(2)]
        remove_ = [ranks.remove(x) for x in [first_pair, first_pair]]
        return "pair", [first_pair, ranks[0], ranks[1], ranks[2]]
    return False


def hand(hole_cards, community_cards):
    cards_rank = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    d_cards_rank = {y: x for x, y in zip([x for x in range(14, 0, -1)], cards_rank)}

    united_hand = hole_cards + community_cards
    united_hand_s = []
    for card in united_hand:
        card_suit, *card_rank = card[::-1]
        card_rank = '{1}{0}'.format(str(card_rank[0]), str(card_rank[1])) if len(card_rank) > 1 else card_rank[0]
        united_hand_s.append((card_rank, d_cards_rank[card_rank], card_suit))
    united_hand_s.sort(key=lambda x: d_cards_rank[x[0]], reverse=True)
    ranks = [x[0] for x in united_hand_s]

    if straight_flush_check(united_hand_s):
        return straight_flush_check(united_hand_s)
    elif four_of_a_kind_check(united_hand_s):
        return four_of_a_kind_check(united_hand_s)
    elif full_house_check(united_hand_s):
        return full_house_check(united_hand_s)
    elif flush_check(united_hand_s):
        return flush_check(united_hand_s)
    elif straight_check(united_hand_s):
        return straight_check(united_hand_s)
    elif three_of_a_kind_check(united_hand_s):
        return three_of_a_kind_check(united_hand_s)
    elif two_pair_check(united_hand_s):
        return two_pair_check(united_hand_s)
    elif pair_check(united_hand_s):
        return pair_check(united_hand_s)
    else:
        return "nothing", ranks[:5]


# suit = ['♠', '♦', '♣', '♥']
#
# straight_flush = ['A♠', 'K♠', 'Q♠', 'J♠', '10♠']
# four_of_a_kind = ['A♠', 'A♦', 'A♣', 'A♥']
# full_house = ['A♠', 'A♦', 'A♣', 'K♥', 'K♣']
# flush = ['5♠', '8♠', 'Q♠', 'J♠', '10♠']
# straight = ['A♠', 'K♦', 'Q♠', 'J♦', '10♥']
# three_of_a_kind = ['A♠', 'A♦', 'A♣']
# two_pair = ['A♠', 'A♦', 'K♥', 'K♣']
# pair = ['K♥', 'K♣']
# nothing = []

# print(hand(["6♠", "2♦"], ["3♣", "8♥", "9♥", "7♥", "10♦"]))
print(hand(["A♦", "10♦"], ['Q♦', '3♦', '8♦', '9♦', 'J♦']))
er = [('10', 10, '♣'), ('10', 10, '♠'), ('9', 9, '♦'), ('8', 8, '♦'), ('7', 7, '♦'), ('6', 6, '♦'), ('5', 5, '♦')]

########################################################################################################################
########################################################################################################################
# best practice
########################################################################################################################
########################################################################################################################
#
# class Poker:
#     value_map = {r: v for r, v in zip('2 3 4 5 6 7 8 9 10 J Q K A'.split(), range(2, 15))}
#
#     class Card:
#         def __init__(self, card):
#             self.rank = card[:-1]
#             self.value = Poker.value_map[self.rank]
#             self.suit = card[-1]
#
#         def __hash__(self):
#             return hash(self.rank)
#
#     def __init__(self, cards):
#         self.cards = sorted((Poker.Card(c) for c in cards), key=lambda x: x.value, reverse=True)
#         self.rank_count = {r: 0 for r in 'A K Q J 10 9 8 7 6 5 4 3 2'.split()}
#         self.suit_count = {s: 0 for s in '♠♦♣♥'}
#         for card in self.cards:
#             self.rank_count[card.rank] += 1
#             self.suit_count[card.suit] += 1
#
#     def best_hand(self):
#         if hand := self.four_of_a_kind():
#             return ("four-of-a-kind", hand)
#         elif hand := self.full_house():
#             return ("full house", hand)
#         elif flush := self.flush():
#             if straight := self.straight(flush):
#                 return ("straight-flush", straight)
#             return ("flush", [c.rank for c in flush[:5]])
#         elif straight := self.straight(self.cards):
#             return ("straight", straight)
#         elif hand := self.three_of_a_kind():
#             return ("three-of-a-kind", hand)
#         elif r1 := self.pair():
#             if r2 := self.pair(r1[0]):
#                 return ("two pair", [r1[0]] + r2)
#             return ("pair", r1)
#         else:
#             return ("nothing", [c.rank for c in self.cards[:5]])
#
#     def four_of_a_kind(self):
#         for rank, count in self.rank_count.items():
#             if count == 4:
#                 tie = [c.rank for c in self.cards if c.rank != rank][0]
#                 return [rank, tie]
#         return []
#
#     def full_house(self):
#         if three := self.three_of_a_kind():
#             r3 = three[0]
#             if two := self.pair(r3):
#                 r2 = two[0]
#                 return [r3, r2]
#         return []
#
#     def flush(self):
#         for suit, count in self.suit_count.items():
#             if count >= 5:
#                 return [card for card in self.cards if card.suit == suit]
#         return []
#
#     def straight(self, cards):
#         cards = sorted(set(c.rank for c in cards), key=lambda x: self.value_map[x], reverse=True)
#         for i in range(len(cards) - 4):
#             run = cards[i:i + 5]
#             if all(self.value_map[a] - self.value_map[b] == 1 for a, b in zip(run, run[1:])):
#                 return run
#         return []
#
#     def three_of_a_kind(self):
#         for rank, count in self.rank_count.items():
#             if count == 3:
#                 tie = [c.rank for c in self.cards if c.rank != rank][:2]
#                 return [rank] + tie
#         return []
#
#     def pair(self, exclude=None):
#         for rank, count in self.rank_count.items():
#             if count == 2:
#                 if exclude is not None:
#                     if rank != exclude:
#                         tie = [c.rank for c in self.cards if c.rank not in [rank, exclude]][0]
#                         return [rank, tie]
#                 else:
#                     tie = [c.rank for c in self.cards if c.rank != rank][:3]
#                     return [rank] + tie
#         return []
#
#
# def hand(hole_cards, community_cards):
#     poker = Poker(hole_cards + community_cards)
#     return poker.best_hand()
