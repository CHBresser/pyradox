import _initpath
import os
import re
import collections
import pyradox.config
import pyradox.txt
import pyradox.primitive
import pyradox.image
import pyradox.struct

start_date = pyradox.primitive.Date('1444.11.11')

counts = pyradox.struct.Tree() # province counts

# parse all files in a directory, producing instances of pyradox.struct.Tree
for filename, data in pyradox.txt.parse_dir(os.path.join(pyradox.config.basedirs['EU4'], 'history', 'provinces')):
    # pyradox.struct.Tree has many dict methods, such as .keys()
    if 'base_tax' not in data.keys(): continue
    
    trade_good = 'unknown'
    for curr_good in data.find_walk('trade_goods'):
        if curr_good != 'unknown':
            trade_good = curr_good
        
    if trade_good not in counts: counts[trade_good] = 1
    else: counts[trade_good] += 1
        
print([(key, counts[key]) for key in counts.keys()])
