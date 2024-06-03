 Nuke from orbit

Make sure there is no residue of any old config or attempt

rm -rf ~/.config/nvim 
rm -rf ~/.local/share/nvim 
rm -rf ~/.local/state/nvim 

Create the config folder

mkdir ~/.config/nvim
cd ~/.config/nvim
nvim .

That should leave you on nvim default config folder with nvim open on its default netrw (vims file explorer) view.

" ============================================================================
" Netrw Directory Listing                                        (netrw v171)
"   /home/fer/.config/nvim
"   Sorted by      name
"   Sort sequence: [\/]$,\<core\%(\.\d\+\)\=\>,\.h$,\.c$,\.cpp$,\~\=\*$,*,\.o$,\.obj$,\.info$,\.swp$,\.bak$,\~$
"   Quick Help: <F1>:help  -:go up dir  D:delete  R:rename  s:sort-by  x:special
" ==============================================================================
../
./

From here you can press % which means create file, you should see a Enter filename: prompt appear on the lower left corner. There you can type init.lua. This name is important as it is the file nvim will look for to read config from.

This leaves you inside that file. I you do i (for insert m ode), print("hello"), and then <esc>ZZ to save and quit, and then you execute nvim . again from bash, you will see the same screen as before but with "hello" written in the bottom left corner.

This is useless in general but useful as a checkpoint that you got all the paths and names right. I suggest deleting the print statement now before it becomes a bother.

Here Primeagen goes on to create lua folder (d from the netrw view) within the nvim one, and theprimeagen there, and then another init.lua.

He will later require all his custom config files from lua/theprimeagen/init.lua and require('theprimeagen') from the main init.lua. I don't see any advantage from this indirection so I would di this instead.

    Create lua folder ~/.config/nvim
    Create a core folder there (instead of your name, so it's easier to share around)
    Create mappings.lua in ~/.config/nvim/lua/core
    write

vim.g.mapleader = " " -- easy to reach leader key
vim.keymap.set("n", "-", vim.cmd.Ex) -- need nvim 0.8+

    Open init.lua and write require("core.mappings")
    Exit and open init.lua

If everything when right, now you can type - (instead of <esc>:Ex) and see netrw's menu.

ThePrimeagen suggests <leader>pv as the mapping to see the folder, but - comes from me being used to https://github.com/tpope/vim-vinegar some time ago. Choose your's to your liking.

After the previous steps, my folder looks like this:

$ tree
.
├── init.lua
└── lua
    └── core
        └── mappings.lua

2 directories, 2 files

$ cat init.lua 
require ("core.mappings")

$ cat lua/core/mappings.lua 
vim.g.mapleader = " " -- easy to reach leader key
vim.keymap.set("n", "-", vim.cmd.Ex) -- need nvim 0.8+

Plugin manager

we are going to use:
https://github.com/wbthomason/packer.nvim

Here I will diverge again from ThePrimeagen and sugges auto_bootstraping packer.
So go to this section
https://github.com/wbthomason/packer.nvim#bootstrapping

Copy the code block there and paste it into lua/core/plugins.lua. Then add require("core.plugins") to your init.lua file and either exit and re-open, or source it <esc>:so % (short for source ).
Fuzzy finder

We are going to take advantage of the previous step and use it to install our fuzzy finder telescope.

Wer will go to https://neovimcraft.com/plugin/nvim-telescope/telescope.nvim/index.html and scroll down to where if says "Using packer.nvim" under the Getting Started section, and copy a block of code similar to this one:

use {
  'nvim-telescope/telescope.nvim', tag = '0.1.0',
-- or                            , branch = '0.1.x',
  requires = { {'nvim-lua/plenary.nvim'} }
}

The we will go to lua/core/plugins.lua file, look for the part that looks like:

  -- My plugins here
  -- use 'foo1/bar1.nvim'
  -- use 'foo2/bar2.nvim'

and replace it with the telescope block.
You can now save, source the file and run :PackerSync and you got yourself telescope installed.

You can use :Telescope find_files<cr> to check that the plugin is installed and works ok.

Telescope commands are a bit wordy, so next you will create a new folder path: ~/.config/nvim/after/plugin (also auto loaded by nvim).

Then you will scroll to Usage on the telescope page, look to the Using Lua part and copy it:
```
local builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff', builtin.find_files, {})
vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})
vim.keymap.set('n', '<leader>fb', builtin.buffers, {})
vim.keymap.set('n', '<leader>fh', builtin.help_tags, {})
```
My recommendation is to come up with your own set of mappings for this instead of trying to remember these.

If you add desc params to the mappings and then use Telescope keymaps then you will be able to find commands per your own description of what they do. I suggest you have a sneak peek at my telescope config to see an example and come up with your own mnemonics.
Colorscheme

Another good use of the plugin system is installing your favourite colorscheme, this is very personal, Theprimeagen uses rose-pine, I choose jellybeans. A good point to realize you can use VimL

Add this to you plugins file (under the last use block you added):

use({ 'nanotech/jellybeans.vim' })

Source the file, run :PackerSync

Add this to ~/.config/nvim/after/plugin/colors.lua

--
-- COLORS --
--

vim.opt.termguicolors = true

function SetColor(color)
    color = color or "jellybeans" -- have a default value
    vim.cmd.colorscheme(color)

    vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
    vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    vim.api.nvim_set_hl(0, "ColorColumn", { bg = "#330000" })
end

SetColor() -- run at startup

Treesitter

Similar to the color part:
Add this to plugins.lua

use('nvim-treesitter/nvim-treesitter', { run = ':TSUpdate'})

got to https://github.com/nvim-treesitter/nvim-treesitter#modules Copy the code block there, paste it into a new file on after/plugin/treesitter.lua and edit to your convenience, specifically, adding languages tgou use to ensure_installed, and commenting or deleting the ignore_install line unless you need it.

If you are into compilers/ASP look into https://github.com/nvim-treesitter/playground and catch ThePrimeagen's vide around this timestamp.
Additional plugins

There are some more plugins that you might find very helpful, at this point you should be able to install and set up a plugin by yourself based on the previous examples, so i will leave the links here for you to practice:

    Undotree a visual interface to your undo (allowing for branching).
    Fugitive Tim pope's git integration
    Commentary Tim pope's comment plugin
    Git gutter Git status signs in the gutter (leftmost column)

Set options

If you had an existing .vimrc config before, chances are that you were setting a lot of vim's options to your liking

To that effect, you can create a lua/core/options.lua file and require it from init.lua adding require("core.options").

Here you have mine, but as these are very personal. be sure to chose yours. For the most part you can run :help option_name replacing option_name with whatever comes after vim.opt. on this file and read about what it does.
Mappings

Similarly, you will want to have your own key mappings. I recommend you keep plugin-specific key-mappings under after/plugin/<plugin-name>.lua so that they are easir to find and delete in case you decide to stop using some plugin if it gives you trouble.

Like I did before, here you have my mappings and a recommendation to come up with your own instead of copying anyone else's.