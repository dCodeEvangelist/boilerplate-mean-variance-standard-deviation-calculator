import numpy as np

def calculate(list):

  if len(list) == 9:

    arrayList = np.array(list)
    arrayListReshape = arrayList.reshape(3, 3) # convert to 3 by 3 dimentional array or matrix
    
    calculations = {
        'mean': [
            np.mean(arrayListReshape, axis=0).tolist(),  # along horizontal axis
            np.mean(arrayListReshape, axis=1).tolist(),  # along vertical  axis
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
  return calculations # transfer controls out of the function: calculate


outputResult = calculate([24, 55, 17, 24, 88, 56, 7, 23, 56])
print(outputResult) # print out result as formated above in the dictionary calculations above!
