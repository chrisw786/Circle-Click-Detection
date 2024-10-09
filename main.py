# Imports
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up display for full screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Circle Click Detection")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Circle and square properties
circle_radius = 50
circle_center = (width // 2, height // 2)
square_side = circle_radius * 2
square_top_left = (circle_center[0] - circle_radius, circle_center[1] - circle_radius)

# Font for displaying text
font = pygame.font.SysFont(None, 24)
label_text = "Click anywhere to check distance from the circle."

# Function to check if click is inside the circle using Pythagorean theorem
def is_click_inside_circle(mouse_pos, center, radius):
    dist_x = mouse_pos[0] - center[0]
    dist_y = mouse_pos[1] - center[1]
    distance = math.sqrt(dist_x**2 + dist_y**2)
    return distance <= radius, distance

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw square
    pygame.draw.rect(screen, BLUE, (*square_top_left, square_side, square_side), 2)

    # Draw circle inside the square
    pygame.draw.circle(screen, BLACK, circle_center, circle_radius, 2)

    # Display the label in the top-right corner
    label = font.render(label_text, True, BLACK)
    screen.blit(label, (width - label.get_width() - 10, 10))

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        # Check mouse click and calculate distance from circle
        if event.type == pygame.MOUSEBUTTONDOWN:
            inside, distance = is_click_inside_circle(event.pos, circle_center, circle_radius)
            
            if inside:
                label_text = "You clicked inside the circle!"
            else:
                miss_distance = distance - circle_radius
                label_text = f"Missed by {miss_distance:.2f} pixels."

    pygame.display.flip()
