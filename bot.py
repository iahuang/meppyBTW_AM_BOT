import sys
import time
import json
import discord
import requests
import jstris

with open('.\keys.json', 'r') as read_file:
    keys = json.load(read_file)
    TOKEN = keys["TOKEN"]   
    OWNER = keys["OWNER"]
    GAY = keys["GAY"]
    SEXY = keys["SEXY"]
    read_file.close()



client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    message_id = message.id
    channel = message.channel
    
    if message.content.startswith('!stop') and message.author.id == OWNER:
        print('stop')
        sys.exit()

    if message.author.id == GAY:
        await channel.send(f"<@{message.author.id}> is gay")

    if message.author.id == SEXY:
        await channel.send(f"<@{message.author.id}> is sexy waifu")

    if message.content.lower().startswith('no u '):
        await channel.send('no u')
    
    if message.content.count('@everyone') > 0:
        for i in range(5):
            await channel.send(f"<@{message.author.id}> is bad")
        return

    #commands after
    if not message.content.startswith('!'):
        return

    if message.content.startswith('!help'):
        print('help')
        await channel.send('```help: shows commands\npepega: just run it\nsprint [username] [20L/40L/100L/1000L, defaults to 40L]\ncheese [username] [10L/18L/100L, defaults to 100L]```')
        return

    if message.content.startswith('!owner'):
        await channel.send('This bot is run and maintained by meppydc')
        return

    if message.content.startswith('!pepega'):
        print('pepega') 
        await channel.send(f'<@{message.author.id}> is supa pepega')
        return

    if message.content.startswith('!everyone'):
        print('everyone')
        await channel.send('haha you thought this would ping everyone? Nice try buddy')
        return
    
    if message.content.startswith('!sprint'):
        args = message.content.split(' ')[1:]
        if len(args) < 1:
            await channel.send('Missing username')
            print("sprint no arguments")
            return
        username = str(args[0])
        if len(args) < 2:
            mode = '40L'
        else:
            mode = str(args[1])
        print(username,mode)

        try:
            result = jstris.SPRINT.get_mode_embed(username,mode)
            await channel.send(embed=result)
        except jstris.ModeError:
            print(f'sprint invalid mode {mode}')
            await channel.send('Invalid Mode')
        except jstris.UsernameError:
            print(f'sprint invalid username {username}')
            await channel.send(f'Invalid username')
        return

    if message.content.startswith('!cheese'):
        args = message.content.split(' ')[1:]
        if len(args) < 1:
            await channel.send('Missing username')
            print("cheese no arguments")
            return
        username = str(args[0])
        if len(args) < 2:
            mode = '100L'
        else:
            mode = str(args[1])
        print('cheese',username,mode)

        try:
            result = jstris.CHEESE.get_mode_embed(username,mode)
            await channel.send(embed=result)
        except jstris.ModeError:
            print(f'cheese invalid mode {mode}')
            await channel.send('Invalid Mode')
        except jstris.UsernameError:
            print(f'cheese invalid username {username}')
            await channel.send('Invalid username')
        return

    if message.content.startswith('!survival'):
        args = message.content.split(' ')[1:]
        if len(args) < 1:
            await channel.send('Missing username')
            print('survival no arguments')
            return
        username = str(args[0])
        mode = ''
        print('survival',username,mode)

        try:
            result = jstris.SURVIVAL.get_mode_embed(username,mode)
            await channel.send(embed=result)
        except jstris.ModeError:
            print(f'survival invalid mode {mode}')
            await channel.send('Invalid Mode')
        except jstris.UsernameError:
            print(f'survival invalid username {username}')
            await channel.send('Invalid username')
        return

    if message.content.startswith('!ultra'):
        args = message.content.split(' ')[1:]
        if len(args) < 1:
            await channel.send('Missing username')
            print('ultra no arguments')
            return
        username = str(args[0])
        mode = ''
        print('ultra',username,mode)

        try:
            result = jstris.ULTRA.get_mode_embed(username,mode)
            await channel.send(embed=result)
        except jstris.ModeError:
            print(f'ultra invalid mode {mode}')
            await channel.send('Invalid Mode')
        except jstris.UsernameError:
            print(f'ultra invalid username {username}')
            await channel.send('Invalid username')
        return

    if message.content.startswith('!embed'):

        embed = jstris.embed_test()
        await channel.send(embed=embed)
        return
    
    #await channel.send("Invalid command")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)
