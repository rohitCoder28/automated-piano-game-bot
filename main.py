from pyautogui import click
# from directKeys import click, moveMouseTo
# import win32api, win32con
from PIL import ImageGrab
import time
import keyboard

w, h = 588, 733
score = 0
# previousX = -1
# previousY = -1
lane1 = True
lane2 = True
lane3 = True
lane4 = True


# def PressKey(key):
#     keyboard.press(key)


# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def hit(x, y):
    # # return
    # global score, previousY, previousX
    # # moveMouseTo(x, y)
    click(x, y)
    # score += 1
    # # previousX = x
    # # previousY = y
    # if score > 1000:
    #     actualY += 10
    # if score > 1250:
    #     actualY += 10
    # if score > 1450:
    #     actualY += 10
    # if score > 1600:
    #     actualY += 20
    # for k in range(1700, 2500):
    #     if score > k:
    #         actualY += 10
    #     else:
    #         break


def collide(data):
    global lane1, lane2, lane3, lane4
    if lane1:
        for i in range(670, 720):
            for j in range(750, 850):
                if data[i, j] < 100:
                    hit(i, j)
                    # PressKey("a")
                    lane1 = False
                    lane2 = True
                    lane3 = True
                    lane4 = True
                    return
    if lane2:
        for i in range(850, 900):
            for j in range(750, 850):
                if data[i, j] < 100:
                    hit(i, j)
                    # PressKey("s")
                    lane1 = True
                    lane2 = False
                    lane3 = True
                    lane4 = True
                    return
    if lane3:
        for i in range(1020, 1070):
            for j in range(750, 850):
                if data[i, j] < 100:
                    hit(i, j)
                    # PressKey("d")
                    lane1 = True
                    lane2 = True
                    lane3 = False
                    lane4 = True
                    return
    if lane4:
        for i in range(1170, 1220):
            for j in range(750, 850):
                if data[i, j] < 100:
                    hit(i, j)
                    # PressKey("f")
                    lane1 = True
                    lane2 = True
                    lane3 = True
                    lane4 = False
                    return
    return


if __name__ == "__main__":
    print("Hey.. game about to start")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        collide(data)
        if keyboard.is_pressed('q'):
            break

        # for i in range(670, 720):
        #     for j in range(750, 850):
        #         data[i, j] = 0
        # for i in range(850, 900):
        #     for j in range(600, 650):
        #         data[i, j] = 0
        # for i in range(1020, 1070):
        #     for j in range(600, 650):
        #         data[i, j] = 0
        # for i in range(1170, 1220):
        #     for j in range(600, 650):
        #         data[i, j] = 0
        # image.show()
        # break

