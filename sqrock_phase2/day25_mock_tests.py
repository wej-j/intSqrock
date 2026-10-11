from PIL import Image
from pathlib import Path

out = Path(".")
out.mkdir(exist_ok=True)

# Genuine PNG
img_png = Image.new("RGB", (32, 32), "white")
img_png.save(out / "benign_test_image.png", format="PNG")

# Genuine JPEG
img_jpg = Image.new("RGB", (32, 32), "white")
img_jpg.save(out / "benign_test_image.jpg", 
             format="JPEG")

# Fake JPEG: text content but .jpg extension
with open(out / "fake_image.jpg", "w", 
          encoding="utf-8") as f:
    f.write("This is not a real JPEG file. It is a safe mock file for magic-byte validation testing.\n")

print(out)
