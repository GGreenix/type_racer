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
        self.sentence_font = pygame.font.init()
        self.sentence_font = pygame.font.Font('freesansbold.ttf',32)
        

    def key_event_handler(self,ascii_value):
        
        
        if ascii_value > 96 and ascii_value < 123:
            #global current_word
            self.current_written_word += chr(ascii_value)
            
            return chr(ascii_value)
        elif ascii_value == 135:
            self.current_written_word = self.current_written_word[:-1]
        elif ascii_value == 137:
        
            if self.sentence[self.current_index] == self.current_written_word:#true advance in word(return index of next word)
                self.current_index += 1
                self.current_written_word = ""
                print("PASSED!!")
                return True
            else:
                print("wrong word buddy")

    def finish_sesion(self):
        self.run_status = False
        
    def events_handler(self,pygame_event):
        
        if pygame_event.type == pygame.QUIT or self.current_index == len(self.sentence):
            self.finish_sesion()
        elif pygame_event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            print(self.key_event_handler(key.index(1)+93))
        
    def display_handler(self):
        bar_color = (255,255,255)
        pygame.draw.rect(self.canvas,bar_color,(25,275,(self.current_index/len(self.sentence[self.current_index]))*100,50))
        
        pygame.display.update()  
    

    def main_loop(self):
        pygame.display.set_caption(self.title)
        pygame.init()

        while self.run_status:
            pygame.time.delay(50)
            for event in pygame.event.get():
                    self.display_handler()
                    self.events_handler(event)
            
        pygame.quit()