import discord
import random

client = discord.Client()

quotes = ["If it's all the same to you, I'll have that drink now.", "I am burdened with glorious purpose.",
          "Kneel before me. I said... KNEEELLL!", " I'll split his skull! This is MY bargain, you mewling quim!",
          "Well done, you just decapitated your grandfather!", "Your savior is here!",
          "You will...never be ... a god", "Oh I do, kill away", "Hitting does not solve everything",
          "We are NOT doing Get Help", "Scared of a little lightning?I'm not overly fond of what follows",
          "You were made to be ruled. In the end, you will always kneel", "God bless Americ--!",
          "So tight, but the confidence!I can feel the righteousness surging!", "This usually works...."]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    server = message.guild
    """copy user's roles, id pic, username"""
    roles = []
    old_name = message.author.name
    members = server.members[:]
    shifted = False
    for i in message.author.roles:
        roles.append(i.name)
        print(roles)
    if message.content.startswith('!mischief'):
        """changes person user, roles with random person in the server"""

        memb = random.choice(server.members)
        print(memb)
        print(old_name)
        new_name = str(memb.name)
        print(new_name)
        shifted = True
        await message.author.edit(nick=new_name)

    if message.content.startswith('!brother'):
        """sends out a loki quote from list"""
        await message.channel.send(random.choice(quotes))
    if message.content.startswith('!shift'):
        """changes person user,roles back to normal"""
        if shifted == True:
            await message.author.edit(nick=old_name)
        else:
            await message.channel.send("I, Loki, Prince of Asgard, Odinson, "
                                       "the rightful King of Jotunheim, God of Mischief, do hereby pledge to you, my undying fidelity.")
            shifted = False
"""async def member_info(memb,id_num,channel):
    for i in range(len(memb)):
        if memb[i].id == id_num:
            return memb.nick
        if memb[i].id == 733559714817769532:
            await channel.send("This usually works....")"""


client.run("NzMzNTU5NzE0ODE3NzY5NTMy.XxHVpg.vh5P4gYShV6hk8pQri_aZ-xrSWQ")
