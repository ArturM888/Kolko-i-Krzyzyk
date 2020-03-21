import Board
import pygame

# rozpocznij program
pygame.init()


# stworz ekran gry
screen = pygame.display.set_mode((550, 550))
screen.fill((65 ,105 ,225))
# nazwa gry
pygame.display.set_caption("Kółko i krzyżyk")

#ikonka
icon = pygame.image.load("assets/kik.png")
pygame.display.set_icon(icon)

# graffiki znaczków X i O
textureX = pygame.image.load("assets/X.png")
textureO = pygame.image.load("assets/O.png")

text = "Witam w grze kółko i krzyżyk. Wybierz gracza, który rozpocznie rozgrywkę "
text11 = "klikając w wybrany obrazek"
text1 = "Krzyżyk"
text2 = "Kółko"
czcionka = pygame.font.SysFont("dejavusans", 20)
czcionka2 = pygame.font.SysFont("dejavusans", 30)
text_render = czcionka.render(text, 1, (250, 250, 250))
text_render11 = czcionka.render(text11, 1, (250, 250, 250))
text_render1 = czcionka.render(text1, 10, (250, 250, 250))
text_render2 = czcionka.render(text2, 10, (250, 250, 250))
screen.blit(text_render11, (10, 30))
screen.blit(text_render, (10, 10))
screen.blit(text_render1, (85, 180))
screen.blit(text_render2, (310, 180))

first_choice = pygame.draw.rect(screen, (255, 255, 255), (75, 200, 150, 150))
second_choice = pygame.draw.rect(screen, (255, 255, 255), (300, 200, 150, 150))



screen.blit(textureX, (75, 200))

screen.blit(textureO, (300, 200))
pygame.display.flip()







runningFirstWindow = True

running = True




while running:

    pygame.time.delay(100)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if runningFirstWindow:
                if first_choice.collidepoint(pos):
                    player = "X"
                    board = Board.Board(player)
                    runningFirstWindow = False
                    screen.fill((65, 105, 225))
                    first = pygame.draw.rect(screen, (255, 255, 255), (25, 25, 150, 150))
                    second = pygame.draw.rect(screen, (255, 255, 255), (200, 25, 150, 150))
                    third = pygame.draw.rect(screen, (255, 255, 255), (375, 25, 150, 150))

                    fourth = pygame.draw.rect(screen, (255, 255, 255), (25, 200, 150, 150))
                    fifth = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 150, 150))
                    sixth = pygame.draw.rect(screen, (255, 255, 255), (375, 200, 150, 150))

                    seventh = pygame.draw.rect(screen, (255, 255, 255), (25, 375, 150, 150))
                    eighth = pygame.draw.rect(screen, (255, 255, 255), (200, 375, 150, 150))
                    ninth = pygame.draw.rect(screen, (255, 255, 255), (375, 375, 150, 150))

                    first_open = True
                    second_open = True
                    third_open = True
                    fourth_open = True
                    fifth_open = True
                    sixth_open = True
                    seventh_open = True
                    eighth_open = True
                    ninth_open = True
                else:
                    if second_choice.collidepoint(pos):
                        player = "O"
                        board = Board.Board(player)
                        runningFirstWindow = False
                        screen.fill((65, 105, 225))
                        first = pygame.draw.rect(screen, (255, 255, 255), (25, 25, 150, 150))
                        second = pygame.draw.rect(screen, (255, 255, 255), (200, 25, 150, 150))
                        third = pygame.draw.rect(screen, (255, 255, 255), (375, 25, 150, 150))

                        fourth = pygame.draw.rect(screen, (255, 255, 255), (25, 200, 150, 150))
                        fifth = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 150, 150))
                        sixth = pygame.draw.rect(screen, (255, 255, 255), (375, 200, 150, 150))

                        seventh = pygame.draw.rect(screen, (255, 255, 255), (25, 375, 150, 150))
                        eighth = pygame.draw.rect(screen, (255, 255, 255), (200, 375, 150, 150))
                        ninth = pygame.draw.rect(screen, (255, 255, 255), (375, 375, 150, 150))

                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True

            if first.collidepoint(pos) and first_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (25, 25))
                    pygame.display.flip()
                    board.putToBoard(0, 0)


                else:
                    screen.blit(textureO, (25, 25))
                    pygame.display.flip()
                    board.putToBoard(0, 0)
                first_open = False

            if second.collidepoint(pos) and second_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (200, 25))
                    pygame.display.flip()
                    board.putToBoard(0, 1)
                else:
                    screen.blit(textureO, (200, 25))
                    pygame.display.flip()
                    board.putToBoard(0, 1)
                second_open = False

            if third.collidepoint(pos) and third_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (375, 25))
                    pygame.display.flip()
                    board.putToBoard(0, 2)
                else:
                    screen.blit(textureO, (375, 25))
                    pygame.display.flip()
                    board.putToBoard(0, 2)
                third_open = False

            if fourth.collidepoint(pos) and fourth_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (25, 200))
                    pygame.display.flip()
                    board.putToBoard(1, 0)
                else:
                    screen.blit(textureO, (25, 200))
                    pygame.display.flip()
                    board.putToBoard(1, 0)
                fourth_open = False

            if fifth.collidepoint(pos) and fifth_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (200, 200))
                    pygame.display.flip()
                    board.putToBoard(1, 1)
                else:
                    screen.blit(textureO, (200, 200))
                    pygame.display.flip()
                    board.putToBoard(1, 1)
                fifth_open = False

            if sixth.collidepoint(pos) and sixth_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (375, 200))
                    pygame.display.flip()
                    board.putToBoard(1, 2)
                else:
                    screen.blit(textureO, (375, 200))
                    pygame.display.flip()
                    board.putToBoard(1, 2)
                sixth_open = False

            if seventh.collidepoint(pos) and seventh_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (25, 375))
                    pygame.display.flip()
                    board.putToBoard(2, 0)
                else:
                    screen.blit(textureO, (25, 375))
                    pygame.display.flip()
                    board.putToBoard(2, 0)
                seventh_open = False

            if eighth.collidepoint(pos) and eighth_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (200, 375))
                    pygame.display.flip()
                    board.putToBoard(2, 1)
                else:
                    screen.blit(textureO, (200, 375))
                    pygame.display.flip()
                    board.putToBoard(2, 1)
                eighth_open = False

            if ninth.collidepoint(pos) and ninth_open:
                if board.getPlayer() == "X":
                    screen.blit(textureX, (375, 375))
                    pygame.display.flip()
                    board.putToBoard(2, 2)
                else:
                    screen.blit(textureO, (375, 375))
                    pygame.display.flip()
                    board.putToBoard(2, 2)
                ninth_open = False

 
    pygame.display.update()


pygame.quit()