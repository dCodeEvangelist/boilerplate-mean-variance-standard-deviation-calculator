import numpy as np

def calculate(lists):

  if len(lists) == 9:

    arrayList = np.array(lists)
    arrayListReshape = arraylist.reshape(3, 3) # changes it into 3 by 3 matrix array
    #print(arrayListReshape)
    calculations = {
        'mean': [
            np.mean(arrayListReshape, axis=0).tolist(), # along vertical axiz
            np.mean(arrayListReshape, axis=1).tolist(), # along horizontal axis
            np.mean(arrayListReshape)
        ],
        'variance': [
            np.var(arrayListReshape, axis=0).tolist(),
            np.var(arrayListReshape, axis=1).tolist(),
            np.var(arrayListReshape.flatten())
        ],
        'standard deviation': [
            np.std(arrayListReshape, axis=0).tolist(),
            np.std(arrayListReshape, axis=1).tolist(),
            np.std(arrayListReshape.flatten())
        ],
        'max': [
            np.max(arrayListReshape, axis=0).tolist(),
            np.max(arrayListReshape, axis=1).tolist(),
            np.max(arrayListReshape.flatten())
        ],
        'min': [
            np.min(arrayListReshape, axis=0).tolist(),
            np.min(arrayListReshape, axis=1).tolist(),
            np.min(arrayListReshape.flatten())
        ],
        'sum': [
            np.sum(arrayListReshape, axis=0).tolist(),
            np.sum(arrayListReshape, axis=1).tolist(),
            np.sum(arrayListReshape.flatten())
        ]
    }
  else:
    raise ValueError('List must contain nine numbers.')
  return calculations


OutpuResult = calculate([34, 45, 67, 23, 78.456, 786, 23, 56])
print(OutpuResult) 

# this will print the computed results: mean, variance, std, max, min and sum in the
# order they are formated above.
