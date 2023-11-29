# %%
# ------------------------ #
import sys

# import project root
sys.path.append("../../../")
# ------------------------ #

from pathlib import Path

import cv2
from cv2.typing import MatLike

from utils.image_util import ImageUtil

imori_path: Path = ImageUtil.get_asset_path("imori.jpg")
original_img: MatLike = cv2.imread(str(imori_path))

converted_img: MatLike = cv2.cvtColor(original_img, cv2.COLOR_RGB2GRAY)
ImageUtil.show_image_cv2(converted_img, title="Original Image")

# %%
