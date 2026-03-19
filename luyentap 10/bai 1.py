#bai 1
import os
def lay_ten_file(path):
    return os.path.basename(path)
def lay_ten_bai_hat(path):
    return os.path.splitext(os.path.basename(path))[0]
path = "d:\\music\\muabai.mp3"
print(lay_ten_file(path))
print(lay_ten_bai_hat(path))
