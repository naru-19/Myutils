def get_digit(x):
    block=np.zeros((5,3,1))
    if x==1:
        block[:,2]=1
    elif x==2:
        block[[0,2,4],:]=1
        block[0:3,2]=1
        block[2:,0]=1
    elif x==3:
        block[[0,2,4],:]=1
        block[:,2]=1
    elif x==4:
        block[:3,0]=1
        block[2,:]=1
        block[:,2]=1
    elif x==5:
        block[[0,2,4],:]=1
        block[0:3,0]=1
        block[2:,2]=1
    elif x==6:
        block[[4,2],:]=1
        block[0:4,0]=1
        block[2:,2]=1
    elif x==7:
        block[0,:]=1
        block[:,2]=1
    elif x==8:
        block[:,:]=1
        block[1,1]=0
        block[3,1]=0
    elif x==9:
        block[[0,2],:]=1
        block[:3,0]=1
        block[:,2]=1
    elif x==0:
        block[[0,4],:]=1
        block[:,[0,2]]=1
    
    return block
        
def num2img(
    n:'input number',
    fix_digit:'Fix the number of digits displayed?'=False,
    nod_fix:'number of digit'=2):
    if n==0:
        margin=0
    else:
        margin=int(np.log10(n))
    nod=margin+1
    if fix_digit:
        margin=nod_fix-1
        nod=nod_fix
    margin+=2
    
    digit=np.zeros((7,margin+nod*3,1))
    l=1
    while nod>0:
        tmp=n//10**(nod-1)
        nod-=1
        digit[1:6,l:l+3]=get_digit(tmp)
        n=n-10**(nod)*tmp
        l+=4
    return digit
