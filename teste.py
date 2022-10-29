import os

os.system(r"ffmpeg -i static\videos\input.mp4 cache\input.png")

path_videos = os.listdir("D:/Leo s files/Projects/Flask/videos-testes")
for i in path_videos:
	os.system(r"ffmpeg -i videos-testes\{} cache\{}.png -n".format(i, i[:-4]))


path_videos = os.listdir("cache")
for i in path_videos:
	print(i)
