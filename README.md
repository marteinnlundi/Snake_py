# Snake Game

A classic Snake Game implemented using Python and Pygame, with features like customizable colors, leaderboard tracking, and different game speeds.

## Table of Contents
- [Getting Started](#getting-started)
- [Game Features](#game-features)
- [Controls](#controls)
- [Customizations](#customizations)
- [Leaderboard](#leaderboard)
- [Dependencies](#dependencies)

## Getting Started

To start the game, simply run the `snake.py` file in your terminal or IDE:
```bash
python snake.py
```

## Game Features

- **Snake Gameplay**: Control the snake to eat food and grow longer. Avoid hitting yourself to keep the game going.
- **Main Menu**: Access the game, leaderboard, or customization options through an interactive menu.
- **Leaderboard**: Stores and displays the top scores for players.
- **Color Customization**: Allows customization of snake and food colors for a personalized experience.

## Controls

- **Arrow Keys**: Control the snake's direction.
- **Enter**: Confirm selections in the menu.
- **Space**: Switch color choices in the customization menu.
- **Any Key**: Return from the leaderboard screen to the main menu.

## Customizations

In the main menu, select "Customize Colors" to change the colors of the snake and food. Use the **Space** key to switch colors and **Enter** to confirm.

## Leaderboard

Scores are saved in a `leaderboard.json` file. The leaderboard displays the top five scores and resets only if the file is deleted.

## Dependencies

This game requires **Pygame** to run. You can install it via pip:
```bash
pip install pygame
```

## License
This project is open-source and available for anyone to modify and enhance.