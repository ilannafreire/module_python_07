from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    for create in (factory.create_base, factory.create_evolved):
        creature = create()
        print(creature.describe())
        print(creature.attack())
    print()


def test_battle(first_factory: CreatureFactory,
                second_factory: CreatureFactory) -> None:
    print("Testing battle")
    first = first_factory.create_base()
    second = second_factory.create_base()
    print(first.describe())
    print("vs.")
    print(second.describe())
    print("fight!")
    print(first.attack())
    print(second.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)
