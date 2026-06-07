from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
from twitchAPI.helper import first
from twitchAPI.object.eventsub import ChannelFollowEvent
from twitchAPI.eventsub.websocket import EventSubWebsocket
import json
import pathlib
import asyncio
import subprocess
from colorama import Fore, Style


# Settings startup
with open("../common/twitch_app.json", "r", encoding="utf8") as jf:
    twitch_app = json.load(jf)

APP_ID = twitch_app["id"]
APP_SECRET = twitch_app["secret"]

USER_SCOPE = [AuthScope.MODERATOR_READ_FOLLOWERS]
USER_ID = "verdeitorres"

async def on_follow(data: ChannelFollowEvent):
    subprocess.run("notify-send -w -a Twitch -u critical 'NOVO SEGUIDOR'")
    print(f"{Fore.MAGENTA}{data.event.user_name}{Style.RESET_ALL} 💜")

    # Followers History - Follow Widget
    if pathlib.Path("../common/follow_history.json").exists():
        with open("../common/follow_history.json", "r", encoding="utf8") as jf:
            followers = json.load(jf)
    else:
        followers = []

    while len(followers) >= 10:
        followers.pop(0)

    followers.append(data.event.user_name)
    with open("../common/follow_history.json", "w", encoding="utf8") as jf:
        json.dump(followers, jf)

async def run():
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    user = await first(twitch.get_users())
    eventsub = EventSubWebsocket(twitch)

    eventsub.start()
    sub_id = await eventsub.listen_channel_follow_v2(user.id, user.id, on_follow)
    print(f"channel follow: {user.id} {sub_id}")


    subprocess.run("clear")
    try:
        input(f"{Fore.GREEN}[NOVOS SEGUIDORES DA TWITCH]{Style.RESET_ALL}\n")
    finally:
        await eventsub.stop()
        await twitch.close()


if __name__ == "__main__":
    asyncio.run(run())
