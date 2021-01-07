import pygame

def is_a_letter_character(ascii_value):
    if ascii_value > 96 and ascii_value < 123:
        return chr(ascii_value)
def events_handler(pygame_event):
    if pygame_event.type == pygame.QUIT:
        run = False
    elif pygame_event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        print(pos)
    elif pygame_event.type == pygame.KEYDOWN:
        key = pygame.key.get_pressed()
        print(is_a_letter_character(key.index(1)+93))


def main():
    dim = (550,550)
    title = "tic tac toe"
    run = True

    pygame.display.set_caption(title)
    pygame.init()

      
    canvas = pygame.display.set_mode(dim)

    while run:
        for event in pygame.event.get():
            events_handler(event)
            pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()