import random
import re

from src.discord_bot.helpers.command_logging import command_log


FACES: list = [
    '(・`ω´・)', ';;w;;', 'owo', 'UwU', '>w<', '^w^', '(* ^ ω ^)',
    '(⌒ω⌒)', 'ヽ(*・ω・)ﾉ', '(o´∀`o)', '(o･ω･o)', '＼(＾▽＾)／',
    '(*^ω^)', '(◕‿◕✿)', '(◕ᴥ◕)', 'ʕ•ᴥ•ʔ', 'ʕ￫ᴥ￩ʔ', '(*^.^*)', '(｡♥‿♥｡)',
    'OwO', 'uwu', 'uvu', 'UvU', '(*￣з￣)', '(つ✧ω✧)つ', '(/ =ω=)/',
    '(╯°□°）╯︵ ┻━┻', '┬─┬ ノ( ゜-゜ノ)', '¯\\_(ツ)_/¯'
]

OTHER: list = [
    "*giggles*", "*waises paw*", "OwO whats this?", "*unbuttons shirt*",
    "*blushes*", "*nuzzles*", "hehe", "heh", "murr~"
]

SPARKLE: str = "｡･:*:･ﾟ★,｡･:*:･ﾟ☆"

CHARACTERS: dict = {
    r"that": "dat",
    r"have": "hab",
    r"love": "wuv",
    r"mr.": "mistuh",
    r"cat": "catto",
    r"fuck": "fwick",
    r"shit": "shoot",
    r"friend": "fwend",
    r"stop": "stawp",
    r"dick": "peepee",
    r"penis": "peepee",
    r"mr": "mistuh",
    r"fuk": "fwick",
    r"god": "gosh",
    r"hello": "hewwo",
}


@command_log
def make_owoify(message: str | tuple[str]) -> str:
    message = " ".join(message)
    message = message.lower()

    for search_chars, replace_chars in CHARACTERS.items():
        message = re.sub(search_chars, replace_chars, message)

    message_parts = message.split()
    message = ""
    for word in message_parts:
        if word not in CHARACTERS.values():
            word = word.replace("r", "w")
            word = word.replace("o", "owo")
            word = word.replace("u", "uwu")
        message += f"{word} "

    if bool(random.getrandbits(1)):
        message = f"~ meowwww {message} "

    if bool(random.getrandbits(1)):
        message = f"{message} ❤️ "

    if bool(random.getrandbits(1)):
        message = f"{message} nyaaa ~ "

    if bool(random.getrandbits(1)):
        message = f"{random.choice(OTHER)} {message}"

    if bool(random.getrandbits(1)):
        message = f"{message} {random.choice(OTHER)} "

    if bool(random.getrandbits(1)):
        message = f"{random.choice(FACES)} {message} "

    if bool(random.getrandbits(1)):
        message = f"{message} {random.choice(FACES)} "
    
    if bool(random.getrandbits(1)):
        message = f"{message} {SPARKLE} "

    return message
