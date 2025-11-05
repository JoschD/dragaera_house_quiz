from dataclasses import dataclass, fields
from typing import Any

@dataclass(kw_only=True, slots=True)
class TheCycle:
    Phoenix: Any
    Dragon: Any
    Lyorn: Any
    Tiassa: Any
    Athyra: Any
    Issola: Any
    Yendi: Any
    Jhereg: Any
    Orca: Any
    Dzur: Any
    Jhegaala: Any
    Chreotha: Any
    Teckla: Any
    Tsalmoth: Any
    Vallista: Any
    Iorich: Any
    Hawk: Any

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def to_dict(self) -> dict[str, Any]:
        return dict(**{field.name: getattr(self, field.name) for field in fields(self)})

    def keys(self):
        return [field.name for field in fields(self)]


    def items(self):
        for field in fields(self):
            yield (field.name, getattr(self, field.name))

    def __len__(self) -> int:
        return self.len()

    @classmethod
    def len(cls) -> int:
        return 17
