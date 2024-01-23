#!/usr/bin/env python3

"""
Created by: Ian Beddie
Created on: Jan 2024
This program is the "Vampire survivors" game on the pybadge
"""

import stage
import ugame


def game_scene() -> None:
    """This function is the main game game_scene"""

    image_bank_background = stage.Bank.from_bmp16("vampire_survivors_background.bmp")

    background = stage.Grid(image_bank_background, 10, 8)

    game = stage.Stage(ugame.display, 60)

    game.layers = [background]

    game.render_block()

    while True:
        pass


if __name__ == "__main__":
    game_scene()
