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
    
    if message.content.startswith('!stop') :
        print('stop')
        sys.exit()

    if message.author.id == GAY:
        await channel.send(f"<@{str(GAY)}> is gay")

    if message.author.id == SEXY:
        await channel.send(f"<@{str(sexyId)}> is sexy waifu")

    if message.content.lower().startswith('no u'):
        await channel.send('no u')

    #commands after
    if not message.content.startswith('!'):
        return

    if message.content.startswith('!help'):
        print('help')
        await channel.send('```help: shows commands\npepega: just run it\nsprint [username]```')
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
        if len(args) < 2:
            await channel.send('Missing argument')
            print("sprint no arguments")
            return
        username = str(args[0])
        print(username)
        mode = str(args[1])
        print(mode)

        try:
            result = jstris.sprint(username,mode)  
            await channel.send(embed=result)
        except jstris.ModeError:
            print(f'sprint invalid mode {mode}')
            await channel.sent('Invalid Mode')
        except jstris.UsernameError:
            print(f'sprint invalid username {username}')
            await channel.send('Invalid username')
        #except: 
        #    print('sprint went very wrong')
        #    await channel.send('Unknown Error')
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
