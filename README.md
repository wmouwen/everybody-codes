# Everybody Codes

This repository contains a set of solutions to the problems published by the events
at [Everybody Codes](https://everybody.codes/).

The repository contains a mixture of different programming languages. Solutions are made to read from `stdin` and output
to `stdout`.

## Events

### 2024 - The Kingdom of Algorithmia

| Quest | Name                         | Problem                                              | Solution               | Ducks |
|------:|:-----------------------------|:-----------------------------------------------------|:-----------------------|:------|
|     1 | The Battle for the Farmlands | [link](https://everybody.codes/event/2024/quests/1)  | [link](events/2024/1)  |       |
|     2 | The Runes of Power           | [link](https://everybody.codes/event/2024/quests/2)  | [link](events/2024/2)  |       |
|     3 | Mining Maestro               | [link](https://everybody.codes/event/2024/quests/3)  | [link](events/2024/3)  |       |
|     4 | Royal Smith's Puzzle         | [link](https://everybody.codes/event/2024/quests/4)  | [link](events/2024/4)  |       |
|     5 | Pseudo-Random Clap Dance     | [link](https://everybody.codes/event/2024/quests/5)  | [link](events/2024/5)  |       |
|     6 | The Tree of Titans           | [link](https://everybody.codes/event/2024/quests/6)  | [link](events/2024/6)  |       |
|     7 | Not Fast but Furious         | [link](https://everybody.codes/event/2024/quests/7)  | [link](events/2024/7)  |       |
|     8 | A Shrine for Nullpointer     | [link](https://everybody.codes/event/2024/quests/8)  | [link](events/2024/8)  |       |
|     9 | Sparkling Bugs               | [link](https://everybody.codes/event/2024/quests/9)  | [link](events/2024/9)  |       |
|    10 | Shrine Needs to Shine        | [link](https://everybody.codes/event/2024/quests/10) | [link](events/2024/10) |       |
|    11 | Biological Warfare           | [link](https://everybody.codes/event/2024/quests/11) | [link](events/2024/11) |       |
|    12 | Desert Shower                | [link](https://everybody.codes/event/2024/quests/12) | [link](events/2024/12) |       |
|    13 | Never Gonna Let You Down     | [link](https://everybody.codes/event/2024/quests/13) | [link](events/2024/13) |       |
|    14 | The House of Palms           | [link](https://everybody.codes/event/2024/quests/14) | [link](events/2024/14) |       |
|    15 | From the Herbalist's Diary   | [link](https://everybody.codes/event/2024/quests/15) | [link](events/2024/15) |       |
|    16 | Cat Grin of Fortune          | [link](https://everybody.codes/event/2024/quests/16) | [link](events/2024/16) |       |
|    17 | Galactic Geometry            | [link](https://everybody.codes/event/2024/quests/17) | [link](events/2024/17) |       |
|    18 | The Ring                     | [link](https://everybody.codes/event/2024/quests/18) | [link](events/2024/18) |       |
|    19 | Encrypted Duck               | [link](https://everybody.codes/event/2024/quests/19) | [link](events/2024/19) |       |
|    20 | Gliding Finale               | [link](https://everybody.codes/event/2024/quests/20) | [link](events/2024/20) |       |

### 2025 - The Song of Ducks and Dragons

Future event.

## Stories

### 1 - Echoes of Enigmatus

| Quest | Name                    | Problem                                          | Solution               | Ducks |
|------:|:------------------------|:-------------------------------------------------|:-----------------------|:------|
|     1 | EniCode                 | [link](https://everybody.codes/story/1/quests/1) | [link](stories/1/1) |       |
|     2 | Tangled Trees           | [link](https://everybody.codes/story/1/quests/2) | [link](stories/1/2) |       |
|     3 | The Conical Snail Clock | [link](https://everybody.codes/story/1/quests/3) | [link](stories/1/3) |       |

### 2 - The Entertainment Hub

Future story.

## Technologies

### Python

To run the Python scripts, you need to perform the following steps:

1. Install [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/).

2. Start a virtual environment.
   ```shell
   python -m venv venv
   ```

3. Activate the virtual environment.
   ```shell
   source venv/bin/activate
   ```

4. Install the dependencies.
   ```shell
   pip install -e .
   ```

5. Run the solution for the required day.
   ```shell
   year=2015
   day=1
   set="puzzle"
   python "./$year/$day/solution.py" < "./problems/$year/$day/inputs/$set.txt"
   ```
