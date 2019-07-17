#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        move = ' '
        while move not in moves:
            move = input("Enter Rock,Paper or scissors:\n").lower()
            if move not in moves:
                print("I dont understand, try again")
        return move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.next_move = 'rock'

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move
        pass


class Cycleplayer(Player):
    def __init__(self):
        self.next_move = 0

    def move(self):
        return moves[self.next_move]

    def learn(self, my_move, their_move):
        if self.next_move <= 1:
            self.next_move = self.next_move+1
        elif self.next_move == 2:
            self.next_move = 0
            pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0
        self.scores = [0, 0]

    def keep_score(self, p1, p2):
        if (beats(p1, p2)):
            print("p1 has won this round!!")
            self.p1.score = self.p1.score+1
        elif (beats(p2, p1)):
            print("p2 has won this round!!")
            self.p2.score = self.p2.score+1
        else:
            print("No one has won this round!!")
            self.p1.score = self.p1.score
            self.p2.score = self.p2.score

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.keep_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(self.p1.score, " _", self.p2.score)
        if self.p1.score > self.p2.score:
            print(f"{self.p1} is the winer with {self.p1.score} scores")
        elif self.p1.score < self.p1.score:
            print(f"{self.p2} is the winer with {self.p2.score} scores")
        else:
            print(f"Equalize")
        print("Game over!")


if __name__ == '__main__':
    valid_inputs = ["rock", "reflect", "random", "cycle", "human"]
    Player_input = " "
    while Player_input not in valid_inputs:
        Player_input = input("choose player to play against human or cycle\n")
        if Player_input not in valid_inputs:
            print("not one of our players!")
    d = {"human": Game(HumanPlayer(), HumanPlayer()),
         "cycle": Game(HumanPlayer(), Cycleplayer()),
         "random": Game(HumanPlayer(), RandomPlayer()),
         "rock":  Game(HumanPlayer(), Player()),
         "reflect": Game(HumanPlayer(), ReflectPlayer())}
    game = d[Player_input.lower()]
    game.play_game()
