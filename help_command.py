import discord
from discord.ext import commands

intents=discord.Intents.all()
intents.members=True
bot=commands.AutoShardedBot(command_prefix="!",description="WORKING WITH SMF",intents=intents)

@bot.event
async def on_ready():
    print("the bot is ready to perform ! ! !")

bot.remove_command('help')

@bot.command(aliases=[],description="Bot ping check")
async def ping(ctx):
    await ctx.send(f'Pong! In {round(bot.latency * 1000)}ms')

@bot.command(aliases=[],description="Hello reply")
async def hello(ctx):
    await ctx.send("hi")

@bot.command(aliases=['commands'],description="List of commands")
async def help(ctx):
    embed=discord.Embed(title="List of Bot commands",description=f"use  {bot.command_prefix} as command prefix",color=discord.Colour.dark_orange(),type='rich')
    for cmd in bot.commands:
        params=["ctx"]
        for i in cmd.params:
            params.append(i)
        if cmd.aliases==[]:
            val=f"Description : {cmd.description}\n params : {params}"
        else:
            val=f"Description : {cmd.description}\n aliase cmd : {cmd.aliases} \n params : {params}"
        embed.add_field(name=cmd,value=val,inline=True)
    await ctx.send(embed=embed)

bot.run("bot-token",reconnect=True)
