# 📖 Linux Shell Scripting: Logic, Conditionals, and Loops

Detailed study notes and command references based on Episode 18 of the Linux Learning Series.

---

## 1. Introduction to Scripting Logic
Conditional structures and loop modules let scripts analyze conditions dynamically and process repetitive sets of actions efficiently. While logic maps perfectly to languages like Python or Java, you must strictly follow the native syntactical rules unique to the Linux shell.

---

## 2. Conditional Statements (IF, ELSE, ELIF)
Conditional blocks run target code segments only if specified logical or numerical criteria evaluate to true.

### Standard IF Structure
An `if` statement evaluates a target comparison expression wrapped in standard square brackets `[ condition ]`. You must cleanly close every active statement sequence block using the tracking terminator keyword `fi` to avoid a critical interpreter syntax fault.

```bash
#!/bin/bash
# Evaluating a standard hardcoded integer condition
num=10

if [ \$num -gt 5 ]; then
    echo "\$num is greater than 5"
fi
```

### IF-ELSE Structure
The `else` intercept handles script fallback actions if the primary parameter validation rule falls through.

```bash
#!/bin/bash
# Adding interactive data parsing via target prompts
echo "Please enter the number:"
read number

if [ \$number -gt 5 ]; then
    echo "\$number is greater than 5"
else
    echo "\$number is less than or equal to 5"
fi
```

### IF-ELIF-ELSE Structure
You can chain multiple conditions sequentially using the `elif` directive when tracking variable outcomes beyond a binary true/false state.

```bash
#!/bin/bash
echo "Enter your number:"
read number

if [ \$number -lt 10 ]; then
    echo "Number is less than 10"
elif [ \$number -eq 20 ]; then
    echo "Number is exactly 20"
else
    echo "Number is greater than 10 but not 20"
fi
```

---

## 3. Shell Scripting Operators Reference
The shell relies on exact flag codes inside evaluation blocks to process mathematical logic, string matches, or combined multi-rule expressions.

### Integer Comparison Flags

| Operator Flag | Meaning | Example Logic |
| :--- | :--- | :--- |
| `-eq` | Equal to | `[ $num -eq 10 ]` |
| `-ne` | Not equal to | `[ $num -ne 20 ]` |
| `-gt` | Greater than | `[ $num -gt 5 ]` |
| `-lt` | Less than | `[ $num -lt 30 ]` |
| `-ge` | Greater than or equal to | `[ $num -ge 10 ]` |
| `-le` | Less than or equal to | `[ $num -le 30 ]` |

### String Comparison Flags
Shell operations processing text match sequences are completely case-sensitive.
* **`=` or `==`**: Evaluates if two strings match identically.
* **`!=`**: Evaluates if string characters do not match.
* **`-z`**: Checks if the target string evaluates to null or empty.
* **`-n`**: Checks if the target string evaluates to non-null or contains text data.

### Logical Operators
* **`&&` (Logical AND)**: Dictates that both independent expression checks must validate as true for the master loop statement block to run.
  ```bash
  # Validating an integer target safely within a bounded range
  if [ \(number -gt 10 ] && [\)number -le 30 ]; then
      echo "\$number is strictly between 10 and 30"
  fi
  ```

---

## 4. Loop Mechanics (FOR, WHILE, UNTIL)
Loops automate repetitive operations smoothly by repeating a target syntax block until a specific state threshold is reached.

### The FOR Loop
Iterates directly over defined linear values, continuous integer boundaries, step distributions, or target file lookups.

#### Iterating Over Strings or Lists
```bash
#!/bin/bash
# Traverses a raw explicit string sequence
for item in apple banana cherry mango kiwi
do
    echo "Fruit is: \$item"
done
```

#### Iterating Over Integer Ranges and Step Spaces
```bash
#!/bin/bash
# Simple bounded iteration (Loops 1 to 5 sequentially)
for i in {1..5}
do
    echo "Value: \$i"
done

# Step-skipping iteration syntax: {Start..End..IncrementStep}
# This splits values from 1 up to 10 by jumping 2 values each time
for step_val in {1..10..2}
do
    echo "Odd Number: \$step_val"
done
```

#### Iterating Over System Files (Wildcard Globbing)
You can leverage wildcard mechanics (`*`) inside loop blocks to capture, parse, and process directory objects matching standard extension suffixes.
```bash
#!/bin/bash
# Locates and tracks text/sh  files inside your local working path using *.txt or *.sh
for file in *.txt
do
    echo "Processing text file entry: \$file"
done
```

### The WHILE Loop
Runs code segments continuously as long as its evaluation condition returns a valid true state.

```bash
#!/bin/bash
# Standard numerical decrement tracking loop
echo "Enter a starting counter integer:"
read counter

while [ \$counter -ge 0 ]
do
    echo "Countdown position: \$counter"
    counter=\$((counter - 1))
done
```

#### Advanced Use-Case: Stream Parsing Files Line-by-Line
```bash
#!/bin/bash
# Reads an external target configuration or file linearly
line_num=1

while read -r current_line
do
    echo "Line \(line_num:\)current_line"
    line_num=\$((line_num + 1))
done < basic_script.sh
```

### The UNTIL Loop
The exact structural inverse of a `while` loop. It processes the block continuously while the evaluation constraint remains false, terminating immediately when the condition shifts to true.

```bash
#!/bin/bash
counter=1

# Block terminates the exact moment counter evaluates higher than 5
until [ \$counter -gt 5 ]
do
    echo "Count position: \$counter"
    counter=\$((counter + 1))
done
```

---

## 5. Loop Control & Advanced Structure
* **`break`**: Instantly terminates execution of the enclosing loop, dumping processing flow directly to lines below the loop boundary.
* **`continue`**: Skips the remaining operations inside the current loop iteration and immediately restarts the next logical evaluation check.

### Nested Loops Module
You can nest looping workflows within one another to generate multi-dimensional arrays, data mappings, or matrix grids.
```bash
#!/bin/bash
# Generating nested matrix processing tracking routes
for i in {1..3}
do
    for j in {1..2}
    do
        echo "Matrix Coordinate Map -> Outer: i, Inner: j"
    done
done

# Other way to write it
for i in {1..3}; do
    for j in {1..2}; do
        echo "Matrix Coordinate Map -> Outer: i, Inner: j"
    done
done
```
