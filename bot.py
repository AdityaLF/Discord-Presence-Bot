import discord
from discord.ext import commands
import locale 

# --- Bot Setup ---
# Replace with your bot token
YOUR_BOT_TOKEN = 'bot_token_here'

intents = discord.Intents.default()
intents.presences = True
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """
    This event is called when the bot successfully connects to Discord.
    This is the ideal place to set the bot's status/activity.
    """
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    total_members = 0
    for guild in bot.guilds:

        total_members += guild.member_count
    
    total_servers = len(bot.guilds)
    
    formatted_members = f"{total_members:,}"
    formatted_servers = f"{total_servers:,}"
    
    activity_name = f"with {formatted_members} members in {formatted_servers} servers!" 
    
    stream_url = "https://www.youtube.com/watch?v=MYPVQccHhAQ"

    activity = discord.Streaming(name=activity_name, url=stream_url)

    await bot.change_presence(activity=activity)
    
    print(f"Bot activity set to: Streaming '{activity_name}' with URL: {stream_url}")
    print("Check your bot's profile in Discord to see the new activity.")

if __name__ == "__main__":
    bot.run(YOUR_BOT_TOKEN)