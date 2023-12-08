""" Day seven """

from collections import Counter


def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def label_to_number(cards, wildcard=False) -> list[int]:
    mapping = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1 if wildcard else 11,
        "T": 10
    }
    return [int(mapping.get(card, card)) for card in cards]


def get_score(cards, wildcard=False) -> int:
    cards = list(cards)

    jokers = 0
    if wildcard:
        jokers = cards.count("J")
        cards = [card for card in cards if card != "J"]

    counts = list(Counter(cards).values())

    if 5 in counts or jokers == 5:
        rank_score = 50
    elif 4 in counts:
        rank_score = 10 * (4 + jokers)
    elif 3 in counts and 2 in counts:
        rank_score = 32
    elif 3 in counts:
        rank_score = 10 * (3 + jokers)
    elif 2 in counts and list(counts).count(2) == 2:
        rank_score = 22 + 10 * jokers
    elif 2 in counts:
        rank_score = 10 * (2 + jokers)
    else:
        rank_score = 10 * (1 + jokers)

    return rank_score


def calculate_score(lines, wildcard=False) -> int:
    hands = [(label_to_number(hand[0], wildcard=wildcard), int(hand[1]), get_score(hand[0], wildcard=wildcard))
             for hand in [line.split() for line in lines]]
    hands = sorted(hands, key=lambda hand: (hand[2], hand[0]))
    return sum(rank * hand[1] for rank, hand in enumerate(hands, start=1))


def part_one(lines: list):
    print(calculate_score(lines))


def part_two(lines: list):
    print(calculate_score(lines, wildcard=True))


if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
