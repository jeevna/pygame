# Checkpoint 1:
#
# Snowball game
#
# Character: white circle/sphere
# Background: hilltop
#
# Objects = [
#
# Obstacles: trees, yetis, bear
# Bonus points: people, snowmen
#
# ]
#
# Def main_function(keys):
#
# As time lapses, change the sprite to be larger and larger (a growing snowball)
# Increment the score as time elapses
# 	add to score (weight of snowball) every time a bonus is touched
#
# Increase the speed of the character as time elapses (snowball gets heavier)
#
# If sideways arrow keys are pressed, move side to side a certain amount
# Randomize the order in which obstacles cross the screen, direction and speed
# Randomize the order in which bonuses appear on the screen
#
# If an obstacle is hit, reduce the snowball size
# 	If the snowball is already small (i.e. early in the game) end game
#
# If the character goes off screen, end the game
# If the character hits another player, end the game
#
# If the game ends, display the score (weight of the snowball)

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

character = gamebox.from_color(150, 150, 'white', 10, 10)
background = gamebox.from_color(800, 600, 'light blue', 10, 10)
sky = gamebox.from_color(400, camera.top, 'black', 2000, 20)

objects = [

]

rock1 = gamebox.from_image(random.randint(2, 700), 600, "rock-icon-0.png")
rock2 = gamebox.from_image(random.randint(2, 700), 600, "rock-icon-0.png")
tree1 = gamebox.from_image(random.randint(2, 700), 600, "https://www.freeiconspng.com/uploads/small-tree-icon-8.png")
tree2 = gamebox.from_image(random.randint(2, 700), 600, "https://www.freeiconspng.com/uploads/small-tree-icon-8.png")

# obstacles = [
#     gamebox.from_color(random.randint(2, 700), 600, "green", 20, 40),
#     gamebox.from_color(random.randint(2, 700), 600, "green", 20, 40),
#     gamebox.from_color(random.randint(2, 700), 600, "grey", 20, 20),
#     gamebox.from_color(random.randint(2, 700), 600, "grey", 20, 20),
#     gamebox.from_image(random.randint(2, 700), 600, "https://www.freeiconspng.com/uploads/small-tree-icon-8.png"),
#     gamebox.from_image(random.randint(2, 700), 600, "https://www.freeiconspng.com/uploads/small-tree-icon-8.png"),
#     gamebox.from_image(random.randint(2, 700), 600, "rock-icon-0.png"),
#     gamebox.from_image(random.randint(2, 700), 600, "rock-icon-0.png")
# ]

bonuses = [
    gamebox.from_color(random.randint(2, 700), 600, "pink", 10, 20)
]

score = 0
ticks = 0


def tick(keys):
    """this function increments score based on elapsed time, creates and renders obstacles and bonuses, character moves left or right every time the
    left or right arrow key is clicked, obstacles and bonuses randomly scroll from left to right, game ends upon collision with obstacle or movement off screen"""
    global ticks
    ticks += 1
    camera.clear("light blue")
    camera.draw(background)
    camera.draw(sky)
    objects.append(sky)
    character.y += 5
    camera.draw(character)
    for item in objects:
        camera.draw(item)
    for item in obstacles:
        camera.draw(item)

    if pygame.K_LEFT in keys:
        character.x -= 20
    if pygame.K_RIGHT in keys:
        character.x += 20

    character.speedy += 0.01
    character.move_speed()
    camera.x = character.x + 10
    camera.y = character.y

    if ticks % 60 == 0:
        global score
        score += 1
        bonuses.append(bonuses)
    for item in bonuses:
        item.x += 30
    for item in obstacles:
        character.move_to_stop_overlapping(item)
        if character.bottom_touches(item) or character.right_touches(item) or character.left_touches(item):
            text = gamebox.from_text(camera.x, camera.y, "Game Over!", 60, 'red')
            camera.draw(text)
            gamebox.pause()
    for item in bonuses:
        if character.bottom_touches(item) or character.right_touches(item) or character.left_touches(item):
            score += 10
    if character.x > camera.x or character.y > camera.y:
        text = gamebox.from_text(camera.x, camera.y, "Game Over!", 60, 'red')
        camera.draw(text)
        gamebox.pause()
    score_box = gamebox.from_text(camera.left + 100, camera.top + 20, "Weight: " + str(score) + "lbs.", 60, "black")
    camera.draw(score_box)
    keys.clear()
    camera.display()

gamebox.timer_loop(30, tick)