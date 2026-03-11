def my_add(x):
    '''
    a test
    '''
    import numpy as np
    return np.sum(x)

def my_save(x):
    '''
    another test
    '''
    from pathlib import Path
    import sys
    root = Path.cwd().parent
    sys.path.append(str(root / 'src'))
    import util
    import numpy as np
    y = my_add(x)
    np.savetxt(f'{root}/outputs/{x}.txt', np.array([y]))
    return f'{root}/outputs/{x}.txt'