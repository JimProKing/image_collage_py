from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from step_1_1 import OUT_DIR
from step_3_2 import OUT_3_2

# 원본 이미지 열기
img_raw = Image.open(OUT_3_2).convert("RGBA")
text = "공주님 최고야~!!"

# macOS에 무조건 있는 한글 지원 폰트 순서대로 시도 (하나라도 걸리면 끝!)
font_paths = [
    "/System/Library/Fonts/AppleGothic.ttf",           # 제일 확실한 기본 한글 폰트
    "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",  # 유니코드 완벽 지원
    "/Library/Fonts/NanumGothic.ttf",                  # 나눔고딕 있으면 최고
    "/System/Library/Fonts/Supplemental/Times New Roman.ttf",  # 이건 영문만
]

font = None
for fp in font_paths:
    try:
        font = ImageFont.truetype(fp, 120)
        print(f"폰트 찾음! → {Path(fp).name}")
        break
    except:
        continue

# 그래도 다 실패하면? → 최소한 네모는 안 뜨게 강제로 NanumGothic 다운로드 방식 (보너스)
if font is None:
    print("시스템 폰트 없음 → 나눔고딕 자동 설치 중...")
    import subprocess
    subprocess.run(["curl", "-L", "-o", "/tmp/NanumGothic.ttf", 
                    "https://github.com/naver/nanumfont/raw/master/font/NanumGothic.ttf"])
    font = ImageFont.truetype("/tmp/NanumGothic.ttf", 120)

# 글자 크기 계산
left, top, right, bottom = font.getbbox(text)
w = right - left
h = bottom - top

pad = 40
bg_w = w + pad * 2
bg_h = h + pad * 2

# 최종 이미지
img_final = img_raw.copy()
draw = ImageDraw.Draw(img_final)

# 반투명 검정 박스
draw.rectangle((0, 0, bg_w, bg_h), fill=(0, 0, 0, 190))

# 흰색 + 검정 테두리 글자 (진짜 안 깨지고 예쁨!)
draw.text((pad, pad), text, font=font, fill=(255, 255, 255),
          stroke_width=8, stroke_fill=(0, 0, 0))

# 저장 + 약간의 그림자 효과 (선택)
draw.text((pad+4, pad+4), text, font=font, fill=(0, 0, 0, 100))

# 저장
output_path = OUT_DIR / "공주님_최고_완성.jpg"
img_final.convert("RGB").save(output_path)
img_final.convert("RGB").show()

print(f"완료! → {output_path}")