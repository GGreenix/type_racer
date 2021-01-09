import Game_handler as gh

def main():   
    
    title = "type racer"
    sentence = "hey my name is tal"
    
    g_h = gh.Game_handler(title,sentence)

    g_h.main_loop()
    

if __name__ == "__main__":
    main()