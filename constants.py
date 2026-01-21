#!/usr/bin/env python3

"""
Created by: Giordan Zeina
Created on: Jan 2026
This constants file is for Penalty Shootout game
"""

SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60

# Palette for Text
RED_PALETTE = (0xffe0, 0x1a76, 0x0000, 0xff00, 0xffaf, 0xff51, 0xffa8, 0xff00,
               0x9068, 0x8633, 0x3010, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

# Shot selection for sprites
LOCATIONS = {
    'TL': (40, 40), 'M': (72, 40), 'TR': (104, 40),
    'BL': (40, 80), 'BR': (104, 80)
}
