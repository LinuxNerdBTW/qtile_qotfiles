
from libqtile.config import Key
from libqtile.command import lazy
from .functions import *


mod = "mod4"                              
ctrl = "control"
myTerm = "termite"                             
keys = [
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn("kitty"),
             desc='Launches Floating Terminal'
             ),
         Key([mod], "a",
             lazy.spawn("rofi -terminal termite -show drun -modi drun -theme ~/.config/qtile/rofi/themes/nord/nord.rasi"),
             desc='Rofi Application Launcher'
             ),
         Key([mod], "e",
             lazy.spawn("rofi -show emoji -modi emoji -theme ~/.config/qtile/rofi/themes/onedark/onedark.rasi"),
             desc='Rofi Emoji Launcher'
             ),

         Key(["mod1"], "Tab",
             lazy.spawn("rofi -show window -modi window -theme ~/.config/qtile/rofi/themes/onedark/onedark_window.rasi"),
             desc='Rofi Application Switcher'
             ),

         Key([mod], "s",
             lazy.spawn("flameshot gui"),
             desc='ScreenShot'
             ),

         Key([mod], "Tab",
             lazy.next_layout(),    
             desc='Toggle through layouts'
             ),
         Key([mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod], "l",
            lazy.spawn("betterlockscreen --lock"),
            desc='betterlockscreen'
            ),
         ### Launching Programs 
         Key([ctrl, "mod1"], "h",
            lazy.spawn("kitty -e htop"),
            desc='htop'
            ),
         Key([ctrl, "mod1"], "v",
            lazy.spawn("kitty -e vim"),
            desc='vim'
            ),
         Key([ctrl, "mod1"], "b",
            lazy.spawn("kitty -e btop"),
            desc='btop'
            ),
         Key([mod], "d",
            lazy.spawn("thunar"),
            desc="Thunar File Manager"
            ),
         Key([mod], "b",
            lazy.spawn("brave"),
            desc="Brave browser"
            ),
         Key([mod], "v",
            lazy.spawn("pavucontrol"),
            desc="PavuControl"
            ),

         ### Window controls
         ### Window Focus 
         Key([mod], "Down",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "Up",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod], "Left",
             lazy.layout.left(),
             desc='Move focus left in current stack pane'
             ),
         Key([mod], "Right",
             lazy.layout.right(),
             desc='Move focus right in current stack pane'
             ),
         ### window shuffle 
         
         Key([mod, "shift"], "Down",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "Up",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod, "shift"], "Left",
             lazy.layout.shuffle_left(),
             desc='Move windows left in current stack'
             ),
         Key([mod, "shift"], "Right",
             lazy.layout.shuffle_right(),
             desc='Move windows right in current stack'
             ),

         Key([ctrl], "Right",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([ctrl], "Left",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Custom menu .....
         Key([mod], "m",
            lazy.spawn("/home/mangal/bin/menu"),
            desc="custom menu"
            ),
         Key([mod], "n",
            lazy.spawn("/home/mangal/bin/rofi-network-manager/rofi-network-manager.sh"),
            desc="custom menu"
            ),
         Key(["mod1"], "F4",
            lazy.spawn("/home/mangal/bin/powermenu"),
            desc="custom menu"
            ),
]
