
from typing import Any, Callable
from game.character import GameCharacter

character_create_fn: dict[str, Callable[..., GameCharacter]] = {}


def register(char_type: str, creation_fn: Callable[..., GameCharacter]):
    """register a new game character type"""
    character_create_fn[char_type] = creation_fn


def unregister(char_type: str):
    """Unregister game character type"""
    character_create_fn.pop(char_type, None)


def create(args: dict[str, Any]) -> GameCharacter:
    """Create game character of specific type, given arguments"""
    args_copy = args.copy()
    char_type = args_copy.pop("type")
    try:
        creation_fn = character_create_fn[char_type]
        return creation_fn(**args_copy)
    except KeyError as error:
        raise ValueError("no valid character: %s (%s)" % (char_type, error))
