
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Screen
from libqtile.command import lazy
from libqtile import  bar, widget, hook
from libqtile.lazy import lazy
from typing import List  

## Importing configurations modules 
from configurations.keys import mod,keys,ctrl,myTerm
from configurations.mouse import mouse 
from configurations.colours import colors
from configurations.groups import groups
from configurations.layouts import layouts, floating_layout


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="JetBrainsMono Nerd Font Medium Italic",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              # widget.Sep(
              #          linewidth = 0,
              #          padding = 5,
              #          foreground = colors[2],
              #          background = colors[0]
              #          ),
              # widget.TextBox(
              #          text = '◥',
              #          background = colors[7],
              #          foreground = colors[0],
              #          padding = -2,
              #          font= "Fira Code",
              #          fontsize = 50
              #          ),

              widget.TextBox(
                       text = '◣',
                       background = colors[0],
                       foreground = colors[7],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),

             # widget.Sep(
             #           linewidth = 0,
             #           padding = 1,
             #           foreground = colors[2],
             #           background = colors[0]
             #           ),
              widget.GroupBox(
                       font = "JetBrainsMono Nerd Font",
                       fontsize = 14,
                       margin_y = 3,
                       margin_x = 1,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[6],
                       inactive = colors[2],
                       rounded = True,
                       highlight_color = colors[1],
                       highlight_method = "block",
                       urgent_border = colors[8],
                       this_current_screen_border = colors[1],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[1],
                       other_screen_border = colors[4],
                       foreground = colors[7],
                       background = colors[0]
                       ),
              # widget.Prompt(
              #          prompt = prompt,
              #          font = "JetBrainsMono Nerd Font Medium Italic",
              #          padding = 10,
              #          foreground = colors[3],
              #          background = colors[1]
              #          ),
              # widget.Sep(
              #          linewidth = 0,
              #          padding = 10,
              #          foreground = colors[2],
              #          background = colors[0]
              #          ),
              widget.TextBox(
                       text = '◢',
                       background = colors[0],
                       foreground = colors[0],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.WindowName(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       font = "JetBrainsMono Nerd Font Medium Italic"
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[0],
                       foreground = colors[5],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
             widget.Net(
                       interface = "wlp3s0",
                       format = '📡 ↓{down} ↑ {up}',
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e nmtui')},
                       padding = 0
                       ),
              widget.TextBox(
                       text='◢',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.TextBox(
                       text = "",
                       foreground = colors[2],
                       background = colors[4],
                       padding = 1,
                       fontsize = 20
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[4],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e btop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.TextBox(
                      text = " 🎧 Vol:",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[4],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[5],
                       # format = "📅 %A, %B %d, %H:%M:%S ",
                       format = "📅 %H:%M:%S ",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e calcurse')}
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),

              # widget.TextBox(
              #         text= '◣',
              #         background = colors[0],
              #         foreground = colors[4],
              #         padding = -2,
              #         font = "Fira Code",
              #         fontsize = 50
              #         ),
              widget.Systray(
                      background = colors[4],
                      padding = 0
                      ),
              widget.TextBox(
                       text = '◢',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),

              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), border_width=[0, 0, 0, 0], opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()




dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False


auto_fullscreen = False
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
