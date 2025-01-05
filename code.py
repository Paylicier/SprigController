import board
import busio
import digitalio
import time
import usb_hid
from adafruit_hid.gamepad import Gamepad
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import displayio
import terminalio

# Initialize display
displayio.release_displays()
spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)
tft_cs = board.GP20
tft_dc = board.GP22
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.GP26)
display = ST7735R(display_bus, width=160, height=128, rotation=270, bgr=True)

# Create a simple text label
splash = displayio.Group()
display.root_group = splash
color_bitmap = displayio.Bitmap(160, 160, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x008C4A # Bright Green
bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)
bitmap = displayio.OnDiskBitmap("/logo.bmp")
bitmap.pixel_shader.make_transparent(0)
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader, x=10, y=10)
splash.append(tile_grid)
text_area = label.Label(terminalio.FONT, text="", color=0xFFFFFF)
text_area.x = 30
text_area.y = 100
splash.append(text_area)

# Initialize buttons
buttons = {
    "UP": digitalio.DigitalInOut(board.GP5),    # D-pad Up
    "DOWN": digitalio.DigitalInOut(board.GP7),  # D-pad Down
    "LEFT": digitalio.DigitalInOut(board.GP6),  # D-pad Left
    "RIGHT": digitalio.DigitalInOut(board.GP8), # D-pad Right
    "X": digitalio.DigitalInOut(board.GP13),    # Button X
    "Y": digitalio.DigitalInOut(board.GP12),    # Button Y
    "A": digitalio.DigitalInOut(board.GP14),    # Button A
    "B": digitalio.DigitalInOut(board.GP15),    # Button B
}

for pin in buttons.values():
    pin.pull = digitalio.Pull.UP

# Initialize gamepad
gp = Gamepad(usb_hid.devices)

# Map buttons to gamepad button numbers
button_map = {
    "X": 3,      # Button X
    "Y": 4,      # Button Y
    "A": 1,      # Button A
    "B": 2,      # Button B
}

# Variables for Axis 1 (x) and Axis 2 (y)
axis_x_value = 0  # Axis 1 (x)
axis_y_value = 0  # Axis 2 (y)

last_input = None

while True:
    current_input = None

    # Check button states
    for bid, pin in buttons.items():
        if not pin.value:
            if bid in button_map:
                gp.press_buttons(button_map[bid])
            current_input = bid
        else:
            if bid in button_map:
                gp.release_buttons(button_map[bid])

    # Map UP/DOWN to Axis 2 (y)
    if not buttons["UP"].value:
        axis_y_value = -127  # Full positive value for UP
    elif not buttons["DOWN"].value:
        axis_y_value = 127  # Full negative value for DOWN
    else:
        axis_y_value = 0  # Neutral value

    # Map LEFT/RIGHT to Axis 1 (x)
    if not buttons["LEFT"].value:
        axis_x_value = -127  # Full negative value for LEFT
    elif not buttons["RIGHT"].value:
        axis_x_value = 127  # Full positive value for RIGHT
    else:
        axis_x_value = 0  # Neutral value

    # Update joystick axes
    gp.move_joysticks(x=axis_x_value, y=axis_y_value, z=0, r_z=0)

    # Update display if there's a new input
    if current_input and current_input != last_input:
        text_area.text = f"Last Input: {current_input}"
        last_input = current_input

    time.sleep(0.01)  # Debounce delay