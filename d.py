import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(activity=discord.Activity(type=discord.ActivityType.watching, name='the world get smarter'),intents=intents)

def ask(question,ids=None,isvariant=False):
	if ids and len(ids)==4:
		if isvariant:
			pdata={'question':question,'parent_message_id':ids[2],'_id':ids[3],'conversation_id':ids[0]}
		else:
			pdata={'question':question,'parent_message_id':ids[1],'_id':None,'conversation_id':ids[0]}
	else:
		pdata={'question':question,'parent_message_id':None,'_id':None,'conversation_id':None}
	r=requests.post('http://127.0.01:88/ask',data=pdata)
	return r.content.decode()

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.slash_command(description="Ask the AI.")
async def ask(ctx,question):
	print(question)
	embed = discord.Embed(title="{} asked the bot".format(ctx.author.name),description="", color=0xFF0000)
	embed.add_field(name='question',value=question,inline=True)
	await ctx.send(api.ask(question),embed = embed)

if __name__ == "__main__":
	bot.run('<YOUR BOT TOKEN>')