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

jpg = jpegdec.JPEG(display.display)
jpg.open_file("sadie_derp_back.jpg")
jpg.decode(0, 0)


display.set_pen(0)
display.set_font("bitmap8")
display.set_thickness(1)
display.text("Isaiah", 12, 10, (WIDTH - 4), 4)
display.text("Spain", 48, 48, (WIDTH - 16), 4)

display.line(4, 86, 144, 86, 2)
display.line(6, 88, 146, 88, 1)
display.line(144, 86, 168, 62, 2)
display.line(146, 88, 170, 64, 1)

display.set_thickness(1)
display.text("FILM STUDENT", 4, 110, (WIDTH - 4), 2)
display.text("LU", 164, 110, (WIDTH - 16), 2)

display.update()

while True:
    # Sometimes a button press or hold will keep the system
    # powered *through* HALT, so latch the power back on.
    display.keepalive()

    # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()