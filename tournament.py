from typing import List, Tuple

from ex0 import CreatureFactory
from ex2 import BattleStrategy, InvalidCreatureError

Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    creatures = [(factory.create_base(), strategy)
                 for factory, strategy in opponents]
    for index, (first, first_strategy) in enumerate(creatures):
        for second, second_strategy in creatures[index + 1:]:
            print("\n* Battle *")
            print(first.describe())
            print("vs.")
            print(second.describe())
            print("now fight!")
            try:
                for action in first_strategy.act(first):
                    print(action)
                for action in second_strategy.act(second):
                    print(action)
            except InvalidCreatureError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


if __name__ == "__main__":
    from ex0 import AquaFactory, FlameFactory
    from ex1 import HealingCreatureFactory, TransformCreatureFactory
    from ex2 import (AggressiveStrategy, DefensiveStrategy,
                     NormalStrategy)

    scenarios = [
        [(FlameFactory(), NormalStrategy()),
         (HealingCreatureFactory(), DefensiveStrategy())],
        [(FlameFactory(), AggressiveStrategy()),
         (HealingCreatureFactory(), DefensiveStrategy())],
        [(AquaFactory(), NormalStrategy()),
         (HealingCreatureFactory(), DefensiveStrategy()),
         (TransformCreatureFactory(), AggressiveStrategy())],
    ]
    for opponents in scenarios:
        battle(opponents)
