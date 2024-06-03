Parsers are searched for as `parser/{lang}.*` in any 'runtimepath' directory.
If multiple parsers for the same language are found, the first one is used.
(NOTE: This typically implies the priority "user config > plugins > bundled".)

To load a parser from its filepath: >lua

    vim.treesitter.language.add('python', { path = "/path/to/python.so" })
<
Parser names are assumed to be lower case if the file system is
case-sensitive.
