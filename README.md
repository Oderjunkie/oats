# DOCUMENTATION

## OPERATION

Oats programs take place in a 2d grid, with an instruction pointer that will NOT wrap around, but instead fall off and halt execution.

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
             NOTE: If you call the top of the stack X, and the element directly under it Y, the binary operators put Y on the left, and X on the right.
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

⎫
⎬ - Loop current switch statement.
⎬
⎭

} - Loop current code block.

ℝ - Cast to float.
ℤ - Cast to integer.
ℙ - Cast to string.
```

# EXAMPLE PROGS

## HELLO WORLD
```
"Hello, World!"⌃
```
---
```
"..." - "Hello, World!" -> stack
⌃     - stack -> stdout
```
## TRUTH MACHINE
```
⌄ℤ⌥⎡ ⌃⎤
   ⎢⌥^⎬
   ⎣  ⎦
```
---
```
⌄ - stdin -> stack
ℤ - int
⌥ - dup
⎡ - case 0:
      ⌃ - stack -> stdout
      ⎤ - exit case
⎢ - case 1:
      ⌥ - dup
      ⌃ - stack -> stdout
      ⎬ - loop case
⎣ - default:
      ⎦ - exit case
```
## 99 BOTTLES OF BEER
```
99[⌥⌃" Bottles of beer on the wall,\n"⌃⌥⌃" Bottles of beer!\nTake one down, pass it around,\n"⌃1–+⌥1=⎡⌥⌃" Bottles of beer on the wall!\n\n"⌃                                                                                                                                                                                                                                          ⎤}
                                                                                                     ⎣"1 Bottle of beer on the wall!\n\n1 Bottle of beer on the wall,\n1 Bottle of beer!\nTake one down, pass it around,\n0 Bottles of beer on the wall!\n\n0 Bottles of beer on the wall,\n0 Bottles of beer!\nGo to the store and buy some more,\n99 Bottles of beer on the wall!"⌃⍆⎦
```
---
```
99     - 99 -> stack
[ - default:
    ⌥⌃      - stack -> stdout (&preserve)
    "..."⌃  - " Bottles of beer on the wall,\n" -> stdout
    ⌥⌃      - stack -> stdout (&preserve)
    "..."⌃  - " Bottles of beer!\nTake one down, pass it around,\n" -> stack -> stdout
    1–+⌥1=⎡ - if (--stack == 1):
        ⌥⌃     - stack -> stdout (&preserve)
        "..."⌃ - " Bottles of beer on the wall!\n\n" -> stack -> stdout
        ⎤      - exit case
    ⎣      - else:
        "..."⌃ - "1 Bottle of beer on the wall!\n\n1 Bottle of beer on the wall,\n1 Bottle of beer!\nTake one down, pass it around,\n0 Bottles of beer on the wall!\n\n0 Bottles of beer on the wall,\n0 Bottles of beer!\nGo to the store and buy some more,\n99 Bottles of beer on the wall!" -> stack -> stdout
        ⍆      - hop over next character
        ⎦      - exit case (hopped)
} - loop (sidestepped when bottle amount reaches 1)
```
## IS IT TURING COMPLETE?
You /might/ be able to do something with loops and switch-case to emulate a turing machine, but i'm WAY too lazy to do that, so good luck!
