import psmove
import colorsys
import time
from enum import Enum

color_range = 255

#Human speeds[slow, mid, fast]
SLOW_WARNING = [0.1, 0.15, 0.28]
SLOW_MAX = [0.5, 0.8, 1]
FAST_WARNING = [0.5, 0.6, 0.8]
FAST_MAX = [1, 1.4, 1.8]

WERE_SLOW_WARNING = [0.2, 0.3, 0.4]
WERE_SLOW_MAX = [0.7, 0.9, 1.1]
WERE_FAST_WARNING = [0.6, 0.7, 0.9]
WERE_FAST_MAX = [1.1, 1.5, 2.0]

ZOMBIE_WARNING = [0.5, 0.6, 0.8]
ZOMBIE_MAX = [0.8, 1, 1.4]

def hsv2rgb(h, s, v):
    return tuple(int(color * color_range) for color in colorsys.hsv_to_rgb(h, s, v))

def generate_colors(color_num):
    Hue = [ ((num + 1.0)/color_num, 1, 1) for num in range(color_num) ]
    colors = [ hsv2rgb(*hsv_color) for hsv_color in Hue ]
    return colors


def get_move(serial, move_num):
    time.sleep(0.02)
    move = psmove.PSMove(move_num)
    time.sleep(0.05)
    if move.get_serial() != serial:
        for move_num in range(psmove.count_connected()):
            move = psmove.PSMove(move_num)
            if move.get_serial() == serial:
                return move
        return None
    else:
        return move

def lerp(a, b, p):
    return a*(1 - p) + b*p

def change_color(color_array, r, g, b):
    color_array[0] = r
    color_array[1] = g
    color_array[2] = b

class Games(Enum):
    JoustFFA = 0
    JoustTeams = 1
    JoustRandomTeams = 2
    Traitor = 3
    WereJoust = 4
    Zombies = 5
    Commander = 6
    Swapper = 7
    Tournament = 8
    Ninja = 9
    Random = 10

minimum_players = {
    Games.JoustFFA.value: 2,
    Games.JoustTeams.value: 3,
    Games.JoustRandomTeams.value: 3,
    Games.Traitor.value: 6,
    Games.WereJoust.value: 3,
    Games.Zombies.value: 4,
    Games.Commander.value: 4,
    Games.Swapper.value: 3,
    Games.Tournament.value: 3,
    Games.Ninja.value: 2,
    Games.Random.value: 2
}

game_mode_names = {
    Games.JoustFFA.value: 'Joust Free-for-All',
    Games.JoustTeams.value: 'Joust Teams',
    Games.JoustRandomTeams.value: 'Joust Random Teams',
    Games.Traitor.value: 'Traitors',
    Games.WereJoust.value: 'Werewolves',
    Games.Zombies.value: 'Zombies',
    Games.Commander.value: 'Commander',
    Games.Swapper.value: 'Swapper',
    Games.Tournament.value: 'Tournament',
    Games.Ninja.value: 'Ninja Bomb',
    Games.Random.value: 'Random'
}

class Buttons(Enum):
    middle = 524288
    start = 2048
    select = 256
    circle = 32
    nothing = 0

battery_levels = {
    0: "Low",
    1: "20%",
    2: "40%",
    3: "60%",
    4: "80%",
    5: "100%",
    238: "Charging",
    239: "Charged"
}