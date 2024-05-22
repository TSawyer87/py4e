## Comments
```lua

-- This is a single line comment.

--[[
     This is a multi-line comment.
--]]
```
## Variable Scope

All variables are considered **`global`** unless explicitly declared as **`local`**. The scope of local variables is limited in the [**chunk**](https://www.lua.org/pil/1.1.html) in which they appear in. Lua usually interprets each line that we type in _interactive mode_ as a complete chunk or expression. This implies that a variable declared `local` in one line is out of scope in the next line. We can create local chunks by using the **`do`** and **`end`** keywords. This works because if the interpreter detects that the line is not complete, it waits for more input, until it has a complete chunk.
```lua

var = 10 -- global
print( "Global var:", var ) --> 10

do
    local var = 20 -- local
    print( "Local var:", var ) --> 20
end

print( "Global var:", var ) --> 10
```
## Variable Assignment

- Lua does not offer syntactic sugar for **augmented assignments**. That is, we must explicitly write `a = a + 1` instead `a += 1`.
    
- Lua does not offer syntactic sugar for **chained assignments**. That is, instead of `a = b = 0`, each variable assignment must be written separately.
    
- Lua supports **parallel assignment**. For example, `a, b, c = 0, 0, 0`.
    

## Variable Types

There are eight basic types in Lua: _nil_, _boolean_, _number_, _string_, _userdata_, _function_, _thread_, and _table_.

- A _nil_ value represents the absence of data. If you try to access a variable that has not been created yet, its value will be _nil_. If you are done using a variable, you can assign it to _nil_ to delete it.
- Until version 5.2, Lua represented all numbers using double-precision floating-point format. Starting with version 5.3, Lua uses two alternative representations for numbers: 64-bit integer numbers (called _integer_), and double-precision floating-point numbers (called _float_).

**NOTE**: Any arithmetic operation applied to a _string_ will attempt to convert this _string_ to a _number_. Conversely, whenever a _string_ is expected and a _number_ is used instead, the _number_ will be converted to a _string_. This can also be done manually using the `tostring` and `tonumber` functions.
```lua

print( type("Hello")   )  --> string
print( type(10.4*3)    )  --> number
print( type({1, 2, 3}) )  --> table
print( type(print)     )  --> function
print( type(true)      )  --> boolean
print( type(nil)       )  --> nil
```

