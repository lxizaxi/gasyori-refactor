# %%
# ------------------------ #
import sys

# import project root
sys.path.append("../../../")
# ------------------------ #


import cv2
from cv2.typing import MatLike

from utils.image_util import ImageUtil

original_img: MatLike = ImageUtil.get_asset("imori.jpg")

converted_img: MatLike = cv2.cvtColor(original_img, cv2.COLOR_RGB2GRAY)
ImageUtil.show_image_cv2(converted_img, title="Original Image")

# %%
