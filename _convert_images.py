
import subprocess
from pathlib import Path

import glob

for path in glob.glob("images/*.jpg"):
    print("processing", path)
    subprocess.run(["convert", path, "-resize", "50%", "-quality", "80", Path(path).with_suffix(".webp")])



