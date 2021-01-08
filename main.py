import Game_handler

def main():   
    
    title = "type racer"
    sentence = "hello its me"
    
    g_h = game_handler(title,sentence)

    g_h.main_loop()
    

if __name__ == "__main__":
    main()