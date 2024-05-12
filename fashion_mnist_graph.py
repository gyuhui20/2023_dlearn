import matplotlib.pyplot as plt 
import numpy as np
import time
import pandas as pd
import tqdm as tqdm

#test graph
print("number of correct answer", acc_test, "/", len(xs_test))

plt.figure(figsize=(5,5))
sample_size = 9
random_idx = np.random.randint(100, size=sample_size)
for i, idx in enumerate(random_idx):
    plt.subplot(3,3,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(xs_test[idx].reshape(28,28), cmap='gray')
    plt.xlabel(f"real:{np.argmax(ys_test[idx])} : predict:{np.argmax(y_test_pred[idx])}")
plt.show()
