import badger2040
import jpegdec

# Global Constants
WIDTH = badger2040.WIDTH  # 296
HEIGHT = badger2040.HEIGHT # 128

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)


display.set_pen(15)
display.clear()

jpeg = jpegdec.JPEG(display.display)
jpeg.open_file("mega-me-back.jpg")
jpeg.decode(0, 0)


display.set_pen(0)
display.set_font("bitmap8")
display.set_thickness(1)
display.text("Benjamin", 12, 10, (WIDTH - 4), 4)
display.text("Spain", 48, 48, (WIDTH - 16), 4)

display.line(4, 86, 144, 86, 2)
display.line(6, 88, 146, 88, 1)
display.line(4, 86, 144, 86, 2)
display.line(144, 86, 168, 62, 2)
display.line(146, 88, 170, 64, 1)
display.line(184, 46, 198, 32, 2)
display.line(186, 48, 200, 34, 1)
display.line(198, 32, 198, 4, 2)
display.line(200, 34, 200, 4, 1)

display.set_thickness(1)
display.text("PRINCIPAL ENGINEER", 4, 110, (WIDTH - 4), 2)
display.text("@bspain", 216, 110, (WIDTH - 16), 2)

display.line(176, 116, 212, 116, 1)
display.line(178, 119, 212, 119, 2)
display.line(212, 128, 212, 106, 1)
display.line(212, 106, 296, 106, 1)
display.update()

while True:
    # Sometimes a button press or hold will keep the system
    # powered *through* HALT, so latch the power back on.
    display.keepalive()

    # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()
