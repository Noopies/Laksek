import discord
import asyncio


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.get_server)



@client.event
async def on_message(message):
    await client.change_presence(game=discord.Game(name='With Fire'))
    if "dasar culun" in message.content :
        if message.channel.name == "dota" and message.author== "Dest1nationX#5726" :
            await client.send_message(message.channel,message.author.mention)
            await client.send_file(message.channel, './Image/Roast.PNG')


    if "dasar culun lu" in message.content :
        await client.send_message(message.channel,message.author.mention)
        await client.send_file(message.channel, './Image/Roast.PNG')

    if message.content.startswith("!avatar"):
        Nama= message.content.split(" ")

        await client.send_message(message.channel,message.server.get_member_named(Nama[1]).avatar_url)




    print(message.author.name)
    









client.run('NDA5MDczNjUyMDgxMDk4NzUz.DVZWVw.B_YrSej_x5fgCB4XQm3hN2BwuQI')
