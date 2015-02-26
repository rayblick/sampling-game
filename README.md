# sampling-game

This program was designed to give the player an appreciation for sample size, and several other ideas like power to detect change in a population. Currently the game is set up so that the player is required to guess what sample size (N) they would need in order to find a significant difference (power = 80% and alpha = 5%) in the population (estimated by the mean and standard deviation) given a certain % of loss.  

The game is based on an equation (specifically, n=((alpha+beta)/(x1-x2)/sd)^2) that has several fixed terms, such as alpha and beta, and several randomly generate population sizes and distributions.

## command-line version

This program is written in `python 3.4`. Copy and paste to an IDE and run in console. Alternatively, save the file (e.g. sample_game.py) and run at the command line. On windows OS, open the start menu and type cmd in the search bar and hit enter. Navigate to the directory of the script (in this case sample_game.py) and type **python sample_game.py**. The game will run once and exit. Further effort is needed to create a user interface and to make the program executable without using the code.  

## Updated GUI version

To run the updated GUI version of this game you will need to download and unzip from the master branch and then follow the instructions below for your specific OS.

**Windows:**

  - *under construction...*

**Linux:**

  - Make sure you have `python 3.4` and the `python3-tk` package installed.
  - to run the newer GUI version of the game run the script `sample_size.py` from the terminal:

```sh
./sample_size.py
```

  - if the script needs to be made executable run this line of code before running above:

```sh
chmod +x sample_size.py
```

**MacOS**

  - *under construction...* (should work in same manner as Linux though)

### Example
### Game start
For power=80% and alpha=0.05% 

The population mean is 29 and the SD is 5 

Guess the sample size required to detect a loss of 8%


Guess N: 10 

### Output
The calculated N was: 31

You have underestimated the number of samples by: 21

You would need 31 samples to detect a loss of 9%




