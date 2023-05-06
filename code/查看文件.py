import os
from pathlib import Path
totalSize = 0
for filename in os.listdir('D:\\PYCODE'):
    totalSize = totalSize + os.path.getsize(os.path.join('D:\\PYCODE', filename))
print(totalSize)
