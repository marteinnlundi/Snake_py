import pygame
import random
import json
import os

pygame.init()

WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Arial", 24)

# Game variables
clock = pygame.time.Clock()
snake_speed = 10
score = 0
snake_color = GREEN
food_color = RED
leaderboard_file = "leaderboard.json"


# Function to draw text on screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))


# Load leaderboard from file
def load_leaderboard():
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            return json.load(file)
    return []


# Save leaderboard to file
def save_leaderboard(leaderboard):
    with open(leaderboard_file, "w") as file:
        json.dump(leaderboard, file)


# Function to get player name input
def get_player_name():
    player_name = ""
    input_active = True

    while input_active:
        screen.fill(BLACK)
        draw_text("Enter your name:", font, WHITE, screen, WIDTH // 2 - 100, HEIGHT // 2 - 50)
        draw_text(player_name, font, WHITE, screen, WIDTH // 2 - 50, HEIGHT // 2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_name:
                        input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

    return player_name


# Main menu
def main_menu():
    global snake_color, food_color

    menu_running = True
    while menu_running:
        screen.fill(BLACK)
        draw_text("Snake Game", font, WHITE, screen, WIDTH // 2 - 70, HEIGHT // 2 - 120)
        play_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 - 40, 140, 30)
        leaderboard_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2, 140, 30)
        customize_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 40, 140, 30)
        quit_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 80, 140, 30)

        pygame.draw.rect(screen, GREEN, play_button)
        pygame.draw.rect(screen, BLUE, leaderboard_button)
        pygame.draw.rect(screen, YELLOW, customize_button)
        pygame.draw.rect(screen, RED, quit_button)

        draw_text("Play Game", font, BLACK, screen, play_button.x + 20, play_button.y + 5)
        draw_text("Leaderboard", font, BLACK, screen, leaderboard_button.x + 15, leaderboard_button.y + 5)
        draw_text("Customize Colors", font, BLACK, screen, customize_button.x + 5, customize_button.y + 5)
        draw_text("Quit", font, BLACK, screen, quit_button.x + 50, quit_button.y + 5)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    player_name = get_player_name()
                    game(player_name)
                elif leaderboard_button.collidepoint(event.pos):
                    show_leaderboard()
                elif customize_button.collidepoint(event.pos):
                    customize_colors()
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()


# Leaderboard screen
def show_leaderboard():
    leaderboard = load_leaderboard()
    screen.fill(BLACK)
    draw_text("Leaderboard", font, WHITE, screen, WIDTH // 2 - 70, 50)

    y_offset = 100
    for entry in leaderboard[:5]:
        draw_text(f"{entry['name']}: {entry['score']}", font, WHITE, screen, WIDTH // 2 - 70, y_offset)
        y_offset += 30

    draw_text("Press any key to return", font, WHITE, screen, WIDTH // 2 - 90, HEIGHT - 50)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()


# Customize colors screen
def customize_colors():
    global snake_color, food_color

    color_options = [GREEN, YELLOW, BLUE, CYAN, MAGENTA]
    color_names = ["Green", "Yellow", "Blue", "Cyan", "Magenta"]
    color_index = 0

    customizing = True
    while customizing:
        screen.fill(BLACK)
        draw_text("Customize Colors", font, WHITE, screen, WIDTH // 2 - 90, 50)
        draw_text(f"Snake Color: {color_names[color_index]}", font, WHITE, screen, WIDTH // 2 - 70, HEIGHT // 2 - 20)
        draw_text("Press Enter to confirm or Space to change color", font, WHITE, screen, WIDTH // 2 - 150, HEIGHT // 2 + 30)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    snake_color = color_options[color_index]
                    food_color = color_options[(color_index + 2) % len(color_options)]
                    customizing = False
                elif event.key == pygame.K_SPACE:
                    color_index = (color_index + 1) % len(color_options)


# Game function
def game(player_name):
    global score, snake_speed

    snake_pos = [(100, 100), (80, 100), (60, 100)]
    snake_direction = "RIGHT"
    food_pos = (random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE)
    score = 0
    snake_speed = 10
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"

        # Update snake position
        head_x, head_y = snake_pos[0]
        if snake_direction == "UP":
            head_y -= CELL_SIZE
        elif snake_direction == "DOWN":
            head_y += CELL_SIZE
        elif snake_direction == "LEFT":
            head_x -= CELL_SIZE
        elif snake_direction == "RIGHT":
            head_x += CELL_SIZE

        # Wrap the snake around if it goes off the screen
        head_x %= WIDTH
        head_y %= HEIGHT

        snake_pos.insert(0, (head_x, head_y))

        if snake_pos[0] == food_pos:
            score += 1
            food_pos = (random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                        random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE)
            if score % 5 == 0:
                snake_speed += 2
        else:
            snake_pos.pop()

        # Check for collision with itself
        if len(snake_pos) != len(set(snake_pos)):
            leaderboard = load_leaderboard()
            leaderboard.append({"name": player_name, "score": score})
            leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
            save_leaderboard(leaderboard)
            running = False

        screen.fill(BLACK)
        for pos in snake_pos:
            pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

        pygame.display.flip()
        clock.tick(snake_speed)


main_menu()