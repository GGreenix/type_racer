import pygame



class game_handler:
    def __init__ (self,title,sentence):
        self.dim = (550,550)
        self.title = title
        self.sentence = sentence.split(" ")
        self.current_index = 0
        self.current_written_word = ""
        self.run_status = True
        self.canvas = pygame.display.set_mode(self.dim)
    
    def main_loop(self):
        pygame.display.set_caption(self.title)
        pygame.init()

        while run:
        for event in pygame.event.get():
            display_handler(canvas,current_index,sentence)
            run = events_handler(event)
            
        pygame.quit()
    def key_event_handler(ascii_value):
        global sentence
        global current_index
        global text_word 
        
        if ascii_value > 96 and ascii_value < 123:
            #global current_word
            text_word += chr(ascii_value)
            return chr(ascii_value)
        
        elif ascii_value == 137:
        # end_word = lambda string_to_check,string_to_equalize: True if string_to_check == string_to_equalize else False
            #needs to add continuing in sentence
            if sentence[current_index] == text_word:#true advance in word(return index of next word)
                current_index += 1
                text_word = ""
                print("PASSED!!")
                return True
            else:
                print("wrong word buddy")

    def events_handler(self):
        
        if pygame_event.type == pygame.QUIT or current_index == len(sentence):
            return False
        elif pygame_event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        elif pygame_event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            print(key_event_handler(key.index(1)+93),sentence,current_index,text_word)
        else:
            return True

def display_handler(canvas,current_index,sentence):
    bar_color = (255,255,255)

    if not len(sentence) == current_index:
        pygame.draw.rect(canvas,bar_color,(25,275,(current_index/len(sentence[current_index]))*100,50))
    pygame.display.update()


def main():   
    title = "type racer"
    sentence = "hello its me"
    
    g_h = game_handler(title,sentence)

    

if __name__ == "__main__":
    main()