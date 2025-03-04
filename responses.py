from random import choice, randint

# Main bosses with short responses
BOSS_RESPONSES = {
    "Margit": "Fell Omen, vanquished. ",
    "Godrick": "The Grafted is no more.",
    "Rennala": "Queen of the Full Moon fades.",
    "Radahn": "Stars resume their course.",
    "Morgott": "The Veiled Monarch falls.",
    "Fire Giant": "The flame awaits.",
    "Maliketh": "Destined Death returns.",
    "Gideon": "All-Knowing, silenced.",
    "Godfrey": "First Lord, bested.",
    "Radagon": "The hammer shatters.",
    "Elden Beast": "You are Elden Lord.",
}

# giving credit or append
Giving_credit = [
    "Good, job",
    "Well done",
    "Tho strenght befits a crown Tarnished",
    "Impressive",
]


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    # Basic interactions
    if lowered in ["hello", "hi"]:
        return "Greetings, Tarnished."
    elif lowered in ["how are you", "are you there"]:
        return "I am here, as promised.", "I am good, thank you tarnished."
    elif lowered in ["goodbye", "farewell"]:
        return "May your path be clear."
    elif lowered in ["Roll dice"]:
        return f"You rolled a {randint(1, 6)}. Fortune favors you."
    elif "tarnished arrived" in lowered:
        return "Welcome, Tarnished, to the Lands Between."

    # Boss defeat responses
    for boss in BOSS_RESPONSES.keys():
        if f"i have defeated {boss.lower()}" in lowered:
            return f"{BOSS_RESPONSES[boss]} {choice(Giving_credit)}"

    # Default/Fallback responses for unrecognized input
    return choice(
        [
            "I do not understand, Tarnished.",
            "Your words are shrouded in fog. Be clear.",
            "Be more clear, Tarnished.",
            "uncertain..., Thy skill in writing is lost.",
            "What do you seek, Tarnished?",
        ]
    )
