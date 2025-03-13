import os
import asyncio
import random
import discord
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Interaction, Message, app_commands
from discord.ext import commands

# Load environment variables
load_dotenv(override=True)
TOKEN: Final = os.getenv("DISCORD_TOKEN")

# Configure bot intents
intents = Intents.default()
intents.message_content = True

# Initialize bot with a command prefix and disable the default help command
bot = commands.Bot(command_prefix="m!", intents=intents, help_command=None)

# Constants for boss responses and credits
BOSS_RESPONSES = {
    "margit": "Fell Omen, vanquished.",
    "godrick": "The Grafted is no more.",
    "rennala": "Queen of the Full Moon fades.",
    "radahn": "Stars resume their course.",
    "morgott": "The Veiled Monarch falls.",
    "firegiant": "The flame awaits.",
    "godskinduo": "The duo falls silent.",
    "maliketh": "Destined Death returns.",
    "gideon": "All-Knowing, silenced.",
    "godfrey": "First Lord, bested.",
    "radabeast": "The hammer shatters. You are Elden Lord.",
    "DBDL": "The Divine Dancing Lion rests.",
    "rellana": "The protector returns to slumber.",
    "goldenhippo": "The Golden Hippopotamus sinks beneath the waters.",
    "messmer": "Messmer's light fades to darkness.",
    "gaius": "Gaius, the Golden Knight, falls.",
    "scadutree": "The Avatar withers and crumbles.",
    "putrescent": "The Putrescent Knight's corruption is cleansed.",
    "midra": "Midra's final flame extinguished.",
    "bayle": "Bayle's strength was not enough.",
    "metyr": "Metyr returns to the shadows.",
    "romina": "Romina's final song ends.",
    "leda": "The Needle Knight's precision falters.",
    "pcr": "The Promised Consort falls beneath your might."
}

GIVING_CREDIT = [
    "Well done, Tarnished.",
    "You have my gratitude.",
    "A fine display of strength.",
    "You walk with purpose.",
    "May your path be ever guided.",
    "You are worthy.",
    "Your resolve is strong.",
    "Grace is with you.",
    "I acknowledge your strength.",
    "You have done well."
]

# Event: Bot is ready
@bot.event
async def on_ready():
    """Handles bot readiness and syncs application commands."""
    try:
        await bot.tree.sync()
        print(f"Bot is logged in as {bot.user} and ready!")
        print(f"Connected to {len(bot.guilds)} guild(s): {[guild.name for guild in bot.guilds]}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Event: Log messages and process commands
@bot.event
async def on_message(message: Message):
    """Logs user messages and processes commands."""
    if message.author == bot.user:
        return
    print(f"[{message.channel}] {message.author}: {message.content}")
    await bot.process_commands(message)

# Command: Greet the user
@bot.tree.command(name="greet", description="Receive greetings from Melina.")
async def greet(interaction: Interaction):
    """Sends a greeting message."""
    await interaction.response.send_message(f"Greetings, {interaction.user.mention}. The Lands Between welcome you.")

# Command: How are you?
@bot.tree.command(name="how_are_you", description="Ask Melina how her day is.")
async def how_are_you(interaction: Interaction):
    """Responds with Melina's current state."""
    await interaction.response.send_message("I am doing well, thank you for asking, Tarnished.")

# Command: Are you there?
@bot.tree.command(name="are_you_there", description="Check if Melina is with you.")
async def are_you_there(interaction: Interaction):
    """Confirms Melina's presence."""
    await interaction.response.send_message("I am here, always with you, Tarnished.")

# Command: Farewell message
@bot.tree.command(name="farewell", description="Bid farewell to Melina.")
async def farewell(interaction: Interaction):
    """Sends a farewell message."""
    await interaction.response.send_message("May your path be clear, Tarnished. Farewell.")

# Command: Report defeated boss
@bot.tree.command(name="i_have_defeated", description="Tell Melina which boss you have bested.")
@app_commands.describe(bosses="Which boss is it that you have bested?")
@app_commands.choices(bosses=[
    app_commands.Choice(name="Margit", value="margit"),
    app_commands.Choice(name="Godrick", value="godrick"),
    app_commands.Choice(name="Rennala", value="rennala"),
    app_commands.Choice(name="Radahn", value="radahn"),
    app_commands.Choice(name="Morgott", value="morgott"),
    app_commands.Choice(name="Fire Giant", value="firegiant"),
    app_commands.Choice(name="God Skin Duo", value="godskinduo"),
    app_commands.Choice(name="Maliketh", value="maliketh"),
    app_commands.Choice(name="Gideon", value="gideon"),
    app_commands.Choice(name="Godfrey", value="godfrey"),
    app_commands.Choice(name="Radagon and Elden Beast", value="radabeast"),
    app_commands.Choice(name="Divine Beast Dancing Lion", value="DBDL"),
    app_commands.Choice(name="Rellana", value="rellana"),
    app_commands.Choice(name="Golden Hippopotamus", value="goldenhippo"),
    app_commands.Choice(name="Messmer", value="messmer"),
    app_commands.Choice(name="Gaius", value="gaius"),
    app_commands.Choice(name="Scadutree Avatar", value="scadutree"),
    app_commands.Choice(name="Putrescent Knight", value="putrescent"),
    app_commands.Choice(name="Midra", value="midra"),
    app_commands.Choice(name="Bayle", value="bayle"),
    app_commands.Choice(name="Metyr", value="metyr"),
    app_commands.Choice(name="Romina", value="romina"),
    app_commands.Choice(name="Needle Knight Leda", value="leda"),
    app_commands.Choice(name="Promised Consort Radahn", value="pcr")
])
async def defeated_bosses(interaction: Interaction, bosses: str):
    """Responds to boss defeats with acknowledgment."""
    boss_response = BOSS_RESPONSES.get(bosses, "A worthy opponent has fallen.")
    credit_message = random.choice(GIVING_CREDIT)
    await interaction.response.send_message(f"{boss_response} {credit_message}")

# Command: Roll a dice
@bot.tree.command(name="roll_dice", description="Roll a dice and test your fortune.")
async def roll_dice(interaction: Interaction):
    """Rolls a six-sided dice and returns the result."""
    result = random.randint(1, 6)
    await interaction.response.send_message(f"You rolled a {result}. Fortune smiles upon you!")

# Command:  command showcase
@bot.tree.command(name="help", description="Shows every command for melina.")
async def help(interaction: Interaction):
    showcase = bot.tree.command()
    await interaction.response.send_message(showcase)


# Main entry point
async def main():
    """Launches the bot."""
    try:
        print("Launching Melina bot...")
        await bot.start(TOKEN)
    except discord.errors.LoginFailure:
        print("Error: Invalid token. Please check your DISCORD_TOKEN in the .env file.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        await bot.close()

# Run the bot
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot shutdown gracefully by user.")
    except Exception as e:
        print(f"Fatal error: {e}")
