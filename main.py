import discord
import os, random, json
from discord.ext import commands

intents = discord.Intents.default()  
intents.members = True  
################################################################################################################
def get_prefix(client, message):
    with open("prefixes/prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, help_command = None, case_insensitive = True, intents = intents)
################################################################################################################
@client.event
async def on_ready():
    print("Xi is ready to work!")
    await client.change_presence(activity=discord.Game(name=".help"))
################### COGS #############################################################################################

@client.command() 
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('.\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
################################################################################################################

async def get_bank_data():
    with open("economy/bank.json", 'r') as f:
        users = json.load(f)
    return users
        
async def update_bank(user, change = 0, mode = "Wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change
    with open("economy/bank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["Wallet"], users[str(user.id)]["Bank"]]
    return bal
################### WITHDRAW #############################################################################################
@client.command(aliases = ["with"])
async def withdraw(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send(embed = discord.Embed(description = "Podaj ilo????, kt??r?? chcesz wp??aci?? do banku!", color = ctx.author.color))
        return
    
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[1]:
        await ctx.send(embed = discord.Embed(description = "Nie masz wystarczaj??co pieni????k??w!", color = ctx.author.color))
        return
    if amount <= 0:
        await ctx.send(embed = discord.Embed(description = "Oszala??e???", color = ctx.author.color))
        return
    
    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1*amount, "Bank")

    await ctx.send(embed = discord.Embed(description = f"Wyp??aci??e?? z banku **{amount}$** monet.", color = ctx.author.color))

################### DEPOSIT #############################################################################################
@client.command(aliases = ["dep"])
async def deposit(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send(embed = discord.Embed(description = "Podaj ilo????, kt??r?? chcesz wp??aci?? do banku!", color = ctx.author.color))
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send(embed = discord.Embed(description = "Nie masz wystarczaj??co pieni????k??w!", color = ctx.author.color))
        return
    if amount <= 0:
        await ctx.send(embed = discord.Embed(description = "Oszala??e???", color = ctx.author.color))
        return
    
    await update_bank(ctx.author, -1*amount)
    await update_bank(ctx.author, amount, "Bank")

    await ctx.send(embed = discord.Embed(description = f"Wp??aci??e?? do banku **{amount}$** monet.", color = ctx.author.color))

################### GIVE #############################################################################################
@client.command(aliases = ["send", "pay"])
async def give(ctx, user: discord.Member = None, amount = None):
    if user == None:
        await ctx.send(embed = discord.Embed(description = "Pssst.. nie poda??e?? u??ytkownika, kt??remu chcesz podarowa?? pieni????ki!", color = ctx.author.color))
    else:        
        await open_account(ctx.author)
        await open_account(user)
        if amount == None:
            await ctx.send("Podaj ile chcesz wplacic!")
            return
    
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("Nie masz tyle pieni??dzy!")
            return
        if amount < 0:
            await ctx.send("Warto???? nie moze byc na minusie!")
            return
    
        await update_bank(ctx.author, -1*amount, "Wallet")
        await update_bank(user, amount, "Wallet")

        await ctx.send(embed = discord.Embed(description = f"Wys??a??e?? **{amount}$** u??ytkownikowi {user.mention}", color = user.color))
##################### ADD MONEY############################################################################################
#@client.command(aliases = ["addcash", "moneyadd", "cashadd", "add-money", "money-add"])
#async def addmoney(ctx, user: discord.Member = None, mode = None, amount = None):
################### FORTUNE WHEEL #############################################################################################
@client.command(aliases = ["fw", "fwheel", "fortunew"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def fortunewheel(ctx):
    await open_account(ctx.author)
    users = await get_bank_data()

    reward = random.randrange(999)
    embed = discord.Embed(title = "Ko??o fortuny", description = f"Gratulacje! Ko??o fortuny wylosowa??o dla ciebie **{reward}$**!", color = ctx.author.color)
    embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

    await ctx.send(embed = embed)

    users[str(ctx.author.id)]["Wallet"] += reward
    with open("economy/bank.json", 'w') as f:
        json.dump(users, f)
################### ROB #############################################################################################
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def rob(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send(embed = discord.Embed(description = "Pssst.. nie poda??e?? u??ytkownika, kt??rego chcesz okra????!", color = ctx.author.color))
    else:
        await open_account(ctx.author)
        await open_account(user)
    
        bal = await update_bank(user)
    
        cash = random.randint(0, bal[0])

        await update_bank(ctx.author, cash)
        await update_bank(user, -1*cash)
        answers = [f"W??amuj??c si?? do domu {user.mention} okradasz **{cash}$**", f"Uda??o ci si?? napa???? {user.mention} i zgarniasz **{cash}$**", f"Przez chwil?? nieuwagi {user.mention} kradniesz **{cash}$**", f"Hakujesz konto bankowe {user.mention} i zgarniasz **{cash}$**"]
        await ctx.send(embed = discord.Embed(description = random.choice(answers), color = user.color))

################################################################################################################
async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 0
        users[str(user.id)]["Bank"] = 0
    with open("economy/bank.json", 'w') as f:
        json.dump(users, f)
    return True

################### BAL #############################################################################################
@client.command(aliases = ['bal', 'cash', 'money'])
async def balance(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        await open_account(ctx.author) 
        users = await get_bank_data()

        wallet = users[str(user.id)]["Wallet"]
        bank = users[str(user.id)]["Bank"]

        embed = discord.Embed(title = "Stan konta", description = "Wy??wietla stan konta zar??wno jak i w portfelu, jak i w banku.", color = ctx.author.color)
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = ctx.author.avatar_url),
        embed.add_field(name="W portfelu:", value = f"{wallet}$", inline = False)
        embed.add_field(name="W banku:", value = f"{bank}$", inline = False)
        await ctx.send(embed = embed)
    else:
        await open_account(user)
        users = await get_bank_data()

        wallet = users[str(user.id)]["Wallet"]
        bank = users[str(user.id)]["Bank"]

        embed = discord.Embed(title = "Stan konta", description = "Wy??wietla stan konta zar??wno jak i w portfelu, jak i w banku.", color = user.color)
        embed.set_footer(text = user, icon_url = user.avatar_url)
        embed.set_thumbnail(url = user.avatar_url),
        embed.add_field(name="W portfelu:", value = f"{wallet}$", inline = False)
        embed.add_field(name="W banku:", value = f"{bank}$", inline = False)
        await ctx.send(embed = embed)

################### WORK #############################################################################################
@client.command(aliases = ['earn', 'earnmoney'])
@commands.cooldown(1, 30, commands.BucketType.user)
async def work(ctx):
    user = ctx.author
    await open_account(ctx.author)
    users = await get_bank_data()
    cash = random.randrange(101)

    answers = [f"Pracuj??c w ??abce zarabiasz **{cash}$**.", f"Za pomoc starszej pani otrzymujesz **{cash}$**. Tak trzymaj!", f"Sprzedaj??c ciuchy na Vinted otrzymujesz **{cash}$**.", f"Otrzymujesz premi??, kt??ra wynosi **{cash}$**.", f"Za skoszenie trawy dostajesz **{cash}$** kieszonkowego."]

    embed = discord.Embed(title = "Praca", description = random.choice(answers), color = ctx.author.color)
    embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)

    await ctx.send(embed = embed)

    users[str(user.id)]["Wallet"] += cash
    with open("economy/bank.json", 'w') as f:
        json.dump(users, f)
################### ECONOMY LEADERBOARD #############################################################################################
@client.command(aliases = ['lb'])
async def leaderboard(ctx, x = 3):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["Wallet"] + users[user]["Bank"]
        leader_board[total_amount] = name
        total.append(total_amount)
    
    total = sorted(total, reverse = True)

    embed = discord.Embed(title = f"Top {x} najbogatszych u??ytkownik??w", description = f"Tabela, kt??ra pokazuje **{x}** u??ytkownik??w z najwieksz?? ilo??ci?? punkt??w reputacji.", color = ctx.author.color)
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        embed.add_field(name = f"{index}. {name}", value = f"{amt}$", inline = False)
        if index == x:
            break
        else:
            index += 1
        
    await ctx.send(embed = embed)







################### REPUTATION SYSTEM #############################################################################################
async def get_rep_data():
    with open("reputations/reps.json", 'r') as f:
        users = json.load(f)
    return users
################################################################################################################
async def open_rep_account(user):
    users = await get_rep_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["reps"] = 0
    with open("reputations/reps.json", 'w') as f:
        json.dump(users, f)
    return True
################################################################################################################
async def update_reps(user, change = 0, mode = "reps"):
    users = await get_rep_data()

    users[str(user.id)][mode] += change
    with open("reputations/reps.json", "w") as f:
        json.dump(users, f)

    bal = users[str(user.id)]["reps"]
    return bal
################### REPGIVE #############################################################################################
@client.command(aliases = ["rep", "addrep", "repadd", "giverep", "repgive"])
async def reputation(ctx, user: discord.Member = None, amount = 1):
    if user == None:
        await ctx.send(embed = discord.Embed(description = "Pssst.. nie poda??e?? u??ytkownika, kt??remu chcesz przyzna?? punkt reputacji!", color = ctx.author.color))
    if user == ctx.author:
        await ctx.send("Nie mo??esz da?? reputacji samemu sobie!")
    else:        
        await open_rep_account(user)
    
        reps = await update_reps(user)
    
        await update_reps(user, amount, "reps")

        await ctx.send(embed = discord.Embed(description = f"Przynza??e?? **punkt reputacji** u??ytkownikowi {user.mention}", color = user.color))
################### REPLIST #############################################################################################
@client.command(aliases = ['listrep', 'checkrep', 'reps'])
async def replist(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        await open_rep_account(ctx.author) 
        users = await get_rep_data()

        reps = users[str(user.id)]["reps"]

        embed = discord.Embed(title = "Twoje punkty reputacji", description = f"Posiadasz **{reps}** punkty reputacji", color = ctx.author.color)
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = ctx.author.avatar_url),
        await ctx.send(embed = embed)
    else:
        await open_rep_account(user) 
        users = await get_rep_data()

        reps = users[str(user.id)]["reps"]

        embed = discord.Embed(title = f"Punkty reputacji {user.name}", description = f"U??ytkownik {user.mention} posiada **{reps}** punkty reputacji", color = user.color)
        embed.set_footer(text = user, icon_url = user.avatar_url)
        embed.set_thumbnail(url = user.avatar_url),
        await ctx.send(embed = embed)


@client.command(aliases = ['replb', 'lbrep'])
async def repleaderboard(ctx, x = 3):
    users = await get_rep_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["reps"]
        leader_board[total_amount] = name
        total.append(total_amount)
    
    total = sorted(total, reverse = True)

    embed = discord.Embed(title = f"Top {x} najbogatszych u??ytkownik??w", description = f"Tabela, kt??ra pokazuje **{x}** u??ytkownik??w z najwieksz?? ilo??ci?? punkt??w reputacji.", color = ctx.author.color)
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        embed.add_field(name = f"{index}. {name}", value = f"{amt} punkt??w reputacji", inline = False)
        if index == x:
            break
        else:
            index += 1
        
    await ctx.send(embed = embed)





################### PREFIXES #############################################################################################
@client.event 
async def on_guild_join(guild):
    with open("prefixes/prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."

    with open("prefixes/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent = 4)

@client.command(aliases = ["prefix", "setprefix", "changeprefix", "prefixchange"])
@commands.has_permissions(administrator = True)
async def prefixset(ctx, prefix = None):
    if prefix == None:
        await ctx.send("Podaj jaki chcesz ustawic prefix!")
    else:
        with open("prefixes/prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent = 4)
        
        await ctx.send(f"Prefix serwera zosta?? ustawiony jako **{prefix}**")

@client.event
async def on_message(msg):
    try:
        if msg.mentions[0] == client.user:
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)
            pre = prefixes[str(msg.guild.id)]

            await msg.channel.send(f"Prefix na tym serwerze to **{pre}**")
    except:
        pass
    await client.process_commands(msg)







################### WARNS #############################################################################################
async def get_warn_data():
    with open("warns/warns.json", 'r') as f:
        users = json.load(f)
    return users
        
async def update_warns(user, change = 0, mode = "warns"):
    users = await get_warn_data()

    users[str(user.id)][mode] += change
    with open("warns/warns.json", "w") as f:
        json.dump(users, f)

    amount = users[str(user.id)]["warns"]
    return amount

async def open_warn_account(user):
    users = await get_warn_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["warns"] = 0
    with open("warns/warns.json", 'w') as f:
        json.dump(users, f)
    return True

################### WARN COMMAND############################################################################################
@client.command(aliases = ["givewarn", "warngive"])
async def warn(ctx, user: discord.Member = None, *, reason = None, amount = 1):
    if user == ctx.author:
        await ctx.send("Nie mo??esz nada?? ostrze??enia samemu sobie!")
    if user and reason:    
        await open_warn_account(user)
        warns = await update_warns(user)
        await update_warns(user, amount, "warns")

        await ctx.send(embed = discord.Embed(description = f"U??ytkownik {user.mention} otrzyma?? ostrze??enie od {ctx.author.mention} za **{reason}**.", color = user.color))
    else:
        await ctx.send(embed = discord.Embed(description = "Poprawne u??ycie: .warn <@wzmianka> <pow??d>", color = ctx.author.color))
################### WARNLIST ############################################################################################
@client.command(aliases = ["listwarn", "warns"])
async def warnlist(ctx, user: discord.Member = None):
    if user == None:
        await ctx.send("Poprawne u??ycie: .warns <@wzmianka>")
    else:
        await open_warn_account(user) 
        users = await get_warn_data()

        warns = users[str(user.id)]["warns"]

        embed = discord.Embed(title = f"Ostrze??enia {user.name}", description = f"{user.mention} posiada **{warns}** ostrze??e??.", color = user.color)
        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = user.avatar_url),
        await ctx.send(embed = embed)
################### UNWARN ############################################################################################
@client.command(aliases = ["delwarn", "warndel"])
async def unwarn(ctx, user: discord.Member = None, amount = -1):
    if user == None:
        await ctx.send(embed = discord.Embed(description = "Poprawne u??ycie: .unwarn <@wzmianka>", color = ctx.author.color))
    if user == ctx.author:
        await ctx.send("Nie mo??esz usun???? ostrze??enia samemu sobie!")
    else:        
        await open_warn_account(user)
        warns = await update_warns(user)
        await update_warns(user, amount, "warns")

        await ctx.send(embed = discord.Embed(description = f"Jedno z ostrze??e?? u??ytkownika {user.mention} zosta??o usuni??te.", color = user.color))
################### ERRORS ############################################################################################
@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title=f"Zwolnij!", description = f"Spr??buj ponownie za **{error.retry_after:.0f}s**.", color = ctx.author.color)
        await ctx.send(embed = embed)

@rob.error
async def rob_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title=f"Zwolnij!", description = f"Spr??buj ponownie za **{error.retry_after:.0f}s**.", color = ctx.author.color)
        await ctx.send(embed = embed)

@fortunewheel.error
async def fortunewheel_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title=f"Zwolnij!", description = f"Spr??buj ponownie za **{error.retry_after:.0f}s**.", color = ctx.author.color)
        await ctx.send(embed = embed)
####################################################################################################
client.run('OTA5NTA2Njc3NDI5MTIxMDY0.YZFSGQ.68IkozJoQoE-GEZJInFf4wxp6z8')