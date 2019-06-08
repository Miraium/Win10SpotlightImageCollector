# coding: utf-8
import os
import shutil
import glob
import cv2

LOCK_SCREEN_IMAGE_FOLDER = r"AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
OUTPUT_TEMP = "temporary"
OUTPUT_LANDSCAPE = "output_landscape"
OUTPUT_PORTRAIT = "output_portrait"

IMAGE_SIZE_PORTRAIT = (1920, 1080)
IMAGE_SIZE_LANDSCAPE = (1080, 1920)

def main():
    dst_dir = OUTPUT_TEMP
    dst_land = OUTPUT_LANDSCAPE
    dst_port = OUTPUT_PORTRAIT
    os.makedirs(dst_dir, exist_ok=True)
    os.makedirs(dst_land, exist_ok=True)
    os.makedirs(dst_port, exist_ok=True)

    home_dir = os.path.expanduser('~')
    src_dir = os.path.join(home_dir, LOCK_SCREEN_IMAGE_FOLDER)
    glob_word = os.path.join(src_dir, "*")
    src_paths = glob.glob(glob_word)
    for src_path in src_paths:
        # ファイルをテンポラリフォルダに一度コピー
        # コピー時に拡張子を付与して画像化する
        fname = os.path.basename(src_path)
        fname_ext = "{0}.jpg".format(fname)
        dst_path = os.path.join(dst_dir, fname_ext)
        shutil.copy2(src_path, dst_path)

        # 画像として読み込み
        img = cv2.imread(dst_path)
        # 画像として読み込めないファイルは不要なため削除
        if img is None:
            os.remove(dst_path)
            continue
        # 画像のサイズを取得
        rows = img.shape[0]
        cols = img.shape[1]
        img_size = (rows, cols)
        # 画像サイズに応じて仕分け
        if img_size == IMAGE_SIZE_PORTRAIT:
            # 縦長の画像
            dst_port_path = os.path.join(dst_port, fname_ext)
            shutil.move(dst_path, dst_port_path)
        elif img_size == IMAGE_SIZE_LANDSCAPE:
            # 横長の画像
            dst_land_path = os.path.join(dst_land, fname_ext)
            shutil.move(dst_path, dst_land_path)
        else:
            # アイコン画像などそれ以外の小さな画像
            # print("Useless:", img.shape)
            pass
    # テンポラリフォルダは不要なため削除してしまう
    shutil.rmtree(dst_dir)

if __name__ == "__main__":
    main()
