## modified by Johan Asplund, for my befunge-93 interpreter

# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to
import pygame


def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass


def display_box(screen, message):
    """Print a message in a box in the middle of the screen"""
    fontobject = pygame.font.Font("./font/Inconsolata.otf", 14)
    pygame.draw.rect(screen, (0, 0, 0),
                    ((screen.get_width() / 2) - 150,
                    (screen.get_height() / 2) - 10,
                    250, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                    ((screen.get_width() / 2) - 152,
                    (screen.get_height() / 2) - 12,
                    254, 24), 1)

    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (230, 200, 70)),
                    ((screen.get_width() / 2) - 150,
                    (screen.get_height() / 2) - 10))
    pygame.display.flip()


def ask(screen, question):
    """ask(screen, question) -> answer"""
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + "".join(current_string))
    while True:
        inkey = get_key()
        if inkey == pygame.K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_ESCAPE:
            break
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string))
    return "".join(current_string)
