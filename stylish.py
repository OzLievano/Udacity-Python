import random


def fish_and_chips(count):
    for fish in range(5 * count):
        # this is a ver long comment that do.

        print(random.choice(["fish", "chips", "Malt Vinegar"]))


fish_and_chips(2)
