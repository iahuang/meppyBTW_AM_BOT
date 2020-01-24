import requests
import json
import discord
#jstris related features for the bot

SITE = 'https://jstris.jezevec10.com'
class ModeError(Exception):
    pass

class UsernameError(Exception):
    pass

class APIError(Exception):
    pass

class Mode: 
    #keep parameter names consistent with jstris url
    def __init__(self,name,play,modes):
        self.name = name
        self.play = play
        self.modes = modes
    
    def get_mode(self,mode):
        #raises ValueError
        return self.modes.index(mode)
    
    def get_records(username, play, mode):
        url = f'{SITE}/api/u/{username}/records/{play}?mode={mode}&best'   

        r = requests.get(url)
        return r.json()

    def create_embed(self, username, mode):
        play = self.play
        r = Mode.get_records(username, play, mode)
        #print(play)
        #print(mode)

        if 'error' in r:
            print(r['error'])
            raise UsernameError()
        
        bestReplay = f"{SITE}/replay/{r['best'][0]['id']}" if len(r['best']) == 2 else ''

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

        playName = self.name
        modeName = self.modes[mode]

        #integrate stats thing better later
        embed = discord.Embed(title=r['name'],
                colour=discord.Colour(0xe67e22),
                url=f"https://jstris.jezevec10.com/u/{r['name']}?mode={play}",
                description=f"Displaying [{modeName} {playName}](https://jstris.jezevec10.com/?play={play}&mode={mode}) [statistics](https://jstris.jezevec10.com/{playName.casefold()}?display=5&user={r['name']}&lines={modeName}) for player [{r['name']}](https://jstris.jezevec10.com/u/{r['name']}) on [Jstris](https://jstris.jezevec10.com)\n[Best Game]({bestReplay})") 
            
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

    def get_mode_embed(self, username, mode):
        try:
            modeIndex = self.get_mode(f'{mode}L')
        except ValueError:
            raise ModeError()

        try:
            embed = self.create_embed(username,modeIndex)
        except UsernameError:
            raise UsernameError()

        return embed       

SPRINT = Mode('Sprint',1,['0L','40L','20L','100L','1000L'])
CHEESE = Mode('Cheese',3,['0L','10L','18L','100L'])
SURVIVAL = Mode('Survival',4,['0L','1L'])
ULTRA = Mode('Ultra',5,['0L','1L'])
TSD = Mode('Tsd',7,['0L','1L'])
PC = Mode('PC',8,['0L','1L'])

#MODES = [None,SPRINT,'freeplay',CHEESE,SURVIVAL,ULTRA,'maps',TSD ,PC]

def tsd(username):
    return "muda"

def pc(username):
    return "muda"

def embed_test():
    embed = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~",
            colour=discord.Colour(0x30298a),
            url="https://discordapp.com",
            description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```")

    embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    embed.add_field(name="🤔", value="some of these properties have certain limits...")
    embed.add_field(name="🙄", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
    embed.add_field(name="<:pepega:667519589856313375>", value="these last two", inline=True)
    embed.add_field(name="<:pepega:667519589856313375>", value="are inline fields", inline=True)

    return embed

#print(Mode.get_records('meppydc',1,1))
#print(SPRINT.get_mode_embed('meppydc','40L'))