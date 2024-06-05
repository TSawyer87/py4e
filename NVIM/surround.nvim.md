---
id: surround.nvim
aliases: []
tags: []
---

Surround.vim is all about "surroundings": parentheses, brackets, quotes, XML tags, and more. The plugin provides mappings to easily delete, change and add such surroundings in pairs.

It's easiest to explain with examples. Press `cs"` inside
-- TODO : Hello world!

```md
"Hello world!"
```

to change it to

```md
'Hello world!'
```

Now press `cs'<q>` to change it to

```md
<q>Hello world!</q>
```

To go full circle, press `cst"` to get

```md
"Hello world!"
```

To remove the delimiters entirely, press `ds"`.

```md
Hello world!
```

Now with the cursor on "Hello", press `ysiw]` (iw is a text object).

```md
[Hello] world!
```

Let's make that braces and add some space (use `}` instead of
`{` for no space): `cs]{`

```md
{ Hello } world!
```

Now wrap the entire line in parentheses with `yssb` or `yss)`.

```md
({ Hello } world!)
```

Revert to the original text: `ds{ds)`

```md
Hello world!
```

Emphasize hello: `ysiw<em>`

```md
<em>Hello</em> world!
```

Finally, let's try out visual mode. Press a capital V (for linewise visual mode) followed by
`S<p class="important">`.

```md
<p class="important">
  <em>Hello</em> world!
</p>
```

This plugin is very powerful for HTML and XML editing, a niche which currently seems
underfilled in Vim land. (As opposed to HTML/XML inserting, for which many plugins are available).
Adding, changing, and removing pairs of tags simultaneously is a breeze.

The . command will work with ds, cs, and yss if you install repeat.vim.

```

```
