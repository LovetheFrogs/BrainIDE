# BrainIDE
Welcome to BrainIDE! Following will be some information about this software as well as some help about Brainfuck itself.


## What's BrainIDE?
BrainIDE aims to provide an **easy-to-use, lightweight and user-friendly** brainfuck IDE. The main purpose of this piece of sowtware is to allow for 
brainfuck coding on the go, without the need of an Internet connection. Fully coded using python and tkinter for GUI design.

| Windows version | Linux version |
| - | - |
| ![windows](https://user-images.githubusercontent.com/102818341/170823884-9351cfff-b952-4322-851b-70c9e0b0b6b8.png) | ![linux](https://user-images.githubusercontent.com/102818341/170818959-2dbed08b-ef42-4669-b857-38568917041e.png) |

## BrainIDE's features.
BrainIDE has several features that makes it helful and easy-to-use. The most relevant ones are automatic code highlighting, keyboard shorcuts for every 
action, a text-to-brainfuck translator and a charr-to-ASCII function, as well as customizing features to change the look of your code.

For more advanced users, BrainIDE's interpreter can be changed by just cloning the repository and changing brainfuck_compiler.py with your own. **Note it 
must be renamed to _brainfuck_compiler.py_**


## How to Install BrainIDE?
Installation is as easy as it could be, just go to releases, select the last release, and download the zip file corresponding to your OS (current version 
is only supported in Windows and Linux) and follow the intructions for your own dist. You can find these instructions in the README.txt file inside the zip 
file you've downloaded!


## How to contribute?
All contributions and suggestions are welcome. If you´d like to contribute, clone the repo with:
```
git clone https://github.com/LovetheFrogs/BrainIDE
```
Send your PR's and they will be reviewed.


## Brainfuck!
Continue reading for some information regarding brainfuck and how to use it.


### What is brainfuck?
The following is extracted from the [Wikipedia page](https://en.wikipedia.org/wiki/Brainfuck) for brainfuck. If you would like a better insight into the 
history and origin of this language, I'd recommend you to head over there.

>Brainfuck is an esoteric programming language created in 1993 by Urban Müller.
>
>Notable for its extreme minimalism, the language consists of only eight simple commands, a data pointer and an instruction pointer. While it is fully 
>Turing complete, it is not intended for practical use, but to challenge and amuse programmers. Brainfuck simply requires one to break commands into 
>microscopic steps.
>
>The language's name is a reference to the slang term brainfuck, which refers to things so complicated or unusual that they exceed the limits of one's 
>understanding. 

### The language.
Brainfuck is made of two main components. An array of 30k cells and a pointer to one of its cells. When a brainfuck program begins execution, the pointer 
is placed at cell 0 and each of the cell's values are set to 0. 

The programmer can manipulate the value of a cell or move to a different one, as well as looping through a set of instructions or use input/output. In 
total, there are 8 commands as stated above. Here you can find a table detailing the function of each oone of them.

| Command | Description |
| - | - |
| **+** | Increment value of current cell by one. |
| **-** | Decrement value of current cell by one. |
| **>** | Move pointer one position to the right. |
| **<** | Move pointer one position to the left.|
| **[** | Start of a while loop, will repeat until cell pointet to is cero. |
| **]** | Marks the end of a while loop. if the cell pointet to when reached here is noncero, it loops over. |
| **.** | Used to output the ASCII value of the current cell to the screen. |
| **,** | Used to input the ASCII value of one byte to the cell pointed to. |

As one could have probably guessed by now, brainfuck uses ASCII codes to manage whats in the cell. This means that if cell 3 has the value '97', it 
actually has the letter 'a'. 

### A simple introduction to programming in brainfuck.
Below, you will learn how to write some code wich will print a letter. However, this is super simple. However, if you'd want to learn brainfuck from 
scratch, I'd recommend heading over to [**roachhd's brainfuck bacics**](https://gist.github.com/roachhd/dce54bec8ba55fb17d3a) as it deepens way more into 
the basics of this language.

Let's code a simple program in brainfuck. This one is pretty simple and its aim is just to show how to print a character. Let's say you would like to 
output 'B' to screen, you could use the following code:
```
++++++[>+++++++++++<-]>.
```
Lets break it down:

First, we set the value of the first to 6. This will be used to iterate trough a loop and avoid the hussle of havint to type in 66 plus symbols (as 'B' in
ASCII is 66 decimal).

After that, we start a while loop and move to the second cell, adding 11 to it. When we are done with that, we move back to the first cell and decrease 
it's value by one.

As we've reached the end of our loop and the current cell we're at is not 0, we iterate though again. Following there's a diagram of show the fist 3 cells
look like at the start of all the loop iterations. (Note that the pointer will be pointing to the first cell at the start of each cycle).

<p align='center'> |6|0|0| ---> |5|11|0| ---> |4|22|0| ---> |3|33|0| ---> |2|44|0| ---> |1|55|0| </p>

Lastly, we move to the second cell, wich contains the value 66, and use '.' to output it's value. If you open BrainIDE, copy the code snippet above, and
execute it, you will see that a letter **B** prints on the output box.

So, with what you have learned, you could easily write your very own Hello World! program. I'll leave one example below, so take your time to analize it.
Note that there's nos only one way to code it, so it is likely you'll see other implementations online. A commented version of the code can be found inside
the repository, under CompilerApp > Premade > HelloWorld.bf
```
>++++++++[<+++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]<.>+++++++++++[<+++++>-]<.
>++++++[<++++>-]<.+++.>++[<--->-]<.>++++[<-->-]<.>+++++++++++++++++[<---->-]<+.
```

## About.
BrainIDE is software developed by LovetheFrogs and licensed under GPL-3.0 license.
