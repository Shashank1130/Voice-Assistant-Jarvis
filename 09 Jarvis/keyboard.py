from pynput.keyboard import Key,Controller
from time import sleep

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def fullvolume():
    for i in range(50):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volumedown():
    for i in range(8):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


def forward():
    keyboard.press(Key.right) # press the right arrow key
    keyboard.release(Key.right)
    sleep(0.1)

def backward():
    keyboard.press(Key.left) # press the left arrow key
    keyboard.release(Key.left)
    sleep(0.1)
