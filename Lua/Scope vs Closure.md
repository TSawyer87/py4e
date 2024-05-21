Scope vs. Closure:

**Scope**: The scope of a function defines the visibility of variables within that function and any nested blocks of code. Variables declared within a scope are only accessible within that scope (unless explicitly passed or returned).

**Closure**: A closure is a special type of function that, in addition to its own code, captures variables from its enclosing scope, even if the enclosing code has already finished executing. This allows the closure to access and use those variables even when it's called outside of that scope.

Function vs. Closure (Not All Functions Are Closures):

- Not every function defined within a scope becomes a closure. A function becomes a closure only if it needs to access variables from its enclosing scope.
- If a function doesn't rely on any variables outside its own scope, it's just a regular function and doesn't capture any variables.

Understanding the "End" of a Function:

The `end` statement in Lua marks the end of a code block, typically a function or a block defined with `do ... end.`
    However, the "end" doesn't necessarily determine the lifetime of captured variables in a closure.

Here's an analogy:

Imagine a library (the enclosing scope). It has different sections (inner scopes) containing books (variables). A librarian (a closure) can borrow a book (variable) from their section (scope) and take it with them (even if the library closes). The "end" of the library's day (function) doesn't mean the librarian has to return the borrowed book.

Example:
Lua
```lua
-- Not a closure (no captured variables)
function add(x, y)
  local sum = x + y
  return sum
end

-- Closure (captures variable 'initialValue')
function createAdder(initialValue)
  local count = initialValue  -- captured variable

  function add(value)
    count = count + value
    return count
  end

  return add  -- return the inner function (the closure)
end
```
Use code with caution.

In this example:

    `add(x, y) ` is a regular function, not a closure. It doesn't need to access any variables outside its own scope.
    createAdder creates a closure. The inner function add captures the local variable count from its enclosing scope (createAdder). Even after createAdder finishes executing, the closure remembers the value of count.



1. What Are Closures?

- In Lua, a closure is a function object that has access to variables from its parent scope, even after the parent function has terminated.
- Essentially, closures allow you to add an extra layer of power and flexibility to your Lua code by enabling functions to carry data around with them.

2. Why Learn Closures?

- Closures are fundamental building blocks in Lua and play a vital role in game development and scripting.
- Their power lies in their ability to foster cleaner, more organized code by allowing functions to remember and manipulate data over time.

3. Creating a Simple Lua Closure:

Let’s start with a basic example:
```lua
function outerFunction()
    local x = 5
    local innerFunction = function()
        print(x)
    end
    return innerFunction
end

local closure = outerFunction()
closure()  -- Prints 5

```
- Here, `innerFunction` is a closure because it can access the `x` variable from its parent function, even after `outerFunction` has finished executing.

4. **Manipulating Variables Within a Closure**:
	- Closures allow you to manipulate variables within a function.
	- For instance, you can use an anonymous function (closure) to sort a list of student names based on their grades:

```lua
names = {"Peter", "Paul", "Mary"}
grades = {Mary = 10, Paul = 7, Peter = 8}

table.sort(names, function(n1, n2)
    return grades[n1] > grades[n2]
end)

```

5. **How Closures Work**:
	- - When you create a closure, it captures the necessary variables (upvalues) from its parent scope.
	- Even if the parent function has returned, the closure still has access to these variables.
	- For example:
```lua
function newCounter()
    local i = 0
    return function()
        i = i + 1
        return i
    end
end

local c1 = newCounter()
print(c1())  -- 1
print(c1())  -- 2

```

6. **Multiple Closures & Independent Variables**:
	- Each closure is independent, even if they share the same function.
	- If you call `newCounter` again, it creates a new local variable `i`, resulting in a new closure:
```lua
local c2 = newCounter()
print(c2())  -- 1
print(c1())  -- 3
print(c2())  -- 2

```
7. **Conclusion**:
	- Closures provide a valuable tool for cleaner code, higher-order functions, and fancy programming techniques.
	- Understanding closures is essential for confident Lua programming and game development.