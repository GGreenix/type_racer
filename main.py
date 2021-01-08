import Game_handler as gh

def main():   
    
    title = "type racer"
    sentence = "hello its me"
    
    g_h = gh.Game_handler(sentence, title)

    g_h.main_loop()
    

if __name__ == "__main__":
    main()