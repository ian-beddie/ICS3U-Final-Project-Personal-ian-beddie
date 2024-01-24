#!/usr/bin/env python3

"""
Created by: Ian Beddie
Created on: Jan 2024
This program is the "Vampire survivors" game on the pybadge
"""

import constants
import stage
import ugame


def game_scene() -> None:
    """This function is the main game game_scene"""

    image_bank_background = stage.Bank.from_bmp16("vampire_survivors_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("vampire_survivor.bmp")

    background = stage.Grid(image_bank_background, 10, 8)

    person = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    game = stage.Stage(ugame.display, 60)

    game.layers = [person] + [background]

    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_RIGHT != 0:
            if person.x < constants.SCREEN_X - constants.SPRITE_SIZE:
                person.move((person.x + constants.SPRITE_MOVEMENT_SPEED), person.y)
            else:
                person.move((constants.SCREEN_X - constants.SPRITE_SIZE), person.y)

        if keys & ugame.K_LEFT != 0:
            if person.x > 0:
                person.move((person.x - constants.SPRITE_MOVEMENT_SPEED), person.y)
            else:
                person.move(0, person.y)

        if keys & ugame.K_DOWN != 0:
            if person.y < constants.SCREEN_Y - constants.SPRITE_SIZE:
                person.move(person.x, (person.y + constants.SPRITE_MOVEMENT_SPEED))
            else:
                person.move(person.x, (constants.SCREEN_Y - constants.SPRITE_SIZE))

        if keys & ugame.K_UP != 0:
            if person.y > 0:
                person.move(person.x, (person.y - constants.SPRITE_MOVEMENT_SPEED))
            else:
                person.move(person.x, 0)

        game.render_sprites([person])
        game.tick()


if __name__ == "__main__":
    game_scene()
