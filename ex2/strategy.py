from abc import ABC, abstractmethod
from typing import List, cast

from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidCreatureError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> List[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise InvalidCreatureError(
                f"Invalid Creature '{getattr(creature, 'name', creature)}' "
                "for this normal strategy"
            )
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise InvalidCreatureError(
                f"Invalid Creature '{getattr(creature, 'name', creature)}' "
                "for this aggressive strategy"
            )
        transformable = cast(TransformCapability, creature)
        return [
            transformable.transform(),
            creature.attack(),
            transformable.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise InvalidCreatureError(
                f"Invalid Creature '{getattr(creature, 'name', creature)}' "
                "for this defensive strategy"
            )
        healer = cast(HealCapability, creature)
        return [creature.attack(), healer.heal()]
