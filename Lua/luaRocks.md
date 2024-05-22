```bash
sudo dnf update && sudo dnf install luarocks
```

- Run `luarocks` to see the available commands.
-

You can get help on any command by using the help command:
```bash
luarocks help install
```

Install packages like this:
```bash
luarocks install dkjson
```

When you install rocks using the `luarocks install`, you get new modules available for loading via `require()` from Lua. For example, after we install the dkjson rock, type `luarocks show dkjson` to show the module installed by the rock:
```
  luarocks show dkjson
```

