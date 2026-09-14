from abc import ABC, abstractmethod
from typing import List, cast

from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidCreatureError(Exception):
    pass


class BattleStrategy(ABC):
    name = "strategy"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> List[str]:
        pass

    def _require_valid(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidCreatureError(
                f"Invalid Creature '{creature.name}' for this {self.name} "
                "strategy"
            )


class NormalStrategy(BattleStrategy):
    name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> List[str]:
        self._require_valid(creature)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> List[str]:
        self._require_valid(creature)
        transformable = cast(TransformCapability, creature)
        return [
            transformable.transform(),
            creature.attack(),
            transformable.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> List[str]:
        self._require_valid(creature)
        healer = cast(HealCapability, creature)
        return [creature.attack(), healer.heal()]
