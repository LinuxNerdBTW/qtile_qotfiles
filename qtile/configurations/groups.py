from libqtile.config import Group,Key
from libqtile.command import lazy
from .keys import keys,mod
# mod = "mod4"
group_names = [(" ", {'layout': 'monadtall'}),
               (" ", {'layout': 'monadtall'}),
               (" ", {'layout': 'monadtall'}),
               (" ", {'layout': 'monadtall'}),
               (" ", {'layout': 'monadtall'}),
               (" ", {'layout': 'monadtall'}),
               (" ", {'layout': 'monadtall'}),
               (" ", {'layout': 'monadtall'}),
               (" ", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
   keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
   keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

