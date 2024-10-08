from pytube import YouTube as ytd, Playlist as pld
from pytube.cli import on_progress
from instaloader import Instaloader as ig
from PyMovieDb import IMDB as ia

def main_display():
    print("\n\t\t********************************************")
    print("\t\t   What type of action do you want to execute")
    print("\t\t********************************************")
    print("\n\t\t\t 1. YouTube Downloader")
    print("\n\t\t\t 2. Instagram Downloader")
    print("\n\t\t\t 3. IMDb Downloader\n")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("YouTube Downloader Activated!")
        ytdl()
    elif choice == 2:
        print("Instagram Downloader Activated!")
        igdl()
    elif choice == 3:
        print("IMDb Servers loading...")
        imdb()
    else:
        print("Invalid Input")

def download_choice():
    print("\n\t\t****************************************")
    print("\t\t    What do you want me to download")
    print("\t\t****************************************")
    print("\n\t\t\t\t 1. Video")
    print("\n\t\t\t\t 2. Audio")
    print("\n\t\t\t\t 3. Info")

def progress_bar(stream, chunk, bytes_remaining):
    total = stream.filesize
    current = total - bytes_remaining
    percent = 100 * (current / total)
    bar = ('*' * int(percent)) + ('-' * (100 - int(percent)))
    print(f"\r |{bar}| {percent:.2f}%", end="\r")

# YouTube Downloader
def ytdl():
    link = input("Enter the link: ")
    yt = ytd(link, on_progress_callback=progress_bar)
    content_type = int(input("\nThe Link you entered is a: 1.Single Video 2.Playlist: "))
    if content_type == 1:
        download_choice()
        dl_choice = int(input("\n: "))
        if dl_choice == 1:  # Video
            resolution = int(input("\nEnter the Resolution you need: 1.High 2.Low: "))
            stream = yt.streams.filter(resolution="720p").first() if resolution == 1 else yt.streams.last()
            stream.download()
            print("\nVideo Successfully Downloaded!!!")
        elif dl_choice == 2:  # Audio
            yt.streams.filter(only_audio=True, progressive=False).first().download()
            print("\nAudio Successfully Downloaded!!!")
        elif dl_choice == 3:  # Info
            print(f"Title: {yt.title}")
            print(f"Author: {yt.author}")
            print(f"Published date: {yt.publish_date.strftime('%Y-%m-%d')}")
            print(f"Number of views: {yt.views}")
            print(f"Length of video: {yt.length} seconds")
            print(f"Thumbnail Link: {yt.thumbnail_url}")
        else:
            print("Invalid Input")
    
    elif content_type == 2:  # Playlist
        pl = pld(link)
        download_choice()
        dl_choice = int(input("\n: "))
        if dl_choice == 1:  # Video
            for video in pl.videos:
                video.streams.first().download()
            print("\nPlaylist Successfully Downloaded!!!")
        elif dl_choice == 2:  # Audio
            for video in pl.videos:
                video.streams.filter(only_audio=True, progressive=False).first().download()
            print("\nAudios Successfully Downloaded!!!")
        elif dl_choice == 3:  # Info
            print(f"Number of videos in playlist: {len(pl.video_urls)}")
            print(f"Author: {pl.title}")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")

# Instagram Downloader
def igdl():
    profile_loader = ig()
    print("\n1. Download Profile Picture")
    print("2. Download IGTV Videos")
    choice = int(input("Enter your choice: "))
    username = input("Enter the username: ")
    try:
        if choice == 1:
            profile_loader.download_profile(username, profile_pic_only=True)
            print("Profile picture downloaded successfully!")
        elif choice == 2:
            profile_loader.download_igtv(username)
            print("IGTV videos downloaded successfully!")
        else:
            print("Invalid Input")
    except Exception as e:
        print(f"An error occurred: {e}")

# IMDb Scraper
def imdb():
    name = input("\nEnter the name of the movie/series you want info about: ")
    res = ia.search(name)
    id = int(input("\nWhich One? Copy-paste the exact \"id\" from the above list:\n"))
    print(ia.get_by_id(id))

if __name__ == "__main__":
    main_display()
