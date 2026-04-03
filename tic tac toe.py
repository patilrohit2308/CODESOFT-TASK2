import math
import random
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.move_count = 0
        
    def print_board(self):
        print("\n   |   |   ")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   \n")
        
    def print_positions(self):
        print("\nPosition guide:")
        print(" 0 | 1 | 2 ")
        print("-----------")
        print(" 3 | 4 | 5 ")
        print("-----------")
        print(" 6 | 7 | 8 \n")
    
    def check_winner(self, player):
        win_patterns = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        return any(self.board[a] == self.board[b] == self.board[c] == player 
                   for a, b, c in win_patterns)
    
    def is_board_full(self):
        return ' ' not in self.board
    
    def get_available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']
    
    def minimax(self, is_maximizing, depth=0):
        if self.check_winner('O'):
            return 10 - depth
        if self.check_winner('X'):
            return depth - 10
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = -math.inf
            for i in self.get_available_moves():
                self.board[i] = 'O'
                score = self.minimax(False, depth + 1)
                self.board[i] = ' '
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for i in self.get_available_moves():
                self.board[i] = 'X'
                score = self.minimax(True, depth + 1)
                self.board[i] = ' '
                best_score = min(best_score, score)
            return best_score
    
    def get_ai_move(self):
        # Add slight delay for more human-like feel
        time.sleep(0.5)
        
        # First move: occasionally pick random corner or center
        if self.move_count == 0:
            if random.random() < 0.3:
                return random.choice([0, 2, 4, 6, 8])
        
        # Find best move using minimax
        best_score = -math.inf
        best_move = None
        
        for i in self.get_available_moves():
            self.board[i] = 'O'
            score = self.minimax(False)
            self.board[i] = ' '
            
            if score > best_score:
                best_score = score
                best_move = i
        
        return best_move
    
    def get_player_move(self):
        while True:
            try:
                move = input("Your turn! Enter position (0-8) or 'q' to quit: ").strip()
                
                if move.lower() == 'q':
                    print("\nThanks for playing! See you next time! 👋")
                    return None
                
                move = int(move)
                
                if move < 0 or move > 8:
                    print("⚠️  Please enter a number between 0 and 8.")
                    continue
                
                if self.board[move] != ' ':
                    print("⚠️  That spot is already taken! Try another one.")
                    continue
                
                return move
                
            except ValueError:
                print("⚠️  Invalid input! Please enter a number between 0 and 8.")
    
    def play(self):
        print("\n" + "="*40)
        print("  Welcome to Tic-Tac-Toe! 🎮")
        print("="*40)
        print("\nYou're X, and I'm O. Let's see who wins!")
        self.print_positions()
        
        while True:
            self.print_board()
            
            # Player's turn
            player_move = self.get_player_move()
            if player_move is None:  # Player quit
                break
                
            self.board[player_move] = 'X'
            self.move_count += 1
            
            if self.check_winner('X'):
                self.print_board()
                print("🎉 Congratulations! You win! Well played!")
                break
            
            if self.is_board_full():
                self.print_board()
                print("🤝 It's a tie! Great game!")
                break
            
            # AI's turn
            print("\n🤔 Let me think...")
            ai_move = self.get_ai_move()
            self.board[ai_move] = 'O'
            self.move_count += 1
            print(f"✓ I'll take position {ai_move}")
            
            if self.check_winner('O'):
                self.print_board()
                print("🏆 I win this round! Want to play again?")
                break
            
            if self.is_board_full():
                self.print_board()
                print("🤝 It's a tie! Great game!")
                break
        
        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again == 'y':
            print("\n" + "="*40 + "\n")
            TicTacToe().play()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
