# DOCUMENTATION

## OPERATION

Oats programs take place in a 2d grid, with an instruction pointer that will NOT wrap around, but instead fall off and halt execution.
What could be more visual than a 2d programming language?

## NOTATION

```
⊤⊥     - True/False.
NUMBER - Push number to the stack.
"TEXT" - Push text to the stack.

⌃ - Pop from stack and print to stdout.
⌄ - Read from stdin and push to stack.
⌥ - Duplicate top element of stack.
⌀ - Ditch the top element of the stack.
⤵ - Swap top two elements of the stack.
⍖ - Put top element of the stack at the bottom.
⍏ - Put bottom element of the stack at the top.
⍆ - Hop over next character.
⍋ - Pop string from stack, push first character, push rest of string.

+·     - Add, Multiply.
             NOTE: + can also concatenate strings together
–/     - Negate, Reciprocal.
             NOTE: - is NOT negate. – is negate. - vs –.
=≠<>≤≥ - Comparison operators.
¬∧∨    - Logical operators. NOT, AND, and OR respectively.
             NOTE: If you call the top of the stack X, and the element directly under it Y,
                   the binary operators put Y on the left, and X on the right.
             NOTE: ∧, ⌃, and ^ all have seperate meanings.
                   and so do ⌄, v, and ∨.
⎡⎤ - Switch-case. Pop top element of stack,
⎢⎥   Top row executes if zero, Next row executes if one, etc...,
⎣⎦   Last row executes if none of the above apply.

     After the switch-case row finishes executing, the execution is returned back 
     to right after the end of the top row of the switch case.
     If you have nested switches, and one of the rows of the outer switch case
     violently rams into the middle of the inner switch case,
     it will jump to the row of code after the entire switch.

[] - Code block.
         NOTE: While the interpreter I made ignores ] entirely,
               omitting it is UB.

λ - Declare a function. it is followed by the function's name and 
                        a code block implementing that function.
          NOTE: redeclaring a function is illegal 

⎫
⎬ - Loop current switch statement.
⎬
⎭

} - Loop current code block.

ℝ - Cast to float.
ℤ - Cast to integer.
ℙ - Cast to string.
```

## IS IT TURING COMPLETE?

> **TL;DR**: yes, the language is turing-complete.

The language is turing-complete if it can perform any action that a classical Turing Machine can do.
In the Oats language we can move freely to any cell in the stack using `⍏` and `⍖` operators and change the value of that cell with `⌀` operator (followed by the new value of that cell). We can also freely add new cells to the stack and branch to a different set of instructions depending on the value of the cell with the _**switch-case**_ operator. Each branch can be thought of as a different state the Turing Machine can be in. Finally we can branch to a state we have already been in (a.k.a jump program execution to an earlier point in the code) with the _**loop**_ operators.

These are all the actions that a classical Turing Machine can do, so (if the stack is unlimited in size) this language is in fact turing-complete.

### Limited stack size case:

If the stack size is limited, then the language can still be turing-complete, but only if the stack cells can hold unbounded numerical values. In this case to prove turing-completness we need to emulate a Minsky Machine [[1]](https://esolangs.org/wiki/Minsky_machine). Minsky Machine is turing-complete if it has at least two unbounded numerical cells and implements the following functions for each such cell:

1. Increment the current cell (the one on top of the stack):
```
λinc[1+]
```

2. If current cell is equal to zero then return true, else decrement and return false:
```
λjzdec[⌥⎡   ⊤⎤]
        ⎣1–+⊥⎦
```

> _* by 'return' I mean that the function pushes the return value onto the stack. The function call can be immidietaly followed by a switch-case instruction to do branching paths depending on the return value of that function._

We can place two unbounded cells on top of the stack and then swap between them with:
```
λswap[⤵]
```

The language is therefore turing-complete even with limited stack size, if it contains (at least) two cells that can hold unbounded numerical values.

## Brainfuck example:

I have created this conversion table that can convert any valid Brainfuck program into an equivalent Oats program [(example)](examples/brainfuck). Since Brainfuck is turing-complete, this table proves beyond any shadow of the doubt that Oats is also turing-complete.

> [!NOTE]
> There is no easy way to convert ASCII codes to characters in Oats, so the output command just prints the raw ASCII code to the console with space for better readability. However it is possible in Oats to create a giant _**switch-case**_ that will convert each ASCII code to it's appropriate character, so the language is still turing-complete.

|Brainfuck|Oats|Notes|
|-|-|-|
|_start of the program_|`""0`|This instruction marks the beginning of the stack with `""` and then adds a single cell initialized with value 0.|
|`>`|<pre><code>⍏⌥""≠⎡⍖0⎤</code><br><code>     ⎣  ⎦</code></pre>|This instruction dynamically adds new cells to the stack if necessary, initialized with value 0.|
|`<`|`⍖`||
|`+`|`1+`||
|`-`|`1–+`||
|`.`|`⌥⌃" "⌃`|_( see the note above )_|
|`,`|`⌀⌄ℤ`||
|`[`|<pre><code>⌥0=⎡</code><br><code>   ⎣</code></pre>||
|`]`|<pre><code>⌥0=⎡⎤⎫⊥⎡⎤</code><br><code>⍆⎦⍆⎣    ⎦</code></pre>||
