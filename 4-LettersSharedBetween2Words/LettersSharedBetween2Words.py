def shared_letters(word1,word2):
    count=0
    if len(word1) < len(word2):
        for i in word1:
            if i in word2:
                count += 1
    else:
        for i in word2:
            if i in word1:
                count += 1
    return(count)