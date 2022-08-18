# Evolutionary Games

In this project, a simple 2D minigame is implemented for the Computational Intelligence course at my university.
The agent needs to learn to maneuver via neural network + evolution algorithm.<br>


## How to play!
You can play these games by executing the following command. For changing the mode of the game, replace the `*MODE_NAME*` with desired game mode.<br>
```
python game.py --mode *MODE_NAME* --play True
```


## Learning
The agent learns via a neural network and evolution algorithm. You can watch the process of learning and behavior of the population of agents by executing the following command.
```
python game.py --mode *MODE_NAME*
```
**Options:**
- Press `Esc` to exit the game.
- Press `F` to see frame rate.
- Press `D` to double up the speed of the process.
- Press `S` to see just one agent instead of the whole population.

You can resume the evolution from the previous execution by checkpoints. By default, every 5 generations are automatically saved as a checkpoint (You can change this number in **`config.py`**). You can use checkpoint by the following command.

```
python game.py --mode *MODE_NAME* -checkpoint checkpoint/*MODE_NAME*/*GENRATION_NUMBER*
```
For example:

```
python game.py --mode helicopter -checkpoint checkpoint/helicopter/5
```


## Game Modes
Helicopter             |  Gravity          |  Thrust
:-------------------------:|:-------------------------:|:-------------------------:
![Helicopter](/screenshots/helicopter.png?raw=true)  |  ![Gravity](/screenshots/gravity.png?raw=true) | ![Thrust](/screenshots/thrust.png?raw=true)

## Contributors
- [Hossein Zaredar](https://github.com/HosseinZaredar)
- [Matin Tavakoli](https://github.com/MatinTavakoli/)
- [Parnian Rad](https://github.com/Parnian-Rad)

