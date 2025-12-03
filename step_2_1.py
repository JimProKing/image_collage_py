from PIL import Image
from step_1_1 import IMG_DIR

# 비율 깨지면서
img = Image.open(IMG_DIR / "img_001.jpg")
print(f"{img.size=}, {img.format=}, {img.mode=}")

SIZE = (500,500)
img_resize = img.resize(SIZE)
print(f"{img_resize.size=}")
img_resize.show()

# 비율 유지하면서
from PIL import ImageOps

img_cont = ImageOps.contain(img,SIZE)
print(f"{img_cont.size = }")
img_cont.show()