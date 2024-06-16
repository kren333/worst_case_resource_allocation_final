import shutil
import os

if __name__ == "__main__":
    # bad_paths = [x for x in os.listdir() if "_optimized" in x and "8_8" in x and not os.path.exists(f"{x}/test_converged_weights_fair.pickle")]
    # for dir_path in bad_paths:
    #     shutil.rmtree(dir_path)
    for dir_path in os.listdir():
        if "_optimized" in dir_path and "8" in dir_path:
            shutil.rmtree(dir_path)
    print("removed all outputs!")
