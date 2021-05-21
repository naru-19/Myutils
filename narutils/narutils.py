def decopri(txt):
    print("-"*80)
    if len(str(txt))<80:
        print(" "*int((80-len(str(txt)))/2)+str(txt)+" "*int((80-len(str(txt)))/2))
    else:
        print(str(txt))
    print("-" * 80)

def decopri_title(title,txt):
    # print("-"*80)
    # if len(title)<80:
    #     print(" "*int((80-len(title))/2)+str(title)+" "*int((80-len(title))/2))
    # else:
    #     print(str(title))
    txt=title+" :"+str(txt)
    if len(str(txt))<80:
        print(" "*int((80-len(str(txt)))/2)+str(txt)+" "*int((80-len(str(txt)))/2))
    else:
        print(str(txt))
    print("-" * 80)
