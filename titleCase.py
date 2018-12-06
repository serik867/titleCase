def title_case(str, expt):
    strlst = str.lower().split()
    finalstr = " "
    
    expt = [i.lower() for i in expt] 
    
    for i in strlst:
        if i == strlst[0] or i not in expt:
            finalstr += i.title() + " "
        else:
            finalstr = finalstr + i + " "


    
    print(finalstr)


text = "Let the beauty of what you love be what you do"
excep = ["the", "Of", "YOU", "be", 'do']
title_case(text, excep)