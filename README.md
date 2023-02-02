# discord-invite-getter
A script for easily retrieving Discord invite link information
# How to Use
## How to setup
Place discord-invite-getter.py in the same hierarchy as your main program file.
## Simple usage
```
import discord-invite-getter as dinvite

res = dinvite.get_invite(input("Enter Invite code : discord.gg/"))

print(res)
```
## Examples
```
import discord-invite-getter as dinvite
import json

#Get invite data
print(res.code)
print(res.type)
print(res.expires_at)
#Get guild data
print(res.guild.id)
print(res.guild.name)
print(res.guild.splash)
print(res.guild.banner)
print(res.guild.description)
print(res.guild.icon)
print(res.guild.verification_level)
print(res.guild.vanity_url_code)
print(res.guild.premium_subscription_count)
print(res.guild.welcome_screen.welcome_channels)
print(res.guild.welcome_screen.description)
#Get invite channel
print(res.channel.id)
print(res.channel.name)
print(res.channel.type)
#All data 
print(json.dumps(res , indent=4))
```
