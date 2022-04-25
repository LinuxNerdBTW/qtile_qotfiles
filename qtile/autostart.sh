#! /bin/bash
cbatticon &
#lxsession &
picom --config ~/.config/qtile/picom/picom.conf --experimental-backends &
nitrogen --restore &
#urxvtd -q -o -f &
nm-applet &
dunst --config ~/.config/qtile/dunst/dunstrc &
#flameshot &

## PowerManager
xfce4-power-manager &
# exec plank & disown
#redshift &