from typing import cast

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    for label, create in (("base", factory.create_base),
                          ("evolved", factory.create_evolved)):
        print(f"{label}:")
        creature = create()
        print(creature.describe())
        print(creature.attack())
        print(cast(HealCapability, creature).heal())
    print()


def test_transforming() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    for label, create in (("base", factory.create_base),
                          ("evolved", factory.create_evolved)):
        print(f"{label}:")
        creature = create()
        print(creature.describe())
        print(creature.attack())
        transformable = cast(TransformCapability, creature)
        print(transformable.transform())
        print(creature.attack())
        print(transformable.revert())


if __name__ == "__main__":
    test_healing()
    test_transforming()
