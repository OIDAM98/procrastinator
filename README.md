# Procrastinator
Procrastinator is an interactive Python-based project that finds different media recommendations based on at most 3 choices given for each media category. It is meant to be used as a way to find new media to consume and procrastinate with, and maybe even add to your favourites!

## Features

Right now it only supports the following media, for both recommendations and user picks:
- Videogames
- TV Shows
- Movies
- Anime
- Bands or Artists

At the end of each session, the recommendation list can be saved to a `txt` file. A prompt will appear that allows the user to select this option. The `recommendations.txt` file is stored at the root folder of the project.

The current limit of `at most 3 choices per category` is due to the limitation of money spent in `ChatGPT` prompts. As more tokens processed, more money spent.

## Requirements
- Python 3.11 or higher
- An OpenAI API Key
- [Poetry](https://python-poetry.org/) _(Optional)_

## Setup
1. Clone the repository:

`git clone `

2. Navigate to project directory:

`cd procrastinator`

3. Installing needed dependencies
   1. If you have `Poetry` installed:
      1. `poetry install`
   2. If not, you can use `pip`:
      1. `pip install -r requirements.txt`
      2. It is recommended that you create a python environment before running this command, with:
      3. `python -m venv procrastinator`, and just run it with `source procrastinator/bin/activate`

4. Create a `.env` at the root of the project directory and add your OpenAI API Key like this:

`OPENAI_API_KEY=${YOUR_API_KEY}`

## Usage

You can run the project two ways:
1. If you have `Poetry` installed:
   1. `poetry run python main.py`
2. Otherwise, using `pip` with `python environment`s, use:
   1. `python main.py`
