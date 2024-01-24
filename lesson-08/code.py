#!/usr/bin/env python3

"""
Created by: Ian Beddie
Created on: Jan 2024
This program is the "Vampire survivors" game on the pybadge
"""

import constants
import stage
import ugame
import time
import random


def splash_scene() -> None:
    """This function is the splash scene"""

    splash_sound = open("splash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(splash_sound)

    image_bank_background = stage.Bank.from_bmp16("menu_background.bmp")

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    game = stage.Stage(ugame.display, constants.FPS)

    game.layers = [background]

    game.render_block()

    while True:
        time.sleep(1.0)
        menu_scene()


def menu_scene() -> None:
    image_bank_background = stage.Bank.from_bmp16("menu_background.bmp")

    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(3, 10)
    text1.text("Beddie Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    game = stage.Stage(ugame.display, constants.FPS)

    game.layers = text + [background]

    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()


def game_scene() -> None:
    """This function is the main game game_scene"""

    image_bank_background = stage.Bank.from_bmp16("vampire_survivors_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("vampire_survivor.bmp")

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    knife_sound = open("knife.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    background = stage.Grid(image_bank_background, constants.SCREEN_X, constants.SCREEN_Y)

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    person = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    enemy = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    game = stage.Stage(ugame.display, 60)

    game.layers = [person] + [enemy] + [background]

    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

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

        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(knife_sound)

        game.render_sprites([person] + [enemy])
        game.tick()


if __name__ == "__main__":
    splash_scene()
