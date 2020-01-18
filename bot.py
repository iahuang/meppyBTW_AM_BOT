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


#bot stuff
def embed_test():
    embed = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~", colour=discord.Colour(0x30298a), url="https://discordapp.com", description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```")

    embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    embed.add_field(name="🤔", value="some of these properties have certain limits...")
    embed.add_field(name="🙄", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
    embed.add_field(name="<:pepega:667519589856313375>", value="these last two", inline=True)
    embed.add_field(name="<:pepega:667519589856313375>", value="are inline fields", inline=True)

    return embed



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
        await channel.send('<@' + str(message.author.id) + '> is supa pepega')
        return

    if message.content.startswith('!everyone'):
        print('everyone')
        await channel.send('haha you thought this would ping everyone? Nice try buddy')
        return
    
    if message.content.startswith('!sprint'):
        args = message.content.split(' ')[1:]
        if len(args) < 1:
            await channel.send('No user specified')
            print("sprint no user")
            return
        username = str(args[0])

        try:
            print("1")s
            result = jstris.create_embed(username,1,1)  
            print("2")
            await channel.send(embed=result) 
        except:
            print(f'sprint invalid username {username}')
            await channel.send('Invalid username')
        return

    if message.content.startswith('!embed'):

        embed = embed_test()
        await channel.send(embed=embed)
        return
    
    #await channel.send("Invalid command")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)