import pyautogui
import time
from keyboard import mouse

# >>> import pyautogui
#
# >>> screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
#
# >>> currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#
# >>> pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
#
# >>> pyautogui.click()          # Click the mouse.
# >>> pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
# >>> pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
#
# >>> pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
# >>> pyautogui.doubleClick()    # Double click the mouse.

# >>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
# Use tweening/easing function to move mouse over 2 seconds.
#
# >>> pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# >>> pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
#
# >>> pyautogui.keyDown('shift') # Press the Shift key down and hold it.
# >>> pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
# >>> pyautogui.keyUp('shift')   # Let go of the Shift key.
#
# >>> pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
#
# >>> pyautogui.alert('This is the message to display.')
# Make an alert box appear and pause the program until OK is clicked.
from pynput.keyboard import Controller

while True:
    drone_type = input("Enter what kind of drone you're going to level upto.\n"
                       "enter p for pentashot\n"
                       "n for necromancer\n"
                       "o for overlord\n"
                       "drone send for drone send (right click)\n"
                       "afk for afk\n"
                       "enter: ")

    if drone_type.lower() == "p":
        print("started")
        time.sleep(1)
        # pyautogui.hotkey("ctrl", "left")
        # pyautogui.keyDown("ctrl")
        # pyautogui.press("right")
        # pyautogui.keyUp("ctrl")
        # time.sleep(0.0001)
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.keyDown("u")
        pyautogui.write("628776576547765477654654654544122", interval=0.0001)
        pyautogui.keyUp("u")
        pyautogui.press("e")

    if drone_type.lower() == "n":
        print("started")
        time.sleep(1)
        # pyautogui.hotkey("ctrl", "left")
        # pyautogui.keyDown("ctrl")
        # pyautogui.press("right")
        # pyautogui.keyUp("ctrl")
        # time.sleep(0.0001)
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.keyDown("u")
        pyautogui.write("628776576547765477654654654544888", interval=0.0001)
        pyautogui.keyUp("u")
        pyautogui.press("e")

    if drone_type.lower() == "o":
        print("started")
        time.sleep(1)
        # pyautogui.hotkey("ctrl", "left")
        # pyautogui.keyDown("ctrl")
        # pyautogui.press("right")
        # pyautogui.keyUp("ctrl")
        # time.sleep(0.0001)
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.keyDown("u")
        pyautogui.write("62865664582645654862546548254488288", interval=0.0001)
        pyautogui.keyUp("u")
        pyautogui.press("e")

    if drone_type.lower() == "drone send":
        time.sleep(2)
        i = 0
        while i < 3:
            i += 1
            mouse.press(button="right")
            time.sleep(30)
            mouse.release(button="right")
            time.sleep(35)

    if drone_type.lower() == "afk":
        team_colour = input("Enter what colour your team is: ")
        if team_colour == "blue":
            time.sleep(2)
            pyautogui.keyDown("w")
            pyautogui.keyDown("a")
            time.sleep(35)
            pyautogui.keyUp("w")
            pyautogui.keyUp("a")
            pyautogui.press("c")
        if team_colour == "purple":
            time.sleep(3)
            pyautogui.keyDown("w")
            pyautogui.keyDown("d")
            time.sleep(35)
            pyautogui.keyUp("w")
            pyautogui.keyUp("d")
            pyautogui.press("c")
        if team_colour == "green":
            time.sleep(3)
            pyautogui.keyDown("s")
            pyautogui.keyDown("a")
            time.sleep(35)
            pyautogui.keyUp("s")
            pyautogui.keyUp("a")
            pyautogui.press("c")
        if team_colour == "red":
            time.sleep(3)
            pyautogui.keyDown("s")
            pyautogui.keyDown("d")
            time.sleep(35)
            pyautogui.keyUp("s")
            pyautogui.keyUp("d")
            pyautogui.press("c")

    else:
        print("nah mate")
