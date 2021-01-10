from time import sleep
import pygame
import socket

class Game_handler:
    def __init__ (self,title,sentence):
        self.dim = (550,550)
        self.title = title
        self.sentence = sentence
        self.sentence_splited = sentence.split(" ")
        self.current_index = 0
        self.current_written_word = ""
        self.run_status = True
        self.canvas = pygame.display.set_mode(self.dim)
        self.typed_font = pygame.font.init()
        self.sentence_font = pygame.font.init()
        self.timer_font = pygame.font.init()
        self.timer = 6000
        self.background_color = (0,0,0)
        self.wrong_indicator = False
        
    def key_event_handler(self,ascii_value):
        
        
        if ascii_value > 96 and ascii_value < 123:

            self.current_written_word += chr(ascii_value)

        elif ascii_value == 135:
            self.current_written_word = self.current_written_word[:-1]

        elif ascii_value == 137:
            if self.sentence_splited[self.current_index] == self.current_written_word:#true advance in word(return index of next word)
                self.current_index += 1
                self.current_written_word = ""
                return True
            else:
                self.wrong_indicator = True

    def finish_sesion(self):
        self.run_status = False
        
    def events_handler(self,pygame_event):
        try:
            if pygame_event.type == pygame.QUIT or self.current_index == len(self.sentence_splited) or self.timer == 0:
                self.finish_sesion()
            elif pygame_event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                self.key_event_handler(key.index(1)+93)
        except ValueError:
            pass

    
        

    def display_progress_bar(self):
        bar_color = (255,255,255)
        
        pygame.draw.rect(self.canvas,bar_color,(25,50,((self.current_index/len(self.sentence_splited))*100)*5,30))
        pygame.display.update()

    def display_full_sentence(self):
        font_size = 20
        color = (255,255,255)
        coords = (25,100)
        self.sentence_font = pygame.font.Font('freesansbold.ttf',font_size)
        pygame.draw.rect(self.canvas,self.background_color,(coords[0],coords[1], 550,50))
        composite_sentence = [self.sentence[x:x+51] for x in range(0, len(self.sentence),51)]
        for i in range(0,len(composite_sentence)): 
            text_to_display = self.sentence_font.render(composite_sentence[i],True,color)
            
            
            self.canvas.blit(text_to_display,(25,100 + (30*i)))
        
        pygame.display.update()
        
    def display_wrong_indicator(self):
        fixed_written_coord = (25,450)
        self.display_text((255,0,0),fixed_written_coord,self.current_written_word)   

    def display_current_written_word(self):
        fixed_written_coord = (25,450)
        self.display_text((255,255,255),fixed_written_coord,self.current_written_word)

    def display_text(self,color,coords,string):
        font_size = 18
        self.tpyed_font = pygame.font.Font('freesansbold.ttf',font_size)
        text_to_display = self.sentence_font.render(self.current_written_word,True,color)
        pygame.draw.rect(self.canvas,self.background_color,(coords[0],coords[1],550,50))
        self.canvas.blit(text_to_display,coords)
        pygame.display.update()

    def display_timer(self):
        font_size = 15
        color = (255,255,255)
        coords = (25,200)
        self.timer_font = pygame.font.Font('freesansbold.ttf',font_size)
        text_to_display = self.timer_font.render(str(self.timer),True,color)
        pygame.draw.rect(self.canvas,self.background_color,(coords[0],coords[1],550,50))
        self.canvas.blit(text_to_display,coords)
        pygame.display.update()

    def display_handler(self):
        self.display_full_sentence()
        
        self.display_progress_bar()
        if not self.wrong_indicator:
            self.display_current_written_word()
        else:
            self.display_wrong_indicator()
            sleep(0.15)
            self.wrong_indicator = False
          
    

    def main_loop(self):
        pygame.display.set_caption(self.title)
        pygame.init()
        
        while self.run_status:
            
            self.display_timer()
            pygame.time.delay(20)
            for event in pygame.event.get():
                    self.events_handler(event)
                    self.display_handler()
            self.timer -= 1
                    
        print (self.timer)
        pygame.quit()
