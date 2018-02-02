import discord
import asyncio


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)

@client.event
async def on_message(message):
    download bokep
    if message.content.startswith('download'):
        if message.channel.name == "general":
            await client.send_file(message.channel, './Image/bsg.jpg')

client.run('NDA5MDczNjUyMDgxMDk4NzUz.DVZWVw.B_YrSej_x5fgCB4XQm3hN2BwuQI')
