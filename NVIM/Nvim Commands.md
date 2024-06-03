# Changing text

 `c` can be used to change text from the cursor:

`cw` = (change to the end of a word). You can replace the word with a longer or shorter word. `cw` can be thought of as "delete the word marked and insert new text until `ESC` is pressed"

`c2b` = Back two words

`c$` = To the end of the line

`c0` = To the beginning of the line

`cc` = Change entire line

`C` = Replace characters from the current cursor position to the end of line. Same effect as `c$`

`r` = replace a single character with another single character. You don't have to press `ESC` to return to command mode after making an edit.

`R` replace in *overstrike mode*
# Substituting text

`s` by itself, replaces a single character. With a preceding count, you can replace that many characters. You can think of `s` being like `r`, but going into insert mode instead of directly replacing the specified character(s).

`S` Deletes the entire line, no matter where the cursor is. The editor puts you in insert mode at the beginning of the line. `S` and `cc` are effectively equivalent.

# Changing Case

`~` the tilde command changes a lowercase letter to uppercase or an uppercase letter to lowercase.

# Deleting Text

`dw` = delete from cursor to beginning of next word including the space.

`dW` = delete word including quotes and punctuation

`de` = delete from cursor to end of word excluding the space.

`dd` = delete whole line

`db` = delete backward

`d0` = delete from cursor to beginning of line.

`d$` = delete from cursor to end of line.

`D` = delete from the cursor to the end of the line.(D is a shortcut for `d$`)

