import sys 
from narutils import *

if __name__=='__main__':
    print(dir(narutils))
    decopri('Counting until three seconds have passed.')
    start = now()
    while now(start)<3:
        ovwrite(now(start))
    args_list=[
        ['--batch_size',int,16,'num of batch size'],
        ['--num_epoch',int,300,'num of epoch']
    ]
    flags = ParseSimple(args_list).flags
    print(flags.batch_size)