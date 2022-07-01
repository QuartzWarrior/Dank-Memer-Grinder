try:
    import discord
except ModuleNotFoundError:
    import os

    os.system("python -m pip install -U git+https://github.com/dolfies/discord.py-self.git")
    import discord
import time

import keep_online
from discord.ext import tasks

client = discord.Client()

channel = None

channel_id = int(input("Channel ID\n\n-> "))


@client.event
async def on_ready():
    global channel
    print(f"Logged in as {client.user}")
    channel = client.get_channel(channel_id)
    beg.start()
    time.sleep(0.3)
    dig.add_exception_type(TypeError)
    dig.start()
    time.sleep(1)
    fish.add_exception_type(TypeError)
    fish.start()
    time.sleep(1)
    deposit.start()
    time.sleep(0.3)
    work.start()
    time.sleep(0.3)
    sell.add_exception_type(TypeError)
    sell.start()
    keep_online.start()


@tasks.loop(seconds=36.5)
async def beg():
    await channel.send("pls beg")


@tasks.loop(seconds=37.1)
async def dig():
    #    await asyncio.sleep(7/350*60)
    await channel.send("pls dig")
    answer = await client.wait_for('message',
                                   check=lambda message: message.author.id == 270904126974590976 and not message.embeds)
    if "You don't have a shovel" in answer.content:
        #        await asyncio.sleep(12/350*60)
        await channel.send("pls with all")
        #        await asyncio.sleep(15/350*60)
        await channel.send("pls shop shovel")
        shovel = await client.wait_for('message', check=lambda
            message: message.author.id == 270904126974590976 and message.embeds and 'Shovel' in message.embeds[0].title)
        #        await asyncio.sleep(7/350*60)
        await channel.send("pls bal")
        balance = await client.wait_for('message', check=lambda
            message: message.author.id == 270904126974590976 and message.embeds and 'balance' in message.embeds[
            0].title)
        if int(shovel.embeds[0].title.split("(")[1].replace(" owned)", "")) == 0 and int(
                balance.embeds[0].description.split("**Wallet**: ⏣ ")[1].split("**Bank**: ⏣ ")[0].replace(",",
                                                                                                          "")) >= 25000:
            #            await asyncio.sleep(14/350*60)
            await channel.send("pls buy shovel")
    else:
        return


@tasks.loop(seconds=37.9)
async def fish():
    #    await asyncio.sleep(8/350*60)
    await channel.send("pls fish")
    answer = await client.wait_for('message',
                                   check=lambda message: message.author.id == 270904126974590976 and not message.embeds)
    if "You don't have a fishing pole" in answer.content:
        #        await asyncio.sleep(12/350*60)
        await channel.send("pls with all")
        #        await asyncio.sleep(20/350*60)
        await channel.send("pls shop fishingpole")
        fishing_pole = await client.wait_for('message', check=lambda
            message: message.author.id == 270904126974590976 and message.embeds and 'Fishing Pole' in message.embeds[
            0].title)
        #        await asyncio.sleep(7/350*60)
        await channel.send("pls bal")
        balance = await client.wait_for('message', check=lambda
            message: message.author.id == 270904126974590976 and message.embeds and 'balance' in message.embeds[
            0].title)
        if int(fishing_pole.embeds[0].title.split("(")[1].replace(" owned)", "")) == 0 and int(
                balance.embeds[0].description.split("**Wallet**: ⏣ ")[1].split("**Bank**: ⏣ ")[0].replace(",",
                                                                                                          "")) >= 25000:
            #            await asyncio.sleep(19/350*60)
            await channel.send("pls buy fishingpole")
    else:
        return


@tasks.loop(minutes=15)
async def sell():
    await channel.send("pls sell")
    answer = await client.wait_for('message', check=lambda
        message: message.author.id == 270904126974590976 and message.embeds and 'Pending Confirmation' in
                 message.embeds[0].title)
    button = answer.components[0].children[1]
    await button.click()


@tasks.loop(seconds=150)
async def deposit():
    await channel.send("pls dep all")


@tasks.loop(hours=1.03)
async def work():
    await channel.send("pls work")
    answer = await client.wait_for('message',
                                   check=lambda message: message.author.id == 270904126974590976 and message.embeds)
    if 'You don\'t currently have a job to work at' in answer.content:
        await channel.send("pls work housewife")


client.run(input("Token\n\n-> "))
