import face_embedding
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser(description='face model test')
# general
parser.add_argument('--image-size', default='112,112', help='')
parser.add_argument('--model', default='../models/model-r34-amf/model,0', help='path to load model.')
parser.add_argument('--gpu', default=0, type=int, help='gpu id')
parser.add_argument('--det', default=2, type=int, help='mtcnn option, 2 means using R+O, else using O')
parser.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
parser.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
args = parser.parse_args()

model = face_embedding.FaceModel(args)
#img = cv2.imread('/raid5data/dplearn/lfw/Jude_Law/Jude_Law_0001.jpg')
img = cv2.imread('/home/deepjunior/PycharmProjects/unit_swap/df_fs/faceswap/experiments/id_distancing/videos/clooney1/images/real_aligned/00227_0.jpg')
f1 = model.get_feature(img)
# img = cv2.imread('/home/deepjunior/PycharmProjects/unit_swap/df_fs/faceswap/experiments/targets/aligned/cage1/cage1_0.jpg')
# img = cv2.imread('/home/deepjunior/PycharmProjects/unit_swap/df_fs/faceswap/experiments/targets/aligned/clooney2/clooney2_0.jpg')
img = cv2.imread('/home/deepjunior/PycharmProjects/unit_swap/df_fs/faceswap/experiments/id_distancing/videos/clooney1/images/de-id_aligned/00227_0.jpg')
f2 = model.get_feature(img)
dist = np.sum(np.square(f1-f2))
print(dist)
sim = np.dot(f1, f2.T)
print(sim)
#diff = np.subtract(source_feature, target_feature)
#dist = np.sum(np.square(diff),1)
