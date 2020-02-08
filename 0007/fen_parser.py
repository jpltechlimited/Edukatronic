import chess


class FenParser:
    def __init__(self, fen):
        self.fen = fen

    def convert_to_matrix(self):
        board = chess.Board(self.fen)
        str_result = str(board)
        return str_result.split("\n")


fenParser = FenParser("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
print(fenParser.convert_to_matrix()[0])
