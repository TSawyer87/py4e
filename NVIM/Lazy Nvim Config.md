#Nvim 
 Lazy.nvim: plugin configuration
#neovim

Here I'm just going to explain how different options in lazy.nvim's plugin configuration interact with each other, and explore a little bit the import system it has. I hope I can give you the basic knowledge that you need to structure your personal Neovim configuration however you want, using lazy.nvim's import feature.
Plugin Spec

In lazy.nvim's documentation they have the concept of "plugin spec." This describes the data lazy.nvim needs about the plugin we want to install. Things like the url of the plugin, the branch we want to download or the plugin dependencies (if it even have dependencies).

From a technical point of view the plugin spec is a "lua table" with a specific set of properties.

Here is an example of a plugin spec for the plugin mini.surround.

{
  'echasnovski/mini.surround',
  branch = 'stable',
  main = 'mini.surround',
  opts = {
    search_method = 'cover_or_next',
  },
}

And so this plugin spec is the thing you give to lazy.nvim's setup function. In your personal Neovim configuration you would have something like this.

require('lazy').setup({
  {
    'echasnovski/mini.surround',
    branch = 'stable',
    main = 'mini.surround',
    opts = {
      search_method = 'cover_or_next',
    },
  },
})

You can find the full list of properties in lazy.nvim's documentation.
The shortest spec

Because Folke (the author of lazy.nvim) is awesome, the only piece of data we need to download a plugin is the short url. So this is a valid plugin spec.

{'echasnovski/mini.surround'}

Notice this is still a "lua table," so actually the shortest spec we can give to lazy.nvim is a string with a short url.

'echasnovski/mini.surround'

Keep in mind, if you do this, lazy.nvim's is going to make some decision for you. In this example I'm showing it might not choose the stable branch for mini.surround. And it won't setup the plugin automatically.

This short spec is best to apply for plugins that don't require user intervention. So mini.surround might not be one of those.
"Plugin lifecycle"

In this section we are going to look at some lua functions we can use in the plugin spec.

These functions get executed at different points in time during lazy.nvim's initialization process.
init

This function that gets executed during Neovim's startup process before the plugin is loaded. Note that lazy.nvim will always execute it during startup even if the plugin is configured to be lazy loaded.

When is this useful?

In case we want to configure a plugin written in vimscript. These types of plugins are configured using global variables that must be created before the plugin loads.

Here is an example of a plugin spec for ctrlsf.vim.

{
  'dyng/ctrlsf.vim',
  init = function()
    -- to create global variables accessible to
    -- vimscript we use`vim.g`

    vim.g.ctrlsf_default_root = 'cwd'
    vim.g.ctrlsf_auto_focus = {at = 'start'}
  end,
}

opts

Let me show you the plugin spec for mini.surround again.

{
  'echasnovski/mini.surround',
  branch = 'stable',
  main = 'mini.surround',
  opts = {
    search_method = 'cover_or_next',
  },
}

Believe or not, when we use the opts property like that we are also using another property called config.

See, like 90% of lua plugins follow a common a convention, they have a lua module that exposes a function called setup. So when we use opts we are telling lazy.nvim that the plugin follows that convention. So lazy.nvim will pass that opts property to the setup function of the plugin.

Let me try to illustrate this with code. Imagine that lazy.nvim is adding a config function for you, and it does something like this.

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

Of course this is an extremely simplified version of what happens under the hood.

Actually, lazy.nvim will try it's best to figure out what is the name of the "main module" of the plugin. If you decide to use lazy.nvim's config implementation then adding the main property to the plugin spec is optional.

Notice in the implementation I showed opts can also be a function. lazy.nvim allows that too. So you can have a custom implementation that returns the result you want. This is also a valid spec.

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

When does this opts function gets executed?

Whenever config gets executed. Speaking of which...
config

This is the function that gets executed after lazy.nvim loads the plugin.

