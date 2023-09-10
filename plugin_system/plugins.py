import json
from dataclasses import dataclass

from game import loader, factory


@dataclass
class Sorcerer:
    name: str

    def make_noise(self):
        print("aahh!")


@dataclass
class Wizard:
    name: str

    def make_noise(self):
        print("boooh!")


@dataclass
class Witcher:
    name: str

    def make_noise(self):
        print("mmmhhh!")


def main():
    data = None
    with open("./plugin_system/plugins.json") as file:
        data = json.load(file)
        file.close()
    if not data:
        raise Exception("no data")

    # load from plugins new character to the factory
    if data.get("plugins"):
        loader.load_plugins(data["plugins"])

    # register characters
    factory.register("sorcerer", Sorcerer)
    factory.register("wizard", Wizard)
    factory.register("witcher", Witcher)

    # old method
    # characters: list[GameCharacter] = []
    # for item in data["characters"]:
    #    item_copy = item.copy()
    #    character_type = item_copy.pop("type")
    #    if character_type == "sorcerer":
    #        characters.append(Sorcerer(**item_copy))
    #    if character_type == "wizard":
    #        characters.append(Wizard(**item_copy))
    #    if character_type == "witcher":
    #        characters.append(Witcher(**item_copy))

    # new method with factories using list comprehension
    characters = [factory.create(item) for item in data.get("characters", None)]

    for character in characters:
        print(character, end="\t")
        character.make_noise()


if __name__ == "__main__":
    main()
