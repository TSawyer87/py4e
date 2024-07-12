## tmux: terminal multiplexer

A terminal multiplexer is essentially a way to make one terminal behave as if it is several. Moreover, a terminal multiplexer like tmux will continue to run even when you log off. So if you're in the middle of something and need to stop working, you just detach and log off. When you log back on, you reattach to the session and it's as if you never left.

Of all the tools that enhance my productivity, tmux probably has the most impact.

### Install tmux

`$ pkg search tmux tmux-3.3a_1                    Terminal Multiplexer  $ pkg install tmux`

To create a session, just type `tmux`

![Default tmux](https://markmcb.com/cli/tmux-zsh-fzf-ui/default_tmux.png)

Default tmux is a bit ugly and not intuitive. It would seem all we got is a bright green bar, but there is much more hidden away. First, let's start by exiting tmux. press `ctrl-b` then `x`. You'll see the green bar turn yellow and ask you to confirm `kill-pane 0 (y/n)?`. Press `y` and you'll be out.

So what did we just do? tmux operates with two-step input: prefix + command. The default prefix is `ctrl-b`. And `x` is the key bound to the `kill-pane` command. In this case, there was only 1 pane, so killing the only pane also killed tmux, and so it exited.

I use a US ANSI keyboard, which means the `` ` `` (back-tick) key is at the upper left of my keyboard. As this key is almost never used, it makes a great single-key alternative to `ctrl-b`.

We'll configure our new tmux prefix in a `.tmux.conf` file in our home directory. And while we're there, we'll give ourselves and easy way to reload the config as we make changes.

Create ~/.tmux.conf

 set prefix to '', but keep 'ctrl-b' too set -g prefix '' bind-key '' send-prefix 
`set-option -g prefix2 C-b  

 easy reload ~/.tmux.conf 
`bind-key r source-file ~/.tmux.conf``

Save the file, and run `tmux` again. Everything should look the same, but try hitting `` ` `` then `x`. You'll get the same kill-pane prompt as before. This time say `n` and stay in tmux.

Hooray! One less key to press. And the way we set it up, `ctrl-b` still works as an alternative. And we bound `r` to source, or (r)eload, our config file. This way we don't have to quit/start tmux for each change we make, we just `` ` `` then `r`.

For the rest of the article I'll write `` ` r `` instead of "`` ` `` then `r`" to be more concise.

### Panes

Let's add a few more lines to our `.tmux.conf` config to allow us to create and cycle through panes.

Append to ~/.tmux.conf

`# split pane commands                                            bind-key | split-window -h -c '#{pane_current_path}'            bind-key - split-window -v -c '#{pane_current_path}'           # cycle through panes                                            set-option -g repeat-time 500 #milliseconds                                       bind-key -r p select-pane -t :.+                                                  bind-key -r P select-pane -t :.-`  

After saving `` ` r `` to reload the config. Now try hitting `` ` - `` and then `` ` | ``. You should now have three panes that you can cycle through by hitting `` ` p ``.

![tmux panes](https://markmcb.com/cli/tmux-zsh-fzf-ui/tmux_panes.png)

This is where tmux starts to become really powerful. Try starting a few commands that don't immediately exit. I'll execute `top` and `iostat -w1`, and also `echo` a string.

![tmux panes with activity](https://markmcb.com/cli/tmux-zsh-fzf-ui/tmux_panes_activity.png)

Now we're starting to see the value of tmux. If you want to have multiple views on the screen all at once, it solves the problem and keeps the many views on the server side (i.e., you could open 3 terminal windows and three connections to do the same thing, but that's on the client side). Now that we have multiple panes open, try out `` ` x `` again. This time it'll kill whatever panes you have active until only one remains.

### Windows

If you like panes, you'll love windows. See that cryptic `0:zsh*` message at the bottom of the screen? That's the name of our window. Like panes, one window isn't too exciting, but when you have several it gets interesting.

Once again, let's edit `.tmux.conf`.

Append to ~/.tmux.conf

`# set window and pane index to 1 (0 by default) for easier direct access set-option -g base-index 1 setw -g pane-base-index 1  # move between windows and sessions bind-key -r h previous-window bind-key -r j switch-client -n bind-key -r k switch-client -p bind-key -r l next-window`

Normally we'd `` ` r `` after saving, but we need to kill all of our panes for this one to fully work as we're changing how panes get numbered. To do that either `` ` x `` each pane, or type `tmux kill-server` and you'll be out of tmux. Then `tmux` again to start once more.

This time when you start there's a very subtle difference. That `0:zsh*` at the bottom is now `1:zsh*` because we told tmux to count windows starting with 1. This will come in handy because we can fast switch to windows by typing `` ` 1 `` or whatever their number is.

Let's create some windows. How about 5? Type `` ` c `` four times to add four windows for a total of five.

![tmux windows](https://markmcb.com/cli/tmux-zsh-fzf-ui/tmux_windows.png)

If all went well, you should see 5 windows listed in the green bar. If you type `` ` 3 `` you'll jump to window 3. Your visual cue is the `*` next to the window name, i.e., you should see `3:zsh*`.

It's a bit confusing that all our windows are named the same. Let's rename them with `` ` , `` and give them descriptive names.

![tmux named windows](https://markmcb.com/cli/tmux-zsh-fzf-ui/tmux_named_windows.png)

You can see now I've got a main window for various system administration, my todo list, a window for IRC chat, a window for a file browser, and a window to monitor logs. I haven't actually set any of this up, so let's call it a vision for now. :-)

Aside from using `` ` [number] `` to move around, we can use our keybindings we added before to use [vim-style arrow keys](https://catonmat.net/why-vim-uses-hjkl-as-arrow-keys). Try `` ` h `` to go left and `` ` l `` to go right through the window list.

We also added the ability to use `` ` j `` and `` ` k `` to go through sessions, but we won't cover that just yet. If windows are collections of panes, then sessions are collections of windows. You may never need more than one session, but if you do, know they're there.

### Styling

Ok, so we have this new cool tool that is sure to enhance our productivity, but that green bar is just so ... green. Let's play with the style a bit.

Append to ~/.tmux.conf

`# STYLE  # Pane seperation colors, i.e., lines between panes set -g pane-active-border-style 'fg=colour243' set -g pane-border-style 'fg=colour236'  # Brighter text for active window pane set -g window-style 'fg=colour245' set -g window-active-style 'fg=colour252'  # Add padding to window names, and visual flag for window activity set-option -g window-status-format ' #W#{?window_activity_flag,!,} '  set-option -g window-status-separator ''  # Default gray on gray status bar style set-option -g status-style bg=colour236,fg=colour248  # Inactive window labels match the color of the status bar set-window-option -g window-status-style bg=colour236,fg=colour248  # Active window label is slightly highlighted. Append -Z if a pane is zoomed. set-window-option -g window-status-current-style bg=colour24,fg=colour14 set-window-option -g window-status-current-style bg=colour239,fg=colour251 set-option -g window-status-current-format ' #W#{?window_zoomed_flag,-Z,} '  # Left status set -g status-left "#[bg=colour239,fg=colour252]"  # Right status set -g status-right "#[bg=colour238,fg=colour244] %d %b %H:%M "`

With those tweaks, hit `` ` r `` and the green is no more! The comments explain what each line does, but if it's not clear, check out [tmux(1)](https://man.freebsd.org/cgi/man.cgi?query=tmux) for details.

![tmux basic style](https://markmcb.com/cli/tmux-zsh-fzf-ui/tmux_style_basic.png)

I find this much easier to look at compared to the default, but play with the configs and find a look and feel you like.

### Mouse and Scroll

Ok, so we're looking good. One last (optional) thing to do: mouse support. If you're like me, you almost always interface with a shell via a terminal emulator in a desktop environment. All of the screenshots have been exactly that, kitty running in macOS and connected to a FreeBSD remote. If you're in a desktop environment, you probably have a mouse. Let's enable it.

Append to ~/.tmux.conf

`# MOUSE  # Enable mouse support by default, but make it easy to turn on/off set-option -g mouse on bind-key m set-option -g mouse  # If you have sessions, and put #S in the status bar, click or  # scroll on the session name to cycle through sessions bind-key -n MouseUp1StatusLeft switch-client -n bind-key -n WheelDownStatusLeft switch-client -n bind-key -n WheelUpStatusLeft switch-client -p  # increase scrollback set-option -g history-limit 50000`

Save and `` ` r `` and then run `for i in $(seq 1000); do echo "$i"; done` to have your shell count to 1000 with one number on each line. Now grab your mouse and scroll up.

![tmux mouse scroll](https://markmcb.com/cli/tmux-zsh-fzf-ui/tmux_mouse_scroll.png)

If all went well you'll happily scroll up through the tmux scroll-back history (which we just set to 50000 lines). You'll see the yellow status indicator appear telling you where you are and how many total lines tmux is tracking.

To get back to a prompt, either scroll back down, or type `q`.

### A few final notes on tmux

This article isn't meant to be a comprehensive tmux guide, but a few points worth noting:

- `` ` d `` is how you detach from tmux.
- `tmux a` is short for `tmux attach` and will attach you to an existing tmux session
- `` ` D `` will let you detach any client, i.e., if you were attached at home and didn't detach, you could detach your home connection from your phone or wherever.
- `` ` z `` will "zoom" a pane, i.e., if you're looking at 4 panes and temporarily want one to be full screen, zoom it

I've added some scripting into my `.zshrc` to automatically look for and attach to tmux sessions when I log in. Integrating tmux into your workflow like this can be really powerful. Check out the tmux docs for all the options you need to get started.