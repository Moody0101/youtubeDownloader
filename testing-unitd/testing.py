from typing import List, Any

from pafy import new

url = 'https://www.youtube.com/watch?v=31HfP81oWDI'
video = new(url)
print(video.author)
print(video.streams)
stream = video.allstreams
print(str(stream))
for i in stream:
    global list1
    print(str(i) + str(i.get_filesize() / 10 ** 6) + "mb")

