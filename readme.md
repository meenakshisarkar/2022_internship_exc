# Coding Assigment for the 2022 Fall internship @GCDSL

## Objective
  - The main.py generates the InceptionV3 cosine similarity between the ground truth and the predicted frames given by the data path. 
  - The directory *../data/*  has 60 color images (30 ground truth frames given by prefix: gt_ and 30 predicted frames given by prefix: pred_) 
  
## Input arguments:
  **data_root**=  root directory for data, default='../data'.\
  **log_dir**= path to the folder where you save your concatenated frame and .npz file, default='../log'.\
  **seed**= namually fixing the seed value for reproducibility of the code and values.\
  **n_past**= number of past frames after which inception similarity index to be calculated for the #n_future of image frames, type=int, default=5.\
  **n_future**= number of future frames on which we calculate inception cosine similarity, type=int, default=10.\
  **datatype**= color/grayscale, default='color'.\
  **image_h**= Frame height,type=int, dest="image_h",default=128\
  **image_w**= Frame width,type=int, dest="image_w",default=128\
  **gpu**= gpu id on server, type=str, default="1". n.d: If you do not have gpu access you can modify this argument and write cpu compatible code.

You can add any additional input arguments in the main program, but we am going to run your code only using these **PREDEFINED SET OF ARGUMENTS** during testing.\
We will also be testing your code with values other than the default values during testing excpet for seed, image_h, image_w, gpu and data_root.

## Output:
  Generates a plot ***Iv3_cos_sim.png*** and an ***Iv3_similarity.npz*** file in the log_dir. 
  
  The Iv3_cos_sim.png shows the cosine similairty between the ground truth frames and the predicted frames for the n_future number of frames. The corresponding similarity values are to be stored in ***Iv3_similarity.npz***.
  
  For eg. if n_past = 10 and n_future = 7, then the cosine similarity needs to be evaluated for frame titled gt_0010.png and pred_0010 till gt_0017 and pred_0017.png.
  
  ## Test time code execution command from src folder
  
 ```
 python main.py --log_dir path/to/log_dir --datatype color --n_past 10 --n_future 20
