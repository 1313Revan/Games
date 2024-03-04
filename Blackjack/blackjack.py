#!/usr/bin/env python3
# coding: utf-8

# A terminal-based Blackjack script I made while learning Python.

# Author: Revan
# Date: 3/4/24

import random
from blkjk_art import logo
from os import system


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = {'Dealer': []}
d_score = 0
p_score = 0

# main functions
def menu():
    system('clear')
    print('\nPlease select an option:\n')
    print('1. Begin\n2. Quit\n')
    menu_op = input('>> ').lower()
    # start game
    if menu_op == 'begin' or menu_op == '1':
        game()
    # leave program
    elif menu_op == 'quit' or menu_op == '2':
        print('\nGoodbye!\n')
        exit()
    else:
        print('\nPlease input a valid word or number.\n')
        menu()

def game():
    for item in players:
        players[item] = []
    d_score = 0
    p_score = 0
    system('clear')
    dealer_deal()
    player_deal()
    dealer_deal()
    player_deal()
    for value in players['Dealer']:
        d_score += value
    for value in players[p_name]:
        p_score += value
    end = False
    while not end:
        system('clear')
        print(f'\nDealer: [{players['Dealer'][0]}, (hidden)]\n{p_name}: {players[p_name]}\n')
        print('\nSelect an option:\n')
        print('1. Hit\n2. Stand\n')
        choice = input('>> ').lower()
        if choice == '1' or choice == 'hit':
            p_card = player_deal()
            p_score += p_card
            if p_score > 21:
                system('clear')
                print(f'\nDealer: {players['Dealer']}\n{p_name}: {players[p_name]}\n')
                print('\nBust!\n')
                print('Play again?\n')
                play_again = input('>> ').lower()
                if play_again == 'yes' or play_again == 'y':
                    game()
                else:
                    print('\nGoodbye!\n')
                    exit()
        elif choice == '2' or choice == 'stand':
            system('clear')
            if d_score < 17:
                while d_score < 17:
                    new_score = dealer_deal()
                    d_score += new_score
                    if d_score > 21:
                        print(f'\nDealer: {players['Dealer']}\n{p_name}: {players[p_name]}\n')
                        print('\nDealer bust!\n')
                        print('Play again?\n')
                        play_again = input('>> ').lower()
                        if play_again == 'yes' or play_again == 'y':
                            game()
                        else:
                            print('\nGoodbye!\n')
                            exit()
            print(f'\nDealer: {players['Dealer']}\n{p_name}: {players[p_name]}\n')
            end = True
        else:
            print('\nInvalid input.\n')
    if p_score > d_score:
        print(f'\n{p_name} wins!\n')
    elif p_score < d_score:
        print('\nDealer wins!\n')
    else:
        print('\nDraw!\n')
    print('Play again?\n')
    play_again = input('>> ').lower()
    if play_again == 'yes' or play_again == 'y':
        game()
    else:
        print('\nGoodbye!\n')
        exit()

# deal functions
def dealer_deal():
    dealer_card = random.choice(cards)
    if dealer_card == 11 and sum(players['Dealer']) + dealer_card > 21:
        dealer_card = 1
    players['Dealer'].append(dealer_card)
    return dealer_card

def player_deal():
    player_card = random.choice(cards)
    if player_card == 11 and sum(players[p_name]) + player_card > 21:
        player_card = 1
    players[p_name].append(player_card)
    return player_card


# script
system('clear')
print(logo)
print('\nWelcome to BLACKJACK\n')
print('\nPlease type your name:\n')
p_name = input('>> ').title()
players[p_name] = []
menu()
