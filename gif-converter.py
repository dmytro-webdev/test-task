# install TikTokApi package
# you need to have directory with name 'images_folder' in root folder of the project. If
# there is no, please create.
from TikTokApi import TikTokApi
import cv2
import glob
from PIL import Image
import pathlib

url_link = "https://www.tiktok.com/@s.weetrexs/video/7057529273443290370?is_copy_url=1&is_from_webapp=v1&q=%D0%BA%D0%BE%D1%80%D0%BE%D1%82%D0%BA%D0%B8%D0%B5%20%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE&t=1659387190249"


def download_video_from_tiktok(link):
    api = TikTokApi()
    video = api.video(url=link).bytes()
    with open("video.mp4", "wb") as out_file:
        out_file.write(video)


def convert_mp4_to_jpgs(path):
    video_capture = cv2.VideoCapture(path)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"images_folder/frame_{frame_count:03d}.jpg", image)
        # read next image
        still_reading, image = video_capture.read()
        frame_count += 1


def make_gif(frame_folder):
    images = glob.glob(f"{frame_folder}/*.jpg")
    images.sort()
    frames = [Image.open(image) for image in images]
    frame_one = frames[0]
    frame_one.save("demo.gif", format="GIF", append_images=frames,
                   save_all=True, duration=30, loop=0)


def main(link):
    # download video to local storage:
    download_video_from_tiktok(link)

    # convert video to frames:
    convert_mp4_to_jpgs("video.mp4")

    # make gif from frames
    make_gif("images_folder")

    # get absolute path to the file:
    path = pathlib.Path().absolute()
    full_path = f"{path}/demo.gif"
    print(full_path)


main(url_link)








