import asyncio

import twitchio
from PySide2.QtWidgets import QMainWindow
from twitchio.ext import commands


class Bot(commands.Bot):
    def __init__(self, parent_window: QMainWindow):
        # Initialise our Bot with our access token, prefix
        # and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...

        self.parent_window = parent_window

        with open("H:/login_data.txt", mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            irc_token = lines[4].strip()

        super().__init__(token=irc_token, prefix="!", initial_channels=["tutorexilius"])

        self.player_1: None | str = None
        self.player_2: None | str = None

        self.loop = asyncio.get_event_loop()
        self.running_game = False

    async def send_message(self, message: str) -> None:
        chan = self.get_channel("tutorexilius")
        self.loop.create_task(chan.send(message))

    async def event_ready(self) -> None:
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    async def event_message(self, message: twitchio.Message) -> None:
        if message is None or message.author is None or not message.content:
            return

        name = message.author.name
        msg = message.content

        if name in ["thomas485", "tutorexilius", "tutorexiliusbot"] and msg == "reset":
            self.player_1 = None
            self.player_2 = None
            self.running_game = False
            self.parent_window.label_player_1_name.setText("Player 1")
            self.parent_window.label_player_2_name.setText("Player 2")
            self.parent_window.game_finished(force_finish=True)
            await self.send_message("Game resetted by moderator")
            return

        if self.player_1 is None and msg == "!p1" and name != self.player_2:
            self.player_1 = name
            await self.send_message(f"{name} is player 1")

        if self.player_2 is None and msg == "!p2" and name != self.player_1:
            self.player_2 = name
            await self.send_message(f"{name} is player 2")

        if (
            not self.running_game
            and self.player_1 is not None
            and self.player_2 is not None
        ):
            self.parent_window.label_player_1_name.setText(self.player_1)
            self.parent_window.label_player_2_name.setText(self.player_2)
            self.parent_window.pushButton_start_game.animateClick()

            self.running_game = True
            await self.send_message(
                f"Game started. @{self.player_1}, @{self.player_2}: "
                "send a cup number (1-6) to make your turn."
            )
        elif self.running_game:
            player_actions = {
                self.player_1: {
                    "1": self.parent_window.pushButton_player_1_cup_1.animateClick,
                    "2": self.parent_window.pushButton_player_1_cup_2.animateClick,
                    "3": self.parent_window.pushButton_player_1_cup_3.animateClick,
                    "4": self.parent_window.pushButton_player_1_cup_4.animateClick,
                    "5": self.parent_window.pushButton_player_1_cup_5.animateClick,
                    "6": self.parent_window.pushButton_player_1_cup_6.animateClick,
                },
                self.player_2: {
                    "1": self.parent_window.pushButton_player_2_cup_1.animateClick,
                    "2": self.parent_window.pushButton_player_2_cup_2.animateClick,
                    "3": self.parent_window.pushButton_player_2_cup_3.animateClick,
                    "4": self.parent_window.pushButton_player_2_cup_4.animateClick,
                    "5": self.parent_window.pushButton_player_2_cup_5.animateClick,
                    "6": self.parent_window.pushButton_player_2_cup_6.animateClick,
                },
            }

            if name not in player_actions.keys():
                return

            player_actions[name][msg]()
