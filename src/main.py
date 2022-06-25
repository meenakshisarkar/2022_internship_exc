from argparse import ArgumentParser

# ############################################
# The main.py generates the Inception_V3 cosine similarity between #n_future of ground truth and predicted frames given by the data_path.  
# The directory ../data/color  has 60 color images (30 ground truth frames given by prefix: gt_ and 30 predicted frames given by prefix: pred_)
# with 3 color channels (RGB in that order, 64*64*3). 

# ############################################
# Input arguments:
#   data_root=  root directory for data, default='../data'.
#   log_dir= path to the folder where you save your plot and .npz file, default='../log'.
#   seed = namually fixing the seed value for reproducibility of the code and values.
#   datatype= color/grayscale, default='color'.
#   n_past= number of past frames after which Inception_V3 cosine similarity index to be calculated for the #n_future of image frames, type=int, default=5.
#   n_future= number of future frames on which we calculate vgg ccosine similarity, type=int, default=10.
#   image_h= Frame height,type=int, dest="image_h",default=128
#   image_w= Frame width,type=int, dest="image_w",default=128
#   gpu = gpu id on server, type=str, default="1". n.d: If you do not have gpu access you can modify this argument and write cpu compatible code.

def main(args):
    # Write your code here.
    pass


if __name__ == "__main__":
    parser = ArgumentParser()
    parser = ArgumentParser()
    parser.add_argument('--data_root', default='../data', help='root directory for data')
    parser.add_argument('--log_dir', default='../log', help='path to the folder where you save your plot and .npz file')
    parser.add_argument('--seed', default=77, type=int, help='manual seed')
    parser.add_argument('--datatype', default='color', help='color/grayscale')
    parser.add_argument('--n_past', type=int, default=5, help='number of past frames')
    parser.add_argument('--n_future', type=int, default=10, help='number of future frames on which we calculate vgg ccosine similarity')
    parser.add_argument("--image_h", type=int, dest="image_h",default=128, help="Frame height")
    parser.add_argument("--image_w", type=int, dest="image_w",default=128, help="Frame width")
    parser.add_argument('--gpu', type=str, default="1", help='gpu id on server')

    main(parser.parse_args())