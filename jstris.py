#jstris related features for the bot

jstris_modes = [
    [None],
    ['Sprint','40L','20L','100L','1000L'],
    ['Freeplay'],
    ['Cheese','10L','18L','100L'],
    ['Survival','Survival'],
    ['Ultra','Ultra'],
    ['Maps','no maps lol'], 
    ['Tsd','20TSD']]

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

def get_records(username, play, type):
    url = f'https://jstris.jezevec10.com/api/u/{username}/records/{play}?mode={type}'

    r = requests.get(url)
    return r.json()

def create_embed(username, play, type):

    r = get_records(username, play, type)

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
            description=f"Displaying {jstris_modes[play][type]} {jstris_modes[play][0]} statistics for player {r['name']} on Jstris") 
    
    embed.add_field(name="Best", value=r['min'] if play != 4 else r['max'], inline=True)
    embed.add_field(name="Worst", value=r['max'] if play != 4 else r['min'], inline=True)
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


class Jstris:
    def __init__(self):
        self.SPRINT = Mode('sprint',1,['40L','20L','100L','1000L'])
        self.CHEESE = Mode('cheese',3,['10L','18L','100L'])

    def sprint(username,type):
        return

    def cheese(username,type):
        return

    def survival(username):
        return

    def ultra(username):
        return

    def tsd(username):
        return
