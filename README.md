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
⍆ - Hop over next character.
⍋ - Pop string from stack, push first character, push rest of string.

+·     - Add, Multiply.
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

     If you have nested switches, and one of the rows of the outer switch case
     violently rams into the middle of the inner switch case,
     it will jump to the row of code after the entire switch.

[] - Code block.
         NOTE: While the interpreter i made ignores ] entirely,
               omitting it is UB.

f - Declare a function. it is followed by a single character, the function's name, 
                        after that a code block implementing the function.
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
You /might/ be able to do something with loops and switch-case to emulate a turing machine, but i'm WAY too lazy to do that, so good luck!
