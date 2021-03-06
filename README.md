# Python Calculator

This is my first project with Python. Challenge provided by Turing college, where I started to learn coding recently. The program performs main calculator
actions - addition/subtraction, multiplication/division and nth root of a number.

## Description

The program is written using POOP (Python Object Oriented Programming) code. The program has its own memory and can be reset any time user wants, this means 
that program starts with value of zero (0) and the user can perform any of previously mentioned actions.

## Getting Started

### Installing

Use the package manager pip to install calculator package like below.

pip install git+https://github.com/Joneckiz/calculator.git

### Executing program

Once the package is installed the user should:
* Import calculator module
* Create new objective
* Perform calculation actions

```
from calculator import calculator as calc

calc = calc.Calculator() # new object created

calc.addition(15) # returns 15.0
```
## Performance

```
calc.addition(15) # adds 15 to the memory, which was 0 once program started, returns 15

calc.subtraction(5) # subtracts 5 from memory, which was 15, returns 10

calc.multiplication(10) # multiplies memory by 10, returns 100

calc.division(4) # divides memory by 4, returns 25

calc.root(2) # square roots memory, returns 5

calc.reset() # resets calculators memory to 0
```

## Authors

Jonas Vengalis

jovengalis@gmail.com


## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
