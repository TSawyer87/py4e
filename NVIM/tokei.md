---
id: tokei
aliases: []
tags: []
---

# tokei

- Get a report on the code in a directory and all subdirs:

```bash
tokei [path/to/directory]
```

- Get a report for a directory excluding .min.js files:

```bash
tokei [path/to/dir] -e [*.min.js]
```

- Print out statistics for individual files in a directory:

```bash
tokei [path/to/dir] --files
```

- Get a report for all files of type Rust and Markdown

```bash
tokei [path/to/dir] -t=[Rust],[Markdown]
```
