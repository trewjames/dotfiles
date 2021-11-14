import os
import subprocess
from libqtile import bar, hook
from libqtile.config import Click, Drag, EzKey, Group, Match, Screen
from libqtile.lazy import lazy

import keys as Keys
import widgets as Widgets
import layouts as Layouts
from colors import OneDark as c

# FIX: set up binds
# TODO: set up layouts
# TODO: program hooks

MOD = "mod4"
SHIFT = "shift"
CTRL = "control"
TAB = "tab"


keys = Keys.keys

groups = [
    Group("www", layout="columns"),
    Group("term", layout="columns"),
    Group("sys", layout="columns"),
    Group("doc", layout="columns"),
    Group("dev", layout="columns"),
    Group(
        "work",
        layout="columns",
        matches=[
            Match(
                wm_class=[
                    "Microsoft Teams - Preview",
                ]
            )
        ],
    ),
    Group("chat", layout="columns", matches=[Match(wm_class=["discord", ""])]),
    Group("etc", layout="columns"),
    Group("oth", layout="columns", matches=[Match(wm_class=["Gimp"])]),
]

# TODO: double check this is working
for key, group in zip([1, 2, 3, 4, 5, 6, 7, 8, 9], groups):
    keys.append(EzKey(f"M-{key}", lazy.group[group.name].toscreen()))
    keys.append(EzKey(f"M-S-{key}", lazy.window.togroup(group.name)))


layouts = Layouts.layouts
floating_layout = Layouts.floating_layout

widget_defaults = Widgets.widget_defaults
extension_defaults = widget_defaults.copy()

status_bar = lambda widgets: bar.Bar(widgets, size=24, opacity=1.0)
screens = [Screen(top=status_bar(Widgets.widgets))]

# Drag floating layouts.
mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/startup.sh"])
