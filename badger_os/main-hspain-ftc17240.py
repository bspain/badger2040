import badger2040
import jpegdec

# Global Constants
WIDTH = badger2040.WIDTH  # 296
HEIGHT = badger2040.HEIGHT # 128
display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)

state = {
    "code" : 1
}

def render():
    display.set_pen(15)
    display.clear()

    jpeg = jpegdec.JPEG(display.display)
    if state["code"] == 1:
        jpeg.open_file("ftc17240-qrcode-tiny.jpg")
        jpeg.decode(188, 6)
    else:
        jpeg.open_file("sparkyproto_back.jpg")
        jpeg.decode(0, 0)

    display.set_pen(0)
    display.set_font("bitmap8")
    display.set_thickness(1)
    display.text("Hannah", 12, 10, (WIDTH - 4), 4)
    display.text("Spain", 48, 48, (WIDTH - 16), 4)

    display.line(4, 86, 144, 86, 2)
    display.line(6, 88, 146, 88, 1)
    display.line(144, 86, 168, 62, 2)
    display.line(146, 88, 170, 64, 1)

    display.set_thickness(1)
    display.text("IRON EAGLES 17240", 4, 92, (WIDTH - 4), 2)
    display.text("AUTOMATION CAPTAIN", 24, 112, (WIDTH - 16), 2)

    display.update()

while True:
    # Sometimes a button press or hold will keep the system
    # powered *through* HALT, so latch the power back on.
    display.keepalive()

    if display.pressed(badger2040.BUTTON_UP):
        state["code"] = 1
    if display.pressed(badger2040.BUTTON_DOWN):
        state["code"] = 0

    render()

    # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()