The common usecase for this function is to call the setup function of lua plugins.

So we can write the plugin spec for mini.surround like this.

{
  'echasnovski/mini.surround',
  branch = 'stable',
  config = function()
    require('mini.surround').setup({
      search_method = 'cover_or_next',
    })
  end,
}

Notice here is not necessary to add main or opts to the plugin spec, we already handle all of that manually. The string mini.surround is written in the require function, and the lua table that used to be in opts is now in the .setup() function.
config & opts

You can use config and opts together if you wanted to. The previous example could be written like this.

{
  'echasnovski/mini.surround',
  branch = 'stable',
  opts = {
    search_method = 'cover_or_next',
  },
  config = function(PluginSpec, opts)
    require('mini.surround').setup(opts)
  end,
}

Is there a use case for this?

Not if you have full control of your Neovim configuration.

This can be useful if you have multiple plugin spec for the same plugin. And now you may ask, Why? Why would someone have multiple plugin spec for the same thing? You would if you are using a "Neovim distribution" that happens to have lazy.nvim as a plugin manager. Usually in this case the author of the Neovim distribution will give you the chance to override their default options.

If you don't know, a Neovim distribution is basically a pre-made Neovim configuration.
Import (all the things)

So lazy.nvim has this feature that allows you to specify the name of a lua module, and then lazy will get the plugin spec from that module.

Instead of having a full plugin spec you can do something like this.

{import = 'user.plugins'}

Where user.plugins can be any valid name for a lua module.

And the module that you specify can be just one lua module that returns a plugin spec or it can be a folder with a bunch of lua files.

In our example user.plugins can be a lua file, located in Neovim's runtimepath, that returns a lua spec.

# imagine this is your neovim config folder

nvim
├── init.lua
└── lua
    └── user
        └── plugins.lua

And because lazy.nvim is awesome this user.plugins module can also be a folder that contains lua files (that return plugin specs).

# neovim config folder

nvim
├── init.lua
└── lua
    └── user
        └── plugins
            ├── mini.lua
            ├── theming.lua
            └── ...

Example time.

Let's say we have this in our init.lua file.

require('lazy').setup({
  {import = 'user.plugins'},
})

We can create the user.plugins folder and inside we can have file called mini.lua. And in there we can return a plugin spec or a list of plugin spec.

-- nvim/lua/user/plugins/mini.lua

return {
  {
    'echasnovski/mini.surround',
    branch = 'stable',
    config = function()
      require('mini.surround').setup({
        search_method = 'cover_or_next',
      })
    end,
  },
  {
    'echasnovski/mini.comment',
    branch = 'stable',
    config = function()
      require('mini.comment').setup({})
    end,
  }
}

In that same user.plugins folder we can also have a file called theming.lua. There we can add plugins that modify Neovim's interface somehow.

-- nvim/lua/user/plugins/theming.lua

return {
  {
    'nvim-lualine/lualine.nvim',
    opts = {
      options = {
        icons_enabled = false,
        component_separators = '|',
        section_separators = '',
      },
    },
  },
  {
    'lukas-reineke/indent-blankline.nvim',
    -- i don't think lazy will be able to guess 
    -- `ibl` is the main module, so set it manually
    main = 'ibl',
    opts = {
      enabled = true,
      scope = {
        enabled = false,
      },
      indent = {
        char = '▏',
      },
    }
  }
}

And then we can have other lua files in user.plugins... you get the idea.

Hopefully you can see the potential this has. You can separate your plugins by category, purpose or configure each plugin in its own file. You are free to do whatever you want, as long as you give lazy.nvim what it needs.
One more thing...

Since you can have your entire plugin setup behind one import, lazy.nvim has a "shortcut" you can use.

So, this example

require('lazy').setup({
  {import = 'user.plugins'},
})

Does the same thing as this

require('lazy').setup('user.plugins')

You can call your entire plugin setup with just one line of code.
