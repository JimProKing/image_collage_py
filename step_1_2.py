from PIL import Image, ImageDraw, ImageFont
from step_1_1 import IMG_DIR

img = Image.open(IMG_DIR / "img_001.jpg").convert("RGB")
draw = ImageDraw.Draw(img)

# 여기만 바꿔! → macOS에 무조건 있는 커다란 폰트 3개 중 하나
font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Impact.ttf", 200)
# 만약 Impact 없으면 아래 줄로 바꿔 (순서대로 시도)
# font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Black.ttf", 200)
# font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 200)

draw.text(
    (100, 100),
    "WOW!!",
    fill=(255, 255, 0),          # 노랑
    stroke_width=15,
    stroke_fill=(0, 0, 0),       # 검정 테두리 두껍게
    font=font                    # 이 줄이 핵심!
)

img.save(IMG_DIR / "★진짜_큼.jpg")
img.show()

print("완료! ★진짜_큼.jpg 파일 열어보면 이제 화면 반을 덮을 정도로 큼")