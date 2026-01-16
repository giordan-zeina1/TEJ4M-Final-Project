#!usr/bin/env python3

"""
Created by: Giordan Zeina
Created on: Jan 2026
This is the "Penalty Shootout" program on the PyBadge
"""

import constants
import stage
import ugame
import random
import time

def splash_scene():
    # Load assets
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_background, constants.SCREEN_X, constants.SCREEN_Y)
    
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()
    
    time.sleep(2.0)
    menu_scene()

def menu_scene():
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # Text setup
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE)
    text1.move(20, 10)
    text1.text("PENALTY SHOOTOUT")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START:
            game_scene()
        game.tick()

def game_scene():
    score = 0
    rounds = 0
    
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    # Load Sprites (index 0: keeper, index 1: ball)
    image_bank_sprites = stage.Bank.from_bmp16("soccer_sprites.bmp")
    image_bank_bg = stage.Bank.from_bmp16("soccer_field.bmp")
    
    background = stage.Grid(image_bank_bg, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    keeper = stage.Sprite(image_bank_sprites, 0, 72, 40)
    ball = stage.Sprite(image_bank_sprites, 1, 72, 100)

    # Audio setup
    kick_sound = open("pew.wav", "rb") # Reusing your pew.wav as kick
    goal_sound = open("coin.wav", "rb")
    sound = ugame.audio

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [score_text, keeper, ball, background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        player_choice = None
        
        # Button mapping to locations
        if keys & ugame.K_UP: player_choice = 'M'
        elif keys & ugame.K_LEFT and keys & ugame.K_UP: player_choice = 'TL'
        elif keys & ugame.K_RIGHT and keys & ugame.K_UP: player_choice = 'TR'
        elif keys & ugame.K_LEFT: player_choice = 'BL'
        elif keys & ugame.K_RIGHT: player_choice = 'BR'

        if player_choice and rounds < 5:
            rounds += 1
            sound.play(kick_sound)
            
            # Computer Logic
            comp_choice = random.choice(list(constants.LOCATIONS.keys()))
            
            # Visual feedback: Move sprites
            ball_pos = constants.LOCATIONS[player_choice]
            keeper_pos = constants.LOCATIONS[comp_choice]
            ball.move(ball_pos[0], ball_pos[1])
            keeper.move(keeper_pos[0], keeper_pos[1])
            
            # Scoring Logic
            if player_choice != comp_choice:
                score += 1
                sound.play(goal_sound)
            
            score_text.clear()
            score_text.text("Score: {0} / {1}".format(score, rounds))
            game.render_block()
            
            time.sleep(1.5)
            # Reset for next round
            ball.move(72, 100)
            keeper.move(72, 40)
            game.render_block()

        if rounds >= 5:
            # End game or return to menu
            time.sleep(2.0)
            menu_scene()

        game.tick()

# Start game
splash_scene()