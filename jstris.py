import requests
import json
import discord
#jstris related features for the bot

class ModeError(Exception):
    pass

class UsernameError(Exception):
    pass

class InvalidMode(Exception):
    pass

class Mode:
    #keep parameter names consistent with jstris url
    def __init__(self,name,play,*modes) :
        self.name = name
        self.play = play
        self.modes = modes
    
    def get_mode(mode):
        #raises ValueError
        return modes.index(mode)

jstris_modes = [
    [None],
    ['Sprint','40L','20L','100L','1000L'],
    ['Freeplay'],
    ['Cheese','10L','18L','100L'],
    ['Survival','Survival'],
    ['Ultra','Ultra'],
    ['Maps','no maps lol'], 
    ['Tsd','20TSD']]

SPRINT = Mode('Sprint',1,['40L','20L','100L','1000L'])
CHEESE = Mode('Cheese',3,['10L','18L','100L'])
SURVIVAL = 'sur'
ULTRA = 'ult'
TSD = 'useless api'

MODES = [None,SPRINT,'freeplay',CHEESE,SURVIVAL,ULTRA,'maps',TSD]

def get_records(username, play, mode):
    url = f'https://jstris.jezevec10.com/api/u/{username}/records/{play}?mode={mode}'

    r = requests.get(url)
    return r.json()

def create_embed(username, play, mode):

    r = get_records(username, play, mode)

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

    #integrate stats thing better later
    embed = discord.Embed(title=r['name'],
            colour=discord.Colour(0xe67e22),
            url=f"https://jstris.jezevec10.com/u/{r['name']}",
            description=f"Displaying {MODES[play]['modes'][mode]} {MODES[play]['name']} statistics for player {r['name']} on Jstris") 
    
    embed.add_field(name="Best", value=r['min'] if play != 4 and play != 5 else r['max'], inline=True)
    embed.add_field(name="Worst", value=r['max'] if play != 4 and play != 5  else r['min'], inline=True)
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

def sprint(username,mode):
    try:
        modeIndex = SPRINT.get_mode(mode)
    except ValueError:
        raise ModeError('ModeError')

    try:
        embed = create_embed(username,SPRINT.play,modeIndex)
    except:
        raise UsernameError('UsernameError') 

    return embed

def cheese(username,type):
    return

def survival(username):
    return

def ultra(username):
    return

def tsd(username):
    return

def embed_test():
    embed = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~", colour=discord.Colour(0x30298a), url="https://discordapp.com", description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```")

    embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    embed.add_field(name="🤔", value="some of these properties have certain limits...")
    embed.add_field(name="🙄", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
    embed.add_field(name="<:pepega:667519589856313375>", value="these last two", inline=True)
    embed.add_field(name="<:pepega:667519589856313375>", value="are inline fields", inline=True)

    return embed
