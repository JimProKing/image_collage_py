from pathlib import Path

# 현재 스크립트가 있는 폴더를 기준으로 경로 설정
WORK_DIR = Path(__file__).parent
IMG_DIR  = WORK_DIR / "img"      # 원본 이미지들이 들어갈 폴더
IN_DIR   = WORK_DIR / "input"    # 처리할 이미지들을 넣을 폴더
OUT_DIR  = WORK_DIR / "output"   # 결과 콜라주가 저장될 폴더

if __name__ == "__main__":       # 여기서 = 하나를 == 두 개로!
    IMG_DIR.mkdir(exist_ok=True)
    IN_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(exist_ok=True)

    print("폴더 생성 완료!")
    print(f"  원본 이미지 폴더 → {IMG_DIR}")
    print(f"  입력 폴더       → {IN_DIR}")
    print(f"  출력 폴더       → {OUT_DIR}")