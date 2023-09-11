import pygame
import player, goal, rock, wall
from data import WINDOW_HEIGHT, WINDOW_WIDTH, GAME_FPS, LINE_Y, BLACK, WHITE
import math
from time import sleep

pygame.init()
pygame.font.init()

game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rock throw game")
game_clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)


main_player = player.Player(game_window)
main_rock = rock.Rock(game_window)
main_wall = wall.Wall(game_window)


def gameReset() -> None:
    main_player.reset()
    main_rock.reset()
    gameLoop()

def gameOver() -> None:
    
    game_over = True
    while game_over:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                gameReset()
                gameLoop()
                game_over = False

# def endText() -> None:
#     go_text = font.render("Bulls EYE!. Press R to Respawn", True, BLACK)        
#     game_window.blit(go_text, (10, 100))

def gameLoop() -> None:
    
    main_goal = goal.Goal(game_window)
    game_run : bool = True
    drawing : bool = False
    start_pos : (int, int) = None
    drawing : bool = False
    canThrow : bool = True
    start_time = pygame.time.get_ticks()
    waiting : bool = True

    font = pygame.font.Font(None, 24)
    
    power : int = 0
    angle_degrees : int = 0

    game_start : bool = False


    while game_run:

        game_clock.tick(GAME_FPS)
        game_window.fill(WHITE)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                quit()
            if canThrow:
                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False
                    game_start = True
                    start_pos = None
                    if main_rock.isThrowing:
                        main_player.throwRock(main_rock, power, angle_degrees)
                        main_rock.isThrowing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    drawing = True
                    start_pos = pygame.mouse.get_pos()
                    if not main_rock.isThrowing:
                        main_rock.isThrowing = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and game_start:
                        gameReset()


        surface = pygame.draw.line(game_window, BLACK, (0, LINE_Y), (WINDOW_WIDTH, LINE_Y), 2)
        main_player.show()
        main_goal.show()
        main_rock.show()
        main_wall.show()
        if game_start:
            main_rock.update(main_wall)
            main_player.setDistance(main_rock.bounces)
            if main_rock.collideGoal(main_goal):
                
                gameOver()
                main_player.score = main_rock.bounces
                game_start = False  

            if main_player.throwCount == 5 and waiting:
                current_time = pygame.time.get_ticks()
                canThrow = False 
                if current_time - start_time >= 5000:
                    waiting = False   
                    gameOver()
                    main_player.score = main_rock.bounces
                    game_start = False
                

        distance_text = font.render(f"Bounces: {main_player.score}", True, BLACK)
        player_shots = font.render(f"Shots available: {5 - main_player.throwCount} / 5", True, BLACK)
        game_window.blit(distance_text, (10, 70))
        game_window.blit(player_shots, (10, 100))

        if drawing and start_pos is not None:
            curr_mouse_position = pygame.mouse.get_pos()
            distance = math.sqrt((curr_mouse_position[0] - start_pos[0]) ** 2 + (curr_mouse_position[1] - start_pos[1]) ** 2)

            # Limit the line length to 300 pixels
            if distance <= 500:
                pygame.draw.line(game_window, BLACK, start_pos, curr_mouse_position, 3)
            else:
                # Calculate the end position to maintain a length of 300 pixels
                angle = math.atan2(curr_mouse_position[1] - start_pos[1], curr_mouse_position[0] - start_pos[0])
                end_x = start_pos[0] + 500 * math.cos(angle)
                end_y = start_pos[1] + 500 * math.sin(angle)
                pygame.draw.line(game_window, BLACK, start_pos, (end_x, end_y), 3)
                distance = 500

            # Calculate the angle and power of the shot and show it on screen

            power = ((distance / 500) * 100) / 5

            angle_degrees = math.degrees(math.atan2(curr_mouse_position[1] - start_pos[1], curr_mouse_position[0] - start_pos[0]))
            angle_degrees = (angle_degrees + 360) % 360

            shot_text = font.render(f"Shot Power: {power*5:.2f}%", True, BLACK)
            angle_text = font.render(f"Radius: {angle_degrees:.2f} dg", True, BLACK)
            
            
            
            game_window.blit(shot_text, (10, 10))
            game_window.blit(angle_text, (10, 40))
            

        

        pygame.display.update()
        # pygame.time.delay(80)


if __name__ == "__main__":
    gameLoop()