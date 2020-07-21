from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discord import Member

class CoffeeCounter:

    def __init__(self, member: discord.Member, count: int = 0):
        self.member = member
        self.count = count

    def getCount(self) -> int:
        return self.count

    def increment(self) -> None:
        self.count +=1

    def message(self) -> str:
        if self.count < 2:
            message = self.member.mention + " you have had " + str(self.count) + " cup of coffee."
        else:
            message = self.member.mention + " you have had " + str(self.count) + " cups of coffee."
        return message

    def reset(self) -> None:
        self.count = 0
