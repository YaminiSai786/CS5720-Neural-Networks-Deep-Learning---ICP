# ICP 3 - Program 2
# 2. Numpy  Using NumPy create random vector of size 20 having only float in the range 1-20.  
# Then reshape the array to 4 by 5 Then replace the max in each row by 0 (axis=1) (you can NOT implement it via for loop) 

# Student Name : Yamini Saraswathi Borra
# Student ID : 700748022

import numpy as np

# Create a random vector of size 20 with floats in the range [1, 20]
random_vector = np.random.uniform(1, 20, 20)

# Reshape the array to a 4x5 matrix
reshaped_matrix = random_vector.reshape(4, 5)

# Replace the max value in each row with 0 along axis=1
reshaped_matrix[np.arange(4), np.argmax(reshaped_matrix, axis=1)] = 0

print("Original Matrix:")
print(reshaped_matrix)
