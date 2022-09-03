from rapydmain import rapydmain
from pathlib import Path

with rapydmain(Path(__file__).parent) as main:
    print('test1')
    raise Exception('test2')
