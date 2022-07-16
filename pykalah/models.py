"""The game classes"""
import random
import time
from enum import IntEnum, auto
from itertools import cycle
from pathlib import Path

from PySide2.QtCore import QObject, Signal
from PySide2.QtMultimedia import QSound
from PySide2.QtWidgets import QApplication, QPushButton


class PlayerType(IntEnum):
    PLAYER_1 = auto()
    PLAYER_2 = auto()


class CupType(IntEnum):
    KALAH = auto()
    CUP = auto()


class StateType(IntEnum):
    CUP_PIECE_INSERT = auto()
    LAST_IN_EMPTY_CUP = auto()
    LAST_IN_KHALA = auto()
    FINISHED_WITH_DRAW = auto()
    FINISHED_WITH_PLAYER_1_WON = auto()
    FINISHED_WITH_PLAYER_2_WON = auto()
    GAME_CONTINUE = auto()
    GAME_CLOSE = auto()


class SoundManager(QObject):
    def __init__(self):
        super(SoundManager, self).__init__()

        self.registered_signals = []

        self.qsound_collections = {
            StateType.CUP_PIECE_INSERT: [
                QSound(str(Path(__file__).parent / "sounds" / f"cup_insert_1.wav")),
                QSound(str(Path(__file__).parent / "sounds" / f"cup_insert_2.wav")),
            ],
            StateType.LAST_IN_EMPTY_CUP: [
                QSound(
                    str(Path(__file__).parent / "sounds" / f"last_in_empty_cup_1.wav")
                ),
                QSound(
                    str(Path(__file__).parent / "sounds" / f"last_in_empty_cup_2.wav")
                ),
            ],
            StateType.LAST_IN_KHALA: [
                QSound(
                    str(Path(__file__).parent / "sounds" / f"last_in_kalah_sound_1.wav")
                ),
            ],
            StateType.FINISHED_WITH_PLAYER_1_WON: [
                QSound(
                    str(
                        Path(__file__).parent
                        / "sounds"
                        / f"finished_with_winner_sound_1.wav"
                    )
                ),
            ],
            StateType.FINISHED_WITH_PLAYER_2_WON: [
                QSound(
                    str(
                        Path(__file__).parent
                        / "sounds"
                        / f"finished_with_winner_sound_1.wav"
                    )
                ),
            ],
            StateType.FINISHED_WITH_DRAW: [
                QSound(
                    str(
                        Path(__file__).parent
                        / "sounds"
                        / f"finished_with_draw_sound_1.wav"
                    )
                ),
            ],
            StateType.GAME_CLOSE: [
                QSound(str(Path(__file__).parent / "sounds" / f"bye.wav")),
            ],
        }

    def register(self, signal: Signal):
        if signal not in self.registered_signals:
            signal.connect(self._play)
            self.registered_signals.append(signal)

    def _play(self, state: StateType):
        if state in self.qsound_collections:
            qsound = random.choice(self.qsound_collections[state])
            qsound.play()
            print("Play sound:", qsound.fileName())


class CupModel:
    """The init method of the Cup class.

    :param associated_button: The binding object in UI, here a QPushButton.
    :param pieces: The initail amount of pieces in the Cup.
    """

    def __init__(
        self,
        id: int,
        cup_type: CupType = CupType.CUP,
        pieces: int = 0,
    ):
        self.id = id
        self.cup_type = cup_type
        self._pieces = pieces

    # use @property (get/set) for pieces attribute, needed for databinding in related CupViewModel
    @property
    def pieces(self) -> int:
        return self._pieces

    @pieces.setter
    def pieces(self, value: int) -> None:
        self._pieces = value


