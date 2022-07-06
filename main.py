import os
import sys
import random
from arguments import getArguments

args = getArguments()

if os.path.exists(args.source) == False:
    os.mkdir(args.source)

source = args.source
train = args.train
test = args.test

original_stdout = sys.stdout
with open(source, "r") as f:
    lines = f.readlines()

    idx = list(range(0, len(lines)))
    sel = random.sample(idx, int(0.8 * len(lines)))
    idx = list(set(idx) - set(sel))

    with open(train, "w") as t:
        sys.stdout = t
        for i in sel:
            print(lines[i][:len(lines[i])-1])

    with open(test, "w") as t:
        sys.stdout = t
        for i in idx:
            print(lines[i][:len(lines[i])-1])

sys.stdout = original_stdout
