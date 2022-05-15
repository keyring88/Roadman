import os
import discord
import random



def randnum(fname):
	lines=open(fname).read().splitlines()
	return random.choice(lines)




client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$roadman'):
        await message.channel.send(randnum('quotes.txt'))

client.run(os.getenv('TOKEN'))