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
    import src.util as util
    import numpy as np
    y = my_add(x)
    np.savetxt(f'outputs/{x}.txt', np.array([y]))
    return f'outputs/{x}.txt'