from typing import Tuple

import datetime

import discord
from coffee_counter import CoffeeCounter

client = discord.Client()

coffeeList = []

timezone = datetime.timezone(datetime.timedelta(hours = -10))

@client.event
async def on_ready():
    for guild in client.guilds:
        for member in guild.members:
            coffeeList.append(CoffeeCounter(member=member, count=0))

    global day
    global last_day

    day = datetime.datetime.now(tz=timezone).day
    last_day = day

@client.event
async def on_message(message):

    global day
    global last_day

    if message.author == client.user:
        return

    day = datetime.datetime.now(tz=timezone).day

    if day != last_day:
        for user in coffeeList:
            user.reset()

    print(str(datetime.datetime.now(tz=timezone).hour))

    if message.content.startswith('!coffee'):
        for user in coffeeList:
            if message.author == user.member:
                user.increment()
                await message.channel.send(user.message())

    last_day = day


client.run('NzM1MTgxOTQ2MzI1MzAzMjk2.Xxchuw.ucNJaiekEn-yb4wcstccxBk3kc4')
