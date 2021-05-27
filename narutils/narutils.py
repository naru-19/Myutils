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

    
    
def decost(txt):
    print("☆"*80)
    if len(str(txt))<80:
        print(" "*int((80-len(str(txt)))/2)+str(txt)+" "*int((80-len(str(txt)))/2))
    else:
        print(str(txt))
    print("☆" * 80)
    
def decopri_title_st(title,txt):
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
    print("☆" * 80)
    

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os
import sys
def savegraph(x,y,title=None,xlabel=None,ylabel=None,filepath="./",overwrite=False):
    title=str(title)
    fname=os.path.join(filepath,title+".png")
    fig = plt.figure()
    ax = fig.add_subplot(111, xlabel=xlabel, ylabel=ylabel)
    fig.suptitle(title)
    ax.plot(x, y,c="b")
    if os.path.isfile(fname):
        if overwrite:
            print("caution:There was a file with the same name and you overwrote it.")
            fig.savefig(fname)
        else :
            print("Error:There is a same name file, please change file name.")
            sys.exit()
    else :
        fig.savefig(fname)
        
import random
def randcol(n,norm=False):
    if n>20:
        print("caution:You should reduce the number of colors a little bit.")
    li=list(range(0,256,5))
    col=[]
    for i in range(3):
        if norm:
            col.append([float(random.randint(0,len(li))*5)/255 for j in range(n)])            
        else :
            col.append([random.randint(0,len(li))*5 for j in range(n)])
    col=np.array(col)
    return col.reshape(col.shape[1],3)