class GameBoardModel:
    """GameBoardModel"""

    def __init__(self, initial_amount_pieces: int):
        # Player 1: [0], Player 2: [1]
        self.kalahs = [
            CupModel(id=i, pieces=0, cup_type=CupType.KALAH) for i in [100, 101]
        ]

        # Player 1: [:6] -> cups 0-5
        # Player 2: [6:] -> cups 6-11
        self.cups = [
            CupModel(id=i, pieces=initial_amount_pieces, cup_type=CupType.CUP)
            for i in range(12)
        ]

    def get_player_cups(self, player_type: PlayerType) -> list[CupModel]:
        player_1_cups = self.cups[:6]
        player_2_cups = self.cups[6:]
        player_1_kalah = [self.kalahs[0]]
        player_2_kalah = [self.kalahs[1]]

        if player_type == PlayerType.PLAYER_1:
            return player_1_cups + player_1_kalah + player_2_cups
        else:
            return player_2_cups + player_2_kalah + player_1_cups

    def get_player_counterpart_cup_map(
        self, player_type: PlayerType
    ) -> dict[CupModel, CupModel]:
        player_1_map = {
            self.cups[0]: self.cups[11],
            self.cups[1]: self.cups[10],
            self.cups[2]: self.cups[9],
            self.cups[3]: self.cups[8],
            self.cups[4]: self.cups[7],
            self.cups[5]: self.cups[6],
        }

        if player_type == PlayerType.PLAYER_1:
            return player_1_map
        else:
            return {value: key for key, value in player_1_map.items()}


class PlayerModel(QObject):
    animate_button = Signal(QPushButton, bool, bool)
    finish_animation = Signal()
    game_action_done = Signal(StateType)

    def __init__(
        self,
        game_board: GameBoardModel,
        player_type: PlayerType,
        sound_manager: SoundManager,
    ):
        super(PlayerModel, self).__init__()

        self.sound_manager = sound_manager
        self.sound_manager.register(self.game_action_done)

        self.player_type = player_type
        self.game_board = game_board.get_player_cups(player_type)
        self.counterpart_cup_map = game_board.get_player_counterpart_cup_map(
            player_type
        )
        self.kalah_id = 0 if player_type == player_type.PLAYER_1 else 1
        self.cup_ids = (
            list(range(0, 6))
            if player_type == player_type.PLAYER_1
            else list(range(6, 12))
        )

    def distribute_pieces(self, cup_id: int, pieces: int) -> StateType:
        cups = cycle(self.game_board)

        old_button_styles = {}

        for cup in cups:
            if cup.id == cup_id:
                cup.pieces = 0

                if hasattr(cup, "_button"):
                    cup._button.setText(str(0))
                    self.animate_button.emit(cup._button, True, False)

                for _ in range(pieces):

                    next_cup = next(cups)
                    is_kalah = next_cup.cup_type == CupType.KALAH
                    next_cup.pieces += 1

                    if hasattr(next_cup, "_button"):
                        next_cup._button.setText(str(next_cup.pieces))

                        self.game_action_done.emit(StateType.CUP_PIECE_INSERT)
                        self.animate_button.emit(next_cup._button, False, is_kalah)

                    last_cup = next_cup
                    QApplication.processEvents()

                    time.sleep(0.2)

                result = self._check_rule(last_cup)
                break

        self.finish_animation.emit()
        QApplication.processEvents()

        return result

    def _check_rule(self, last_cup: CupModel) -> StateType:
        state = StateType.GAME_CONTINUE

        if last_cup.id in [100, 101]:
            state = StateType.LAST_IN_KHALA
        elif last_cup.pieces == 1 and last_cup.id in self.cup_ids:

            counterpart_pieces = self.counterpart_cup_map[last_cup].pieces

            if counterpart_pieces == 0:
                # leave function here !
                return state

            self.counterpart_cup_map[last_cup].pieces = 0
            if hasattr(self.counterpart_cup_map[last_cup], "_button"):
                self.counterpart_cup_map[last_cup]._button.setText(str(0))

            pieces = last_cup.pieces
            last_cup.pieces = 0
            if hasattr(last_cup, "_button"):
                last_cup._button.setText(str(0))

            self.game_board[6].pieces += counterpart_pieces + pieces  # players kalah
            if hasattr(self.game_board[6], "_button"):
                self.game_board[6]._button.setText(str(self.game_board[6].pieces))

            state = StateType.LAST_IN_EMPTY_CUP

        return state


