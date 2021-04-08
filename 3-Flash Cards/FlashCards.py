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


# def flash(flashcard):
#     print (flashcard[0],flashcard[1],flashcard[2])
   
#     if (flashcard[1] == '+'):
#         print (flashcard[0] + flashcard[2])
    
#     elif (flashcard[1] == '-'):
#         print (flashcard[0] - flashcard[2])
    
#     elif (flashcard[1] == 'x'):
#         print (flashcard[0] * flashcard[2])

#     elif (flashcard[1] == '/'):
#         if(flashcard[2] == 0):
#             print ("None")
#         else:
#             print (round(flashcard[0] / flashcard[2],2))

# flash([3, 'x', 7])