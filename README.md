# Module 07 - DataDeck

## Overview

This project is part of the 42 curriculum and focuses on advanced object-oriented
programming concepts in Python.

DataDeck simulates a creature card system. Creatures belong to families, can be
created through abstract factories, may provide additional capabilities, and can
act according to different battle strategies.

The project is divided into three exercises:

- Exercise 0 introduces the Abstract Factory pattern.
- Exercise 1 adds independent healing and transformation capabilities.
- Exercise 2 introduces the Strategy pattern for tournament battles.

The implementation follows the project requirements: Python 3.10 or later,
abstract classes, type annotations, standard libraries only, and no external
dependencies.

## Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Exercise 0 - Creature Factory](#exercise-0---creature-factory)
- [Exercise 1 - Capabilities](#exercise-1---capabilities)
- [Exercise 2 - Abstract Strategy](#exercise-2---abstract-strategy)
- [Validation](#validation)

## Project Structure

```text
.
├── battle.py
├── capacitor.py
├── tournament.py
├── ex0/
│   ├── __init__.py
│   ├── creature.py
│   └── factory.py
├── ex1/
│   ├── __init__.py
│   ├── capability.py
│   ├── creature.py
│   └── factory.py
├── ex2/
│   ├── __init__.py
│   └── strategy.py
└── README.md
```

Each exercise directory is a Python package and contains a mandatory
`__init__.py` file. The public package interfaces expose factories and
strategies while keeping concrete creature classes internal to their modules.

## Requirements

- Python 3.10 or later.
- `flake8` for style validation.
- `mypy` for static type checking.
- No external runtime libraries are required.

## Exercise 0 - Creature Factory

Exercise 0 implements the Abstract Factory pattern for two creature families.

### Abstract classes

`Creature` defines the common creature interface:

- Stores the creature `name` and `creature_type`.
- Provides the concrete `describe()` method.
- Declares the abstract `attack()` method.

`CreatureFactory` defines the factory interface:

- `create_base()` creates a base creature.
- `create_evolved()` creates an evolved creature.

### Creature families

- `FlameFactory` creates `Flameling` and `Pyrodon`.
- `AquaFactory` creates `Aquabub` and `Torragon`.

The concrete creatures implement their own attack messages. The `ex0` package
exposes only `FlameFactory`, `AquaFactory`, and `CreatureFactory`.

### Running the exercise

```bash
python3 battle.py
```

The script tests both factories and makes the base creature from each family
fight.

## Exercise 1 - Capabilities

Exercise 1 extends the creature system without adding capabilities to the base
`Creature` class directly.

### Capabilities

`HealCapability` is an independent abstract class that defines `heal()`.

`TransformCapability` is an independent abstract class that defines:

- `transform()`
- `revert()`
- The persistent `transformed` state

### Healing creatures

- `Sproutling` is the base healing creature.
- `Bloomelle` is the evolved healing creature.
- Both inherit from `Creature` and `HealCapability`.

### Transforming creatures

- `Shiftling` is the base transforming creature.
- `Morphagon` is the evolved transforming creature.
- Both inherit from `Creature` and `TransformCapability`.

When a transforming creature changes state, its `attack()` method produces a
different result. The `ex1` package exposes only
`HealingCreatureFactory` and `TransformCreatureFactory`.

### Running the exercise

```bash
python3 capacitor.py
```

The script demonstrates the healing sequence and the transformation sequence:

```text
describe -> attack -> heal
describe -> attack -> transform -> attack -> revert
```

## Exercise 2 - Abstract Strategy

Exercise 2 implements the Strategy pattern for tournament battles. The battle
orchestration does not need to know the creature's capabilities. It delegates
the action to the strategy associated with each opponent.

### BattleStrategy

`BattleStrategy` is an abstract class that defines:

- `is_valid(creature) -> bool`
- `act(creature) -> list[str]`

If a strategy is used with an incompatible creature, `is_valid()` returns
`False` and `act()` raises `InvalidCreatureError` with a descriptive message.

### Concrete strategies

`NormalStrategy` is valid for every creature and performs one normal attack.

`AggressiveStrategy` is valid for creatures with `TransformCapability` and
performs:

```text
transform -> attack -> revert
```

`DefensiveStrategy` is valid for creatures with `HealCapability` and performs:

```text
attack -> heal
```

### Tournament

The `battle()` function in `tournament.py` receives a list of pairs containing
a `CreatureFactory` and a `BattleStrategy`. It creates the opponents, makes
each pair fight once, applies their strategies, and stops the tournament with a
clear error when a strategy is invalid for its creature.

### Running the exercise

```bash
python3 tournament.py
```

The script demonstrates a valid tournament, an invalid strategy-creature pair,
and a tournament with three opponents.

## Validation

Run the example scripts:

```bash
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

Run the static checks:

```bash
flake8 ex0 ex1 ex2 battle.py capacitor.py tournament.py
mypy ex0 ex1 ex2 battle.py capacitor.py tournament.py
```