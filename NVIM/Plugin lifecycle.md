In this section we're going to look at some lua functions we can use in the plugin spec.
- These functions get executed at different points in time during lazy.nvim's initialization process

## init
This function that gets executed during Neovim's startup process before the plugin is loaded. Note that lazy.nvim will always execute it during startup even if the plugin is configured to be lazy loaded.

_When is this useful?_

In case we want to configure a plugin written in vimscript. These types of plugins are configured using global variables that must be created before the plugin loads.
```lua
{
  'dyng/ctrlsf.vim',
  init = function()
    -- to create global variables accessible to
    -- vimscript we use`vim.g`

    vim.g.ctrlsf_default_root = 'cwd'
    vim.g.ctrlsf_auto_focus = {at = 'start'}
  end,
}
```

## opts
Here's `mini.surround`
```lua
{
  'echasnovski/mini.surround',
  branch = 'stable',
  main = 'mini.surround',
  opts = {
    search_method = 'cover_or_next',
  },
}
```
- When we use the `opts` property like this we are also using another property called config.

90% of lua plugins follow a common a convention, they have a lua module that exposes a function called `setup`. So when we use `opts` we are telling lazy.nvim that the plugin follows that convention. So lazy.nvim will pass that `opts` property to the `setup` function of the plugin.

Let me try to illustrate this with code. Imagine that lazy.nvim is adding a `config` function for you, and it does something like this.
```lua
{
  'echasnovski/mini.surround',
  branch = 'stable',
  main = 'mini.surround',
  opts = {
    search_method = 'cover_or_next',
  },
  config = function(PluginSpec)
    local options = nil

    if type(PluginSpec.opts) == 'function' then
      options = PluginSpec.opts(PluginSpec)
    elseif type(PluginSpec.opts) ~= 'nil' then
      options = PluginSpec.opts
    end

    require(PluginSpec.main).setup(options) 
  end
}
```
Actually, lazy.nvim will try it's best to figure out what is the name of the "main module" of the plugin. If you decide to use lazy.nvim's `config` implementation then adding the `main` property to the plugin spec is optional.

Notice in the implementation I showed `opts` can also be a function. lazy.nvim allows that too. So you can have a custom implementation that returns the result you want. This is also a valid spec.
```lua
{
  'echasnovski/mini.surround',
  branch = 'stable',
  main = 'mini.surround',
  opts = function(PluginSpec)
    -- silly example

    if vim.env.THIS_IS_MY_WORK_PC == 'yes' then
      -- work pc gets the custom configuration
      return {
        search_method = 'cover_or_next',
      }
    end

    -- the others just use whatever 
    -- defaults mini.surround has
    return {}
  end,
}
```
_When does this opts function gets executed?_

Whenever `config` gets executed. Speaking of which...

## config

- This is the function that gets executed after lazy.nvim loads the plugin.

- The common usecase for this function is to call the `setup` function of lua plugins.

So we can write the plugin spec for `mini.surround` like this.
```lua
{
  'echasnovski/mini.surround',
  branch = 'stable',
  config = function()
    require('mini.surround').setup({
      search_method = 'cover_or_next',
    })
  end,
}
```
Notice here it's not necessary to add `main` or `opts` to the plugin spec, we already handle all of that manually. The string `mini.surround` is written in the require function, and the lua table that used to be in `opts` is now in the `.setup()` function.
