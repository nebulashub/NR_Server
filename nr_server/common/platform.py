from enum import Enum, unique


@unique
class Platform(Enum):
    Nebulas = 'nebulas'
    Eth = 'eth'

    @classmethod
    def from_value(cls, v: str):
        if cls.valid(v):
            return Platform(v)
        return None

    @staticmethod
    def valid(v: str):
        return v in ['nebulas', 'eth']
