import numpy
import os
import chess.pgn






class Opening_Classifier(chess.Board):
    def __init__(self):
        super().__init__()
        self._initialize_opening_boards()
    def classify(self,pgn_game):
        game = open(pgn_game)
        game = chess.pgn.read_game(game)
        board = game.board()
        list_of_moves = []
        found = False
        for i, move in enumerate(game.mainline_moves()):
            board.push(move)
            list_of_moves.append(str(move))
            if found:
                break
            for openings, m in self.modern_queen_pawn_dict.items():
                if set(list_of_moves) == set(m):
                    print(openings)
                    found = True
                    break
            for openings, b in self.opening_boards.items():
                if board == b:
                    pass #print(openings)
                    

        pass
    def _initialize_openings(self):
        self.modern_queen_pawn_dict= {"Modern Queen Pawn":['d2d4','d7d6','c2c4','g7g6','b1c3','f8g7','e2e4'],
                                    "SemiBenoni":['d2d4','c7c5','d4d5','e7e5']}
    def _initialize_opening_boards(self):
        self._initialize_openings()
        self.opening_boards = {}
        for opening, moves in self.modern_queen_pawn_dict.items():
            board = chess.Board()
            for m in moves:
                board.push(chess.Move.from_uci(m))
            self.opening_boards[opening] = board
    def print_boards(self):
        for k,v in self.opening_boards.items():
            print(k)
            print(v)

    def modern_queen_pawn(self):
        mqp_board = chess.Board()
        i_mqp_moves = ['d2d4','d7d6','c2c4','g7g6','b1c3','f8g7','e2e4']
        for m in i_mqp_moves:
            mqp_board.push(chess.Move.from_uci(m))
        print(mqp_board)
if __name__ =='__main__':
    #pgn = open("./chess_games_pgn/standards/Modern.pgn")
    path = "./chess_games_pgn/standards/Modern.pgn"
    classifier = Opening_Classifier()
    classifier.classify(path)
    #classifier.modern_queen_pawn()
