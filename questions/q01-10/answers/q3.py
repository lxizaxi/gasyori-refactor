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


_, binary_image = cv2.threshold(converted_img, 128, 255, cv2.THRESH_BINARY)
ImageUtil.show_image_cv2(binary_image, title="Original Image")

# %%
