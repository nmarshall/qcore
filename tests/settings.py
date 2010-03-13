import sys
import os
root = os.path.split(__file__)[0]
#print root
for i in range(1):
    root = os.path.split(root)[0]
    print root

qcore_ = os.path.join(root,'Debug')
print qcore_

sys.path.append(qcore_)
