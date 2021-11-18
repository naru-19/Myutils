import sys
import time 
import numpy as np 
import pandas as pd 
import time 
from tqdm import tqdm 
import math
import argparse
def ovwrite(text):
    sys.stdout.write('\r'+str(text))
    sys.stdout.flush()
    time.sleep(0.01)
def log_string(log_dir,txt):
    log = open(log_dir,'w')
    log.write(str(txt)+'\n')
    log.flush()
    log.close
    print(str(txt))
def loadasdf(fpath):
    if not os.path.exists(fpath):
        print('no such file')
        sys.exit()
    if fpath[-3:]=="npy":
        return pd.DataFrame(np.load(fp))
    elif fpath[-3:]=="txt":
        return pd.read_csv(fp,sep="\s+",header=None)
    else:
        print("Unknown format")

def decopri(txt,op_len=80,op_mark='-'):
    txt = str(txt)
    print(f'{op_mark*op_len}')
    lt = len(txt)
    if lt<op_len:
        sp_len=int((op_len-lt)/2)
        print(f'{" "*sp_len}{txt}{" "*sp_len}')
    else:
        print(txt)
    print(f'{op_mark*op_len}')

def now(s=None):
    if not s:
        return time.time()
    else:
        return time.time()-s
def dfc(s=None):
    return pd.DataFrame(s)

def vc(s):
    _vc = s.value_counts()
    return _vc
def sin(theta):
    return math.sin(theta)
def cos(theta):
    return math.cos(theta) 

class ParseSimple():
    def __init__(self,args_list):
        self.parser = argparse.ArgumentParser()
        for arg in args_list:
            self.add_arg(arg)
        self.flags=self.parser.parse_args()
    def add_arg(self,argument):
        self.parser.add_argument(str(argument[0]),type=argument[1],default=argument[2],help=argument[3])



if __name__=='__main__':
    s = now()
    while now(s)<=1:
        ovwrite(f'{now(s):.3f}')
    print('\n')
    decopri(now(s),90,'+')
    # ar = np.array([[1,2,3],[4,5,6]])
    # df = dfc(ar)
    # print(df)
    # print(vc(df[0]))
    df = dfc()
    df[0]=[1,2,3,]
    print(df)

