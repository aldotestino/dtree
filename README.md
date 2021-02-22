# dtree

## Show the directory structure in the terminal

## Installation
* Download or clone this repo

* ### Windows
  * Change the path of ```dtree.py``` in ```bin/dtree.bat``` file
  * Add ```dtree.bat``` in the system Path (Enviroment variables)

* ### Unix
  * Open your shell profile (```.zshrc```, ```.bashrc```...)
  * At the end of the file add the alias
    ```sh
    alias dtree="python3 ~/path/to/dtree.py ./"
    ```

## Usage
* Open your terminal in a directory and digit
  ```sh
  dtree
  ```
* To define the depth (the default depth is 0)
  ```sh
  dtree 2
  ```