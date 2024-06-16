import os
import shutil

if __name__ == "__main__":
    for dir_path in os.listdir():
        if "_optimized" in dir_path and "8" in dir_path:
            shutil.rmtree(dir_path)
    print("removed all outputs!")
