import sys
import time
import json
import discord
import requests

with open('.\meppyBTW_AM_BOT\keys.json', 'r') as read_file:
    TOKEN = json.load(read_file)["TOKEN"]

#jstris stuff
jstrisModes = [
    [None],
    ['Sprint','40L','20L','100L','1000L'],
    ['Freeplay'],
    ['Cheese','10L','18L','100L'],
    ['Survival','Survival'],
    ['Ultra','Ultra'],
    ['Maps','no maps lol'], 
    ['Tsd','20TSD']
]

def get_records(username, mode, type):
    url = f'https://jstris.jezevec10.com/api/u/{username}/records/{mode}?mode={type}'

    r = requests.get(url)
    return r.json()

def create_embed(r, play, type):
    
    embed = discord.Embed(title=r[name], colour=discord.Colour(0xe67e22), url="https://jstris.jezevec10.com/u/{r[name]}", description="Displaying {play} {type} statistics for player {r[name]} on Jstris")

    embed.add_field(name="Best", value=str(r[min]), inline=True)
    embed.add_field(name="Worst", value=str(r[max]), inline=True)
    embed.add_field(name="Average", value=str(r[avg]), inline=True)
    embed.add_field(name="Total Games", value=str(r[games]), inline=True)
    embed.add_field(name="Mode (1s)", value=r[mode]["1"], inline=True)
    embed.add_field(name="Mode (0.1s)", value=r[mode]["0.1"], inline=True)
    embed.add_field(name="Time spent(sec lol)", value=r[sum], inline=True)
    embed.add_field(name="Avg. spent/day", value=str(r[sums]/r[days]), inline=True)
    embed.add_field(name="Avg. games/day", value=str(r[games]/r[days]), inline=True)

    #await bot.say(embed=embed)
    return embed


class Mode:
    def __init__(self,mode,id,*types) :
        self.mode = mode
        self.id = id
        self.types = types
    
    def get_type(type):
        try:
            return types.index(type)
        except ValueError:
            return None


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    message_id = message.id
    channel = message.channel
    
    if message.content.startswith('!stop'):
        print('stop')
        sys.exit()

    #for kirigo the 0iq
    gayId = 115253155524116488
    if message.author.id == gayId:
        await channel.send("<@" + str(gayId) + "> is gay")

    sexyId = 513442537483272224
    if message.author.id == sexyId:
        await channel.send("<@"+ str(sexyId) + "> is sexy")

    if message.content.lower().startswith('no u'):
        await channel.send('no u')

    #commands after
    if not message.content.startswith('!'):
        return

    print("message")

    if message.content.startswith('!help'):
        print('help')
        await channel.send('''
```help: shows commands
pepega: just run it
everyone: ping everyone
```
        ''')

    if message.content.startswith('!pepega'):
        print('pepega') 
        await channel.send('<@' + str(message.author.id) + '> is supa pepega')

    if message.content.startswith('!everyone'):
        print('everyone')
        await channel.send('haha you thought this would ping everyone? Nice try buddy')
    
    if message.content.startswith('!sprint'):
        args = message.content.split(' ')[1:]
        if len(args) < 1:
            await channel.send('No user specified')
            return
        
        record_data = get_records(args[0],1,1)

        try:
            await channel.send(f'''{args[0]} has a 40L pb of {record_data['min']}s''')
            #result = create_embed(record_data,1,1)  
            #await channel.send(result) 
        except:
            await channel.send('Invalid username')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)