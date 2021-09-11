import YoutubeTags
from YoutubeTags import videotags

link = str(input("Enter The video Link"))
tags = videotags(link)
print(tags)
