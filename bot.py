import sys
import time
import json
import discord
import requests

with open('.\keys.json', 'r') as read_file:
    keys = json.load(read_file)
    TOKEN = keys["TOKEN"]   
    OWNER = keys["OWNER"]
    read_file.close()

#jstris stuff
jstris_modes = [
    [None],
    ['Sprint','40L','20L','100L','1000L'],
    ['Freeplay'],
    ['Cheese','10L','18L','100L'],
    ['Survival','Survival'],
    ['Ultra','Ultra'],
    ['Maps','no maps lol'], 
    ['Tsd','20TSD']]

def get_records(username, play, type):
    url = f'https://jstris.jezevec10.com/api/u/{username}/records/{play}?mode={type}'

    r = requests.get(url)
    return r.json()

def create_embed(username, play, type):

    r = get_records(username, play, type)
    
    #integrate stats thing better later
    embed = discord.Embed(title=r['name'], colour=discord.Colour(0xe67e22), url=f"https://jstris.jezevec10.com/u/{r['name']}", description=f"Displaying {jstris_modes[play][type]} {jstris_modes[play][0]} statistics for player {r['name']} on Jstris")
    
    try:
        #try tenth first because ones can't exist without tenths? not sure if it works that way
        mode_tenth_time = r['mode']['0.1'][0]
        mode_tenth_freq = r['mode']['0.1'][1]
        mode_one_time = r['mode']['1'][0]
        mode_one_freq = r['mode']['1'][1]
    except:
        mode_one_time = "n/a"
        mode_one_freq = "n/a"
        mode_tenth_time = "n/a"
        mode_tenth_freq = "n/a"
    days = r['days'] or 1

    embed.add_field(name="Best", value=r['min'], inline=True)
    embed.add_field(name="Worst", value=r['max'], inline=True)
    embed.add_field(name="Average", value=r['avg'], inline=True)

    embed.add_field(name="Total Games", value=r['games'], inline=True)
    embed.add_field(name="Mode (1s)", value= mode_one_time, inline=True)
    embed.add_field(name="Freq (1s)", value= mode_one_freq, inline=True)

    embed.add_field(name="Days of playing", value=r['days'], inline=True)
    embed.add_field(name="Mode (0.1s)", value=mode_tenth_time,  inline=True)
    embed.add_field(name="Freq (0.1s)", value= mode_tenth_freq, inline=True)

    embed.add_field(name="Time spent(sec lol)", value=r['sum'], inline=True)
    embed.add_field(name="Avg. spent/day", value=r['sum']/days, inline=True)
    embed.add_field(name="Avg. games/day", value=r['games']/days, inline=True)

    return embed


#bot stuff
def embed_test():
    embed = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~", colour=discord.Colour(0x30298a), url="https://discordapp.com", description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```")

    embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    embed.add_field(name="🤔", value="some of these properties have certain limits...")
    embed.add_field(name="🙄", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
    embed.add_field(name="<:pepega:667519589856313375>", value="these last two", inline=True)
    embed.add_field(name="<:pepega:667519589856313375>", value="are inline fields", inline=True)

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
    
    if message.content.startswith('!stop') :
        print('stop')
        sys.exit()

    #for kirigo the 0iq
    gayId = 115253155524116488
    if message.author.id == gayId:
        await channel.send("<@" + str(gayId) + "> is gay")

    sexyId = 513442537483272224
    if message.author.id == sexyId:
        await channel.send("<@"+ str(sexyId) + "> is sexy waifu")

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
        print('sprint')
        args = message.content.split(' ')[1:]
        if len(args) < 1:
            await channel.send('No user specified')
            return
        
        username = str(args[0])

        try:
            result = create_embed(username,1,1)   
            await channel.send(embed=result) 
        except:
            await channel.send('Invalid username')
        return

    if message.content.startswith('!embed'):

        embed = embed_test()
        await channel.send(embed=embed)
        return
    
    await channel.send("Invalid command")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)