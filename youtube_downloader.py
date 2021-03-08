from pytube import YouTube
from pytube import Playlist


location="E:/videos"
download = int(input("""
1.video
2.playlist
\n
"""))

if download is int(1):

    url = input("Enter the link of the video\n")
    youtube_object = YouTube(url)

    Quality = int(input("""
    1.audio
    2.480p
    3.720p
    \n
    """))
    try:
        if Quality is int(1):
            youtube_object.streams.filter(only_audio=True).first().download(output_path=location)
        elif Quality is int(2):
            youtube_object.streams.filter(res="480p").first().download(output_path=location)
        elif Quality is int(3):
            youtube_object.streams.filter(res="720p").first().download(output_path=location)

        print("done")
    except:
        print("error")


elif download is int(2):
    Playlist_link = input("Enter the link of the play list")
    Playlist = Playlist(Playlist_link)
    Quality = int(input("""
    1.audio
    4.480p
    5.720p
    \n
    """))

    try:
        if Quality is int(1):
            for video in Playlist.videos:
                video.streams.filter(only_audio=True).first().download(output_path=location)
        elif Quality is int(2):
            for video in Playlist.videos:
                video.streams.filter(res="480p").first().download(output_path=location)
        elif Quality is int(3):
            for video in Playlist.videos:
                video.streams.filter(res="720p").first().download(output_path=location)

        print("done")
    except:
        print("error")
