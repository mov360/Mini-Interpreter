
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
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
## About The Project

It is a Basic Interpreter written in Python language. It is capable of handling basic arithmetic expressions and execute basic operations like addition, substraction, multiplication and dividation. It is also able to parse numbers and variables.

The logics related the variables are still under development. I hope to add more functional supports to it in near future by adding equation solving, logarithomic operations and so on.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features
* Tokenizes input expressions (`2 + 3 * (4 - 1)`)
* Builds an Abstract Syntax Tree (AST)
* Evaluates the expression using a recursive evaluator
* Supports variables

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Structure

mini_interpreter/
│
├── interpreter/
│   ├── __init__.py
│   ├── lexer.py        # Tokenizes the input string
│   ├── parser.py       # Converts tokens into an AST
│   └── evaluator.py    # Evaluates the AST
│
├── tests/
│   ├── test_interpreter.py
│   └── test_lexer.py
├── interpreter.py     # Main entry point of the program
├── README.md          # Project overview and usage guide
└── tests.sh


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With



* Python 3
* 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

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

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- How To Use EXAMPLES -->
## How To Use

Once you run the interpreter, you can start typing arithmetic expressions directly into the terminal.
Please use only +,-,*,/ operations and write it in a same line. Example expression: 2    + 2*3
Please do not write or input 'exit' unless you want to close the program.

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
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Mohammad Ullah  - ullahm2004@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


