from libqtile.config import Match
from libqtile import layout

layout_theme = {"border_width": 0,
                "margin": 6,
                "border_normal": "4C566A",
                "border_focus": "5E81AC"
                }

layouts = [
    layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    layout.Floating(**layout_theme)
]



floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),  # tastyworks exit box
    Match(wm_class='gnome-calculator'),  # Calculator
    Match(wm_class='pavucontrol'),
    Match(wm_class='Pavucontrol'),
    Match(wm_class='gl'),
    Match(wm_class='mpv'),
    Match(wm_class='vlc'),
    Match(wm_class='kitty'),
    # Match(wm_class='Termite_float'),
    # Match(wm_class='termite_cloat'),
],
**layout_theme)
