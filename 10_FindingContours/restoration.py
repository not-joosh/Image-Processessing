import numpy as np
def get_mask(image):
    '''Create mask with three defect regions'''
    mask = np.zeros(image.shape[:-1])

    mask[101:106, 0:240] = 1
    
    mask[152:154, 0:60] = 1
    mask[153:155, 60:100] = 1
    mask[154:156, 100:120] = 1
    mask[155:156, 120:140] = 1

    mask[212:217, 0:150] = 1
    mask[217:222, 158:256] = 1
    
    return mask