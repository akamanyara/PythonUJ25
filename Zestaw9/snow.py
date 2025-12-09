import pygame
import random
import sys

# --- SETTINGS ---
WIDTH = 600
HEIGHT = 800
FPS = 40
SNOW_SPAWN_RATE = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Snow")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 36)

# --- SNOWFLAKE CLASS ---
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = -10
        self.radius = random.randint(5, 10)
        self.speed = random.uniform(1, 3)

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

    def is_clicked(self, pos):
        return (self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2 <= self.radius ** 2

# --- MAIN GAME LOOP ---
def main():
    snowflakes = []
    running = True
    game_over = False

    while running:
        clock.tick(FPS)

        # --- EVENT HANDLING ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_over:
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Remove clicked snowflake
                snowflakes = [s for s in snowflakes if not s.is_clicked((mx, my))]

        if not game_over:
            # Spawn new snowflakes
            if random.randint(1, SNOW_SPAWN_RATE) == 1:
                snowflakes.append(Snowflake())

            # Update snowflakes
            for s in snowflakes:
                s.update()
                if s.y - s.radius > HEIGHT:
                    game_over = True  # Snowflake touched ground

        # --- DRAW ---
        screen.fill((0, 0, 20))

        for s in snowflakes:
            s.draw(screen)

        if game_over:
            text = FONT.render("GAME OVER!", True, (255, 50, 50))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()

# --- RUN ---
if __name__ == "__main__":
    main()
