from dataclasses import dataclass
from pathlib import Path

import cv2
from cv2.typing import MatLike
from matplotlib import pyplot as plt


@dataclass
class ImageUtil:
    @staticmethod
    def show_image_cv2(img: MatLike, title: str = "Image") -> None:
        rgb_ima: MatLike = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgb_ima)
        plt.title(title)
        plt.axis("off")
        plt.show()

    @staticmethod
    def get_asset_path(asset_name: str) -> Path:
        assets_path: Path = Path(__file__).parent.parent / "assets"
        paths: list[Path] = [p for p in assets_path.iterdir() if p.name == asset_name]

        if len(paths) != 1:
            raise Exception(f"Asset {asset_name} not specified")
        return paths[0]

    @staticmethod
    def get_asset(asset_name: str) -> MatLike:
        asset_path: Path = ImageUtil.get_asset_path(asset_name)
        return cv2.imread(str(asset_path), cv2.IMREAD_COLOR)
