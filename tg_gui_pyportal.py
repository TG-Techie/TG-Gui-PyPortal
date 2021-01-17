
# hardware imports
import gc
import board
from board import DISPLAY as display
import displayio
import adafruit_touchscreen

# TG-Gui setup imports
from tg_gui_core import *
from tg_gui_std import *
from tg_gui_std.event_loops import SinglePointEventLoop
from tg_gui_std.root_wrapper import DisplayioRootWrapper, DisplayioScreen


# hardware setup
splash = displayio.Group()
display.show(splash)

touchscreen = adafruit_touchscreen.Touchscreen(
    board.TOUCH_XL,
    board.TOUCH_XR,
    board.TOUCH_YD,
    board.TOUCH_YU,
    calibration=((5800, 59000), (5800, 57000)),
    size=(320, 240),
)

def get_touch_coord():
    """
    this is a function called by the standard, SinglePointEventLoop loop
        to get new data from the screen. If the screen is touched it returns a
        the coordinates in a tuple (x, y), otherwise it returns None.
    """
    global touchscreen
    # get two points and filter for the hatder one
    point1 = touchscreen.touch_point
    point2 = touchscreen.touch_point

    if point1 is None or point2 is None:
        return None
    else:
        return point1[0:2] if point1[2] > point2[2] else point2[0:2]

# TG-Gui setup

# The screen is a combination of context, implementation details, and defaults
#   for a given TG-Gui window. (aka "root")
# Note: this Screen/LayoutCls/Palettes api is not finalized and my be changing
screen = DisplayioScreen(
    # Layout clases are objects that describe the orientation of the device.
    layout_class = LayoutCls.mobile(SizeClass.regular, SizeClass.compact),
    display=display,
    min_size = 40,
    default = Defaults(
        margin      = 5,
        radius      = 20,
        font_size   = 2,
        _fill_color_    = 0x20609f, #0x20609f,
        _selected_fill_ = 0x7fffff,
        _text_color_    = 0xffffff,
        _selected_text_ = 0x000000,
    ),
    palettes = Palettes(
        primary = Palette(
            fill_color    = 0x20609f, #0x20609f,
            text_color    = color.white,
            selected_fill = 0x7fffff,
            selected_text = color.black,
            backfill      = color.gray,
        ),
        secondary = Palette(
            fill_color    = color.black,
            text_color    = color.lightgray,
            selected_fill = color.gray,
            selected_text = color.black,
            backfill      = color.red, # red until decided (to make it stand out)
        )
    )
)

# This handles touch inputs and translates them
event_loop = SinglePointEventLoop(
    screen=screen, # provides context / what to apply events to
    update_coord=get_touch_coord # provides as hardware call
)

# User Imports

appwrapper = DisplayioRootWrapper(
    screen=screen,
    display=display,
    size=(320, 240)
)

default, palette = screen.default, screen.palettes

def run_app_loop():
    """
    """
    appwrapper._std_startup_()
    app = appwrapper.wrapped

    while True:
        gc.collect()
        # print(gc.mem_free())
        for _ in range(10):
            app._loop_()
            event_loop.loop()
            display.refresh()
