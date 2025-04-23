
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#future-Extensions">Future Extensions</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#how-to-use">How To Use</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## 📘About The Project

It is a Basic Interpreter written in Python language. It is capable of handling basic arithmetic expressions and execute basic operations like addition, substraction, multiplication and dividation. It is also able to parse numbers and variables.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀Features
* Tokenizes input expressions (`2 + 3 * (4 - 1)`)
* Builds an Abstract Syntax Tree (AST)
* Evaluates the expression using a recursive evaluator
* Supports variables

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🔮Future Extensions
* Equation solving and multi-variable support
* Advanced mathematical functions (e.g., log, sqrt)
* Better variable storage with scopes or environment frames

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🏗️Project Structure

* mini_interpreter/
    * interpreter/
        * __init__.py   (_Initializes the interpreter package_)
        * lexer.py     (_Tokenizes the input string_)
        * parser.py    (_Converts tokens into an AST_)
        * evaluator.py (_Evaluates the AST_)
    * tests/
        * test_interpreter.py
        * test_lexer.py
    * interpreter.py     (_ Main entry point of the program_)
    * README.md          (_Project overview and usage guide_)
    * LICENSE
    * tests.sh           (_Script to run the Python tests using unittest_)



### 🦫Built With



* Python 3
* unittest
* Regex
* Recursive Descent Parsing

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## 🎬Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Make sure you have Python 3 installed.
📦 Install Python 3 if not:
* macOS
  ```sh
  brew install python
  ```
* Ubuntu
  ```sh
  sudo apt update
  sudo apt install python3 python3-pip
  ```
* Windows:
  ```sh
  ** Go to python.org/downloads
  ** Download the latest version for Windows
  ** Run the installer and check "Add Python to PATH"
  ```


### Installation

_Please follow the instructions below to clone and run the code_

1. Clone the repo
   ```sh
   git clone https://github.com/mov360/Mini-Interpreter.git
   ```
2. Navigate to the project repository
   ```sh
   cd Mini-Interpreter
   ```
3. Run the interpreter
   ```sh
   python3 interpreter.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- How To Use EXAMPLES -->
## 📑How To Use

Once you run the interpreter, you can start typing arithmetic expressions directly into the terminal.  
Please use only the following operators: `+`, `-`, `*`, `/`, `(`, `)`, and write the expression in a single line.  
Example: `2 + 3 * (4 - 1)`  

⚠️ Do not input `'exit'` unless you want to close the program.


```bash
    $ python3 main.py
    Welcome to Mini Interpreter!
    Type your expression or 'exit' to quit.

    >>> 2 + 3 * 4
    14

    >>> (10 - 2) / 2
    4.0

    >>> 7 + (6 * 5^2 + 3)  # Invalid syntax as ^ is not supported
    Error: Unknown character: ^

    >>> exit
    Goodbye!
  ```

💡 Note: Currently, variables are not supported in the expression input.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## 🪪License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Mohammad Ullah  - ullahm2004@gmail.com

Project Link: [MINI INTERPRETER](https://github.com/mov360/Mini-Interpreter.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


