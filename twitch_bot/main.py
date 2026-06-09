from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.chat import Chat, ChatMessage, EventData
import json
import pathlib
import asyncio
import subprocess
from colorama import Fore, Style
import shlex


# Settings startup
with open("../common/twitch_app.json", "r", encoding="utf8") as jf:
    twitch_app = json.load(jf)

APP_ID = twitch_app["id"]
APP_SECRET = twitch_app["secret"]

USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = "verdeitorres"

async def on_ready(ready_event: EventData):
    await ready_event.chat.join_room(TARGET_CHANNEL)

async def on_message(msg: ChatMessage):
    subprocess.run(shlex.split(f"notify-send -w -a Twitch -u critical 'NOVA MENSAGEM' '{msg.user.name}: {msg.text}'"))

    print(f"{Fore.MAGENTA}{msg.user.name}{Style.RESET_ALL}: {msg.text}")

    # Chat History <-> Chat Widget
    if pathlib.Path("../common/chat_history.json").exists():
        with open("../common/chat_history.json", "r", encoding="utf8") as f:
            lines = json.load(f)
    else:
        lines = []

    while len(lines) >= 10:
        lines.pop(0)

    lines.append([msg.user.name, msg.text])

    with open("../common/chat_history.json", "w", encoding="utf8") as f:
        json.dump(lines, f, indent=4)


async def run():
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    chat = await Chat(twitch)
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)

    chat.start()

    subprocess.run("clear")
    try:
        input(f"{Fore.YELLOW}[CHAT DA TWITCH]{Style.RESET_ALL}\n")
    finally:
        chat.stop()
        await twitch.close()


if __name__ == "__main__":
    asyncio.run(run())
