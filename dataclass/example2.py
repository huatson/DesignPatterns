import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:
    # dataclass:
    #   frozen: prevents data change after creation
    #   kw_only:forze to use keywords arguments only
    #   match_args:
    #   slots:
    name: str
    address: str
    active: bool = True
    emails: list[str] = field(default_factory=list)
    # generates a random id
    id: str = field(init=False, default_factory=generate_id)
    # search field when we want to search this entry
    _search_fields: str = field(init=False, repr=False)

    def __post_init__(self):
        self._search_fields = f"{self.name} {self.address}"


def main():
    person = Person(name="Gerald", address="123 south street", active=False)
    print(person)


if __name__ == "__main__":
    main()
