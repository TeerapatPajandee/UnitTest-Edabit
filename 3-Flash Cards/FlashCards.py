def flash(flashcard):
       
    if (flashcard[1] == '+'):
        return (flashcard[0] + flashcard[2])
    
    elif (flashcard[1] == '-'):
        return (flashcard[0] - flashcard[2])
    
    elif (flashcard[1] == 'x'):
        return (flashcard[0] * flashcard[2])

    elif (flashcard[1] == '/'):
        if(flashcard[2] == 0):
            return None
        else:
            return (round(flashcard[0] / flashcard[2],2))
            
    print (flashcard[0],flashcard[1],flashcard[2])