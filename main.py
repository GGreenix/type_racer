import pygame




def key_event_handler(ascii_value,current_word="",text_word=""):
    if ascii_value > 96 and ascii_value < 123:
        
        return chr(ascii_value)
    
    elif ascii_value == 137:
        end_word = lambda string_to_check,string_to_equalize: True if string_to_check == string_to_equalize else False
        print (current_word,text_word)
        return end_word(current_word,text_word)


def events_handler(pygame_event):
    if pygame_event.type == pygame.QUIT:
        global run
        run = False
    elif pygame_event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        print(pos)
    elif pygame_event.type == pygame.KEYDOWN:
        global current_word
        global text_word

        key = pygame.key.get_pressed()
        print(key_event_handler(key.index(1)+93,current_word=current_word,text_word=text_word))


def main():
    dim = (550,550)
    title = "type racer"

    global run
    global current_word
    global text_word

    pygame.display.set_caption(title)
    pygame.init()

      
    canvas = pygame.display.set_mode(dim)
    run = True
    current_word = ""
    text_word = ""

    while run:
        for event in pygame.event.get():
            events_handler(event)
            pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()