import threading
import chess
import chess.engine
import os


class Game(threading.Thread):
    def __init__(self, client, game_id, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.client = client
        self.stream = client.bots.stream_game_state(game_id)
        self.current_state = next(self.stream)
        self.engine = self.get_engine()
        self.engine_depth_level = 1

    def run(self):
        self.check_first_move()
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)
            else:
                print('Event in game')
                print(event)

    def handle_state_change(self, game_state):
        self.make_a_move()

    # noinspection PyMethodMayBeStatic
    def handle_chat_line(self, chat_line):
        print(chat_line)

    def check_first_move(self):
        self.client.bots.post_message(self.game_id, "Depth level " + str(self.engine_depth_level))
        self.make_a_move()

    def make_a_move(self):
        ongoing_game = self.client.games.get_ongoing()
        if ongoing_game:
            if ongoing_game[0]["isMyTurn"]:
                fen = self.get_fen(ongoing_game[0])
                print(fen)
                board = chess.Board(fen)
                result = self.engine.play(board, chess.engine.Limit(depth=self.engine_depth_level, time=0.100))
                self.client.bots.make_move(self.game_id, result.move)

    # noinspection PyMethodMayBeStatic
    def get_fen(self, ongoing_game):
        fen = ongoing_game["fen"]
        color = ongoing_game["color"]
        if color == "white":
            fen = fen + " w"
        else:
            fen = fen + " b"
        return fen

    # noinspection PyMethodMayBeStatic
    def get_engine(self):
        if os.name == "nt":
            return chess.engine.SimpleEngine.popen_uci("D:\ChessEngines\stockfish-10-win\Windows\stockfish_10_x64.exe")
        else:
            return chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
