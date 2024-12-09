import pygame
import math

# Inisialisasi pygame
pygame.init()

# Konfigurasi jendela
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spedometer with Transmission')

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Parameter spedometer
center = (WIDTH // 2, HEIGHT // 2)
radius = 150
speed = 0
max_speed = 200

# Level transmisi
transmission_level = 1
transmission_levels = {
    1: {'increment': 5, 'decrement': 1},
    2: {'increment': 10, 'decrement': 2},
    3: {'increment': 15, 'decrement': 3},
    4: {'increment': 20, 'decrement': 4}
}
max_transmission_level = len(transmission_levels)

# Status tombol
speed_up = False
shift_down = False
ctrl_down = False

# Fungsi untuk menggambar spedometer
def draw_speedometer(speed):
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, center, radius, 5)

    # Menghitung sudut jarum berdasarkan kecepatan
    angle = (speed / max_speed) * 180 - 90
    radian = math.radians(angle)
    end_x = center[0] + radius * 0.8 * math.cos(radian)
    end_y = center[1] + radius * 0.8 * math.sin(radian)

    pygame.draw.line(screen, GREEN, center, (end_x, end_y), 5)

    # Menampilkan kecepatan dan transmisi
    font = pygame.font.Font(None, 36)
    speed_text = font.render(f'Speed: {speed}', True, BLACK)
    speed_rect = speed_text.get_rect(center=(center[0], center[1] + radius + 30))
    screen.blit(speed_text, speed_rect)
    
    transmission_text = font.render(f'Transmission: {transmission_level}', True, BLACK)
    transmission_rect = transmission_text.get_rect(center=(center[0], center[1] + radius + 60))
    screen.blit(transmission_text, transmission_rect)

    pygame.display.flip()

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed_up = True
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift_down = True
            elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                speed_up = False
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift_down = False
            elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl_down = False

    # Update kecepatan
    if speed_up:
        speed = min(speed + transmission_levels[transmission_level]['increment'], max_speed)
    else:
        speed = max(speed - transmission_levels[transmission_level]['decrement'], 0)

    # Update level transmisi
    if shift_down:
        if transmission_level < max_transmission_level:
            transmission_level += 1
        else:
            transmission_level = max_transmission_level  # Tetap di level maksimum

    if ctrl_down:
        if transmission_level > 1:
            transmission_level -= 1
        else:
            transmission_level = 1  # Tetap di level minimum

    draw_speedometer(speed)
    pygame.time.delay(30)  # Delay sedikit untuk kontrol kecepatan frame

pygame.quit()