class GameModel(QObject):
    """Game"""

    game_action_done = Signal(StateType)

    def __init__(self, initial_amount_pieces: int, sound_manager: SoundManager):
        super(GameModel, self).__init__()

        self.sound_manager = sound_manager
        self.sound_manager.register(self.game_action_done)

        self.game_board = GameBoardModel(initial_amount_pieces)
        self._player_1 = None
        self._player_2 = None
        self._current_turn = None
        self._backuped_cup_styles = None

    def initialize_player(self) -> None:
        self._player_1 = PlayerModel(
            self.game_board, PlayerType.PLAYER_1, self.sound_manager
        )
        self._player_2 = PlayerModel(
            self.game_board, PlayerType.PLAYER_2, self.sound_manager
        )
        self._current_turn = self._player_1

        self._player_1.animate_button.connect(self.inserting_piece_animation)
        self._player_1.finish_animation.connect(self.finish_animation)

        self._player_2.animate_button.connect(self.inserting_piece_animation)
        self._player_2.finish_animation.connect(self.finish_animation)

        self._backuped_cup_styles = {}

    def inserting_piece_animation(
        self, cup_button: QPushButton, is_start_cup, is_kalah
    ):
        print(cup_button.objectName(), " >> START" if is_start_cup else "")

        if cup_button not in self._backuped_cup_styles:
            self._backuped_cup_styles[cup_button] = cup_button.styleSheet()

        if is_start_cup:
            cup_button.setStyleSheet(
                """
                QPushButton{
                    border: 5px inset red;
                    background-color: #fff;
                    font-size: 24pt;
                    border-radius: 40px;
                }
                """
            )
        else:
            if is_kalah:
                cup_button.setStyleSheet(
                    """
                    QPushButton{
                        border: 5px inset #445677;
                        background-color: #fff;
                        font-size: 24pt;
                        border-radius: 15px;
                    }
                    """
                )
            else:
                cup_button.setStyleSheet(
                    """
                    QPushButton{
                        border: 5px inset #445677;
                        background-color: #fff;
                        font-size: 24pt;
                        border-radius: 40px;
                    }
                    """
                )

    def finish_animation(self):
        for button, style in self._backuped_cup_styles.items():
            button.setStyleSheet(style)

    def distribute_pieces(self, cup_data: dict[str, str | int]) -> StateType:
        if cup_data["cup_id"] not in self._current_turn.cup_ids:
            return StateType.GAME_CONTINUE

        state = self._current_turn.distribute_pieces(
            cup_id=cup_data["cup_id"], pieces=cup_data["pieces"]
        )

        if self._continue_game():
            if state != StateType.LAST_IN_KHALA:
                self._current_turn = (
                    self._player_2
                    if (self._current_turn is self._player_1)
                    else self._player_1
                )

            self.game_action_done.emit(state)

            print(self._current_turn.player_type)
            return StateType.GAME_CONTINUE
        else:
            if (
                self._player_1.game_board[6].pieces
                > self._player_2.game_board[6].pieces
            ):
                print("Player 1 Won")
                state = StateType.FINISHED_WITH_PLAYER_1_WON
            elif (
                self._player_1.game_board[6].pieces
                < self._player_2.game_board[6].pieces
            ):
                print("Player 2 Won")
                state = StateType.FINISHED_WITH_PLAYER_2_WON
            else:
                print("DRAW")
                state = StateType.FINISHED_WITH_DRAW

            self.game_action_done.emit(state)
            return state

    def _continue_game(self):
        # player_1_cups = (cup for cup in self.game_board.cups if cup.id in self._player_1.cup_ids)
        player_1_cups = [
            self.game_board.cups[cup_id] for cup_id in self._player_1.cup_ids
        ]

        # player_2_cups = (cup for cup in self.game_board.cups if cup.id in self._player_2.cup_ids)
        player_2_cups = [
            self.game_board.cups[cup_id] for cup_id in self._player_2.cup_ids
        ]

        if all(cup.pieces == 0 for cup in player_1_cups) or all(
            cup.pieces == 0 for cup in player_2_cups
        ):
            for cup in player_1_cups:
                self._player_1.game_board[6].pieces += cup.pieces
                cup.pieces = 0
                if hasattr(cup, "_button"):
                    cup._button.setText(str("0"))

            if hasattr(self._player_1.game_board[6], "_button"):
                self._player_1.game_board[6]._button.setText(
                    str(self._player_1.game_board[6].pieces)
                )

            for cup in player_2_cups:
                self._player_2.game_board[6].pieces += cup.pieces
                cup.pieces = 0
                if hasattr(cup, "_button"):
                    cup._button.setText(str("0"))

            if hasattr(self._player_2.game_board[6], "_button"):
                self._player_2.game_board[6]._button.setText(
                    str(self._player_2.game_board[6].pieces)
                )

            return False

        return True
