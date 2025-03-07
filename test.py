import os
import discord
from typing import Final
from discord.ext import commands
from discord import Intents, app_commands 
from dotenv import load_dotenv
from responses import get_response

# Loads the token from somewhere and Guild ID
load_dotenv(override=True)
TOKEN: Final = os.getenv("DISCORD_TOKEN")
GUILD_ID: Final = os.getenv("GUILD")

# bot setup, the basics
intents: Intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="m!", intents=intents)


# TEST 
# Prefix command
@bot.command
async def Hello(ctx):
    await ctx.send("Hello, Fellow member")



# Slash command 

@bot.tree.command(name="Hello", description=f"replys with Hello, Member")
async def slash_hello(interaction:discord.Interaction, ctx):
    user_name = ctx.author.display_name
    await interaction.response.send_message(f"Hello, {user_name}")

@bot.tree.command(name="hello", description="Replies with Hello using slash command!")
async def slash_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello with slash command! 👋")

# Sync slash commands when bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync slash commands globally
    print(f"Bot is online as {bot.user}")

# Run the bot
bot.run(TOKEN)






"""

# message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty, because intents were not enabled, probably)")
        return

    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        (
            await message.author.send(response)
            if is_private
            else await message.channel.send(response)
        )
    except Exception as e:
        print(e)


# Handling the startup for the App
@bot.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")


# Handling incoming messages
@bot.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    user_name: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    print(f'[{channel}] {user_name}: "{user_message}" ')
    await send_message(message, user_message)


# Main entry point
def main() -> None:
    client.run(TOKEN)


main()
"""