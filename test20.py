import numpy as np
import os

import cv2
import math
from collections import Counter
import matplotlib.pyplot as plt

import time
import sys
import os
import glob

from scipy.ndimage import gaussian_filter
import scipy

from collections import Counter
from sklearn.cluster import KMeans

import pandas as pd
import tarfile
import shutil  # shutil模块可以复制、移动文件，也可以解压和压缩文件
from zipfile import ZipFile


from collections import Counter
import glob

from datetime import datetime


import subprocess

import pptx
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_PARAGRAPH_ALIGNMENT



import sklearn
# import gensim

# import tensorflow as tf

# import keras
import torch

import h5py

from scipy.io import loadmat


# orginal_files_path = '/Users/tonygrant/Documents/apple all work-related files_20250526/some colleagues requests/apple pencil/1m Granite Plinko Random Drop100_DOE_X-Ray/T0'

orginal_files_path = '/Users/tonygrant/Documents/apple all work-related files_20250526/some colleagues requests/apple pencil/1m Granite Plinko Random Drop100_DOE_X-Ray/Drop100'



saved_path = '/Users/tonygrant/Documents/apple all work-related files_20250526/some colleagues requests/apple pencil/1m Granite Plinko Random Drop100_DOE_X-Ray/input/post'


ff = os.listdir(orginal_files_path)


print(ff)

for f in ff:
	if ".jpg" in f:
		
		new_name = f.replace("_","-")
		
		# shutil.copy(os.path.join(orginal_files_path,f),os.path.join(saved_path,new_name))








