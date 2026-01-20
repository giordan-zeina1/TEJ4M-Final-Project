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
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    try:
        coin_sound = open("coin.wav", "rb")
        ugame.audio.play(coin_sound)
    except: pass # Skip if file is missing

    time.sleep(2.0)
    menu_scene()

def menu_scene():
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_mt_background, 10, 8)
    
    text = []
    text1 = stage.Text(width=29, height=12, palette=constants.RED_PALETTE)
    text1.move(20, 40)
    text1.text("PENALTY SHOOTOUT")
    text.append(text1)
    
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
    
    score_text = stage.Text(width=29, height=14, palette=constants.RED_PALETTE)
    score_text.move(1, 1)
    score_text.text("Score: 0")

    image_bank_sprites = stage.Bank.from_bmp16("football_sprites.bmp")
    image_bank_bg = stage.Bank.from_bmp16("football_pitch.bmp")
    
    background = stage.Grid(image_bank_bg, 10, 8)
    keeper = stage.Sprite(image_bank_sprites, 0, 72, 40)
    ball = stage.Sprite(image_bank_sprites, 1, 72, 100)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [score_text, keeper, ball, background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        player_choice = None

        if keys & ugame.K_LEFT and keys & ugame.K_UP: player_choice = "TL"
        elif keys & ugame.K_RIGHT and keys & ugame.K_UP: player_choice = "TR"
        elif keys & ugame.K_UP: player_choice = "M"
        elif keys & ugame.K_LEFT: player_choice = "BL"
        elif keys & ugame.K_RIGHT: player_choice = "BR"

        if player_choice and rounds < 5:
            rounds += 1
            computer_choice = random.choice(list(constants.LOCATIONS.keys()))

            b_pos = constants.LOCATIONS[player_choice]
            k_pos = constants.LOCATIONS[computer_choice]
            
            ball.move(b_pos[0], b_pos[1])
            keeper.move(k_pos[0], k_pos[1])

            if player_choice != computer_choice:
                score += 1
            
            score_text.clear()
            score_text.text("Score: {0} / {1}".format(score, rounds))
            game.render_block()
            time.sleep(1.0)

            # Reset
            ball.move(72, 100)
            keeper.move(72, 40)
            game.render_block()

        if rounds >= 5:
            time.sleep(2.0)
            menu_scene()
        game.tick()

if __name__ == "__main__":
    splash_scene()
