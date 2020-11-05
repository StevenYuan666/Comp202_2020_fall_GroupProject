import math
from card import *
from collections import Counter
from itertools import combinations

def equal_occurrences(l1, l2):
    for x in l1:
        num = 0
        for y in l1:
            if x == y:
                num += 1
        num2 = 0
        for y in l2:
            if x == y:
                num2 += 1
        if num != num2:
            return False
    return True

def is_valid_arrangement(arrangement, hand, wildcard_rank):
    cards = []
    for seq in arrangement:
        if not is_valid_group(seq, wildcard_rank) and not is_valid_sequence(seq, wildcard_rank):
            return False
        
        cards.extend(seq)
    
    return equal_occurrences(hand, cards)

valid_groups = dict()
def is_valid_group(cards, wildcard_rank):
    """ (list<Card>, int) -> bool
    Checks if the given list of cards forms a valid group.
    A group is a set of three or more cards of the same rank.
    A wildcard (card of the given wildcard rank) can fit in any group.
    >>> is_valid_group([get_card(HEARTS, TWO), get_card(HEARTS, TWO), get_card(CLUBS, TWO)], KING)
    True
    >>> is_valid_group([get_card(HEARTS, FOUR), get_card(HEARTS, TWO), get_card(CLUBS, TWO)], KING)
    False
    >>> is_valid_group([get_card(HEARTS, TWO), get_card(CLUBS, TWO)], KING)
    False
    >>> is_valid_group([get_card(HEARTS, TWO), get_card(CLUBS, TWO), get_card(SPADES, KING)], KING)
    True
    """
    if len(cards) < 3:
        return False

    if (tuple(cards), wildcard_rank) not in valid_groups:
        group_rank = get_rank(cards[0])
        result = True
        for card in cards[1:]:
            card_rank = get_rank(card)
            if card_rank != group_rank and card_rank != wildcard_rank:
                result = False
                break
        valid_groups[(tuple(cards), wildcard_rank)] = result
    
    return valid_groups[(tuple(cards), wildcard_rank)]

valid_sequences = dict()
def is_valid_sequence(cards, wildcard_rank):
    """ (list<Card>, int) -> bool
    Checks if the given list of cards forms a valid sequence.
    A sequence is a set of three or more cards of the same suit with consecutive rank.
    A wildcard (card of the given wildcard rank) can fit in any sequence.
    >>> is_valid_sequence([get_card(HEARTS, TWO), get_card(HEARTS, THREE), get_card(HEARTS, FOUR)])
    True
    >>> is_valid_sequence([get_card(HEARTS, TWO), get_card(HEARTS, THREE), get_card(HEARTS, TEN)])
    False
    >>> is_valid_sequence([])
    False
    """
    if (tuple(cards), wildcard_rank) not in valid_sequences:
        result = True
        
        num_wildcards = 0
        for i in range(len(cards)-1, -1, -1):
            card = cards[i]
            if get_rank(card) == wildcard_rank:
                num_wildcards += 1
                cards.remove(card)
    
        if len(cards) < 3-num_wildcards:
            result = False
        elif not all_same_suit(cards):
            result = False
        else:
            cards.sort()
    
            i = 1
            while i < len(cards):
                if get_rank(cards[i]) != get_rank(cards[i-1])+1:
                    result = False
                    break
                i += 1
        valid_sequences[(tuple(cards), wildcard_rank)] = result
    
    return valid_sequences[(tuple(cards), wildcard_rank)]

def arrangement_to_string(arrangement):
    s = ''
    i = 1
    for seq in arrangement:
        s += str(i) + "\t" + hand_to_string(seq) + "\n"
        i += 1
    return s

occurrences = {}
def equal_or_less_occurrences(elements, nested_list):
    elements = elements[:]
    elements.sort()
    nested_list = nested_list[:] # shallow copy is OK here
    nested_list.sort()
    element_str = hand_to_string(elements)
    nested_str = tuple(hand_to_string(combo) for combo in nested_list)
    if (element_str, nested_str) not in occurrences:
        result = True
        counts = Counter(elements)
        for x in elements:
            num2 = 0
            for sublist in nested_list:
                num2 += sublist.count(x)
            if num2 > counts[x]:
                result = False
                break
        occurrences[(element_str, nested_str)] = result
    return occurrences[(element_str, nested_str)]

def count_elements(nested_list):
    num = 0
    for x in nested_list:
        for y in x:
            num += 1
    return num

def get_arrangement(hand, wildcard_rank):
    if len(hand) < 3:
        return []
    
    valid_combinations = set()
    for group_length in range(3, len(hand)+1):
        for combination in combinations(hand, group_length):
            combination = list(combination)
            combination.sort()
            if is_valid_group(combination, wildcard_rank) or is_valid_sequence(combination, wildcard_rank):
                valid_combinations.add(tuple(combination))
    
    if len(valid_combinations) == 0:
        return []
    
    # find optimal combination of groups and sequences
    cur_max_arrangements = []
    cur_max_arranged_cards = 0
    max_possible_arrangements = min(len(valid_combinations), len(hand) // 3)
    for num_sequences in range(max_possible_arrangements, -1, -1):
        for arrangement in combinations(valid_combinations, num_sequences):
            arrangement = list(arrangement)
            arrangement.sort()
            if equal_or_less_occurrences(hand, arrangement) and arrangement not in cur_max_arrangements:
                num_cards_in_sequence = count_elements(arrangement)
                if num_cards_in_sequence > cur_max_arranged_cards:
                    cur_max_arranged_cards = num_cards_in_sequence
                    cur_max_arrangements = [arrangement]
                elif num_cards_in_sequence == cur_max_arranged_cards:
                    cur_max_arrangements.append(arrangement)
    
    if cur_max_arranged_cards == len(hand):
        best_arrangement = cur_max_arrangements[0]
    else:
        min_point_val = math.inf
        best_arrangement = None
        points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]
        for arrangement in cur_max_arrangements:
            unarranged_cards = hand[:]
            for seq in arrangement:
                for card in seq:
                    unarranged_cards.remove(card)
            #assert len(hand2) == 1
            point_value = 0
            for card in unarranged_cards:
                point_value += points[RANKS.index(get_rank(card))]
            if point_value < min_point_val:
                min_point_val = point_value
                best_arrangement = arrangement
    assert best_arrangement is not None
    
    arrangement = []
    for combo in best_arrangement:
        arrangement.append(list(combo))
    return arrangement