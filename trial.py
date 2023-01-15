"""
Prerequisites:
instalation using pip
    pytube
    PyMovieDb

"""


def main_display():
  print(" \t\t********************************************")
  print("\t\t   What type of action you want to execute")
  print(" \t\t********************************************")
  print("\n\t\t\t 1. YouTube Downloder")
  print("\n\t\t\t 2. Instagram Downloder")
  print("\n\t\t\t 3. IDMb Downloder\n\n")

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
  print(" \t\t****************************************")
  print("\t\t    What do you want me to download")
  print(" \t\t****************************************")
  print("\n\t\t\t\t 1. Video")
  print("\n\t\t\t\t 2. Audio")
  print("\n\t\t\t\t 3. Info")

# Progress bar
# def progress_bar(progress, total):
#   per = 100 * (progress / float(total))
#   bar = ('|' * int(per)) + ('-' * (100 - int(per)))
#   print(f"\r |{bar}| {per:.2f}%", end="\r")

  #alt 175 till 179


# YouTube Downloder


def ytdl():

  from pytube import YouTube as ytd, Playlist as pld
  from pytube.cli import on_progress

  link = str(input("Enter the link: "))
  yt = ytd(link,on_progress_callback=on_progress)

  a = int(input("\nThe Link you entered is a: 1.Single Video 2.Playlist: "))

  #for video
  if a == 1:
        download_choice()
        dl = int(input("\n: "))
        if dl == 1:
            rel = input("\nEnter the Resolution you need: 1.High 2.Low: \n")
            if rel == 1:
                yt.streams.first().download()
                # progress_bar(0, r_time)
                print("\nVideo Successfully Downloaded!!!")

            else:
                yt.streams.last().download()
                # progress_bar(0, r_time)
                print("\nVideo Successfully Downloaded!!!")

        elif dl == 2:
            yt.streams.filter(only_audio=True, progressive=False).first().download()
            # progress_bar(0, r_time)
            print("\nAudio Successfully Downloaded!!!")

        elif dl == 3:
            print("Title: ", yt.title)
            print("Author: ", yt.author)
            print("Published date: ", yt.publish_date.strftime("%Y-%m-%d"))
            print("Number of views: ", yt.views)
            print("Length of video: ", yt.length, "seconds")
            print("Thumbnail Link: ", yt.thumbnail_url)

        else:
           print("Invalid Input")

  #for playlist
  elif a == 2:
        pl = pl(link)
        download_choice()
        dl = int(input("\n: "))
        if dl == 1:
          rel = input("\nEnter the Resolution you need: 1.High 2.Low: \n")
          if rel == 1:
            for video in pl.videos:
              video.streams.first().download()
            # progress_bar(0, r_time)
            print("\nPlaylist Successfully Downloaded!!!")

          else:
            for video in pl.videos:
              video.streams.last().download()
            # progress_bar(0, r_time)
            print("\nPlaylist Successfully Downloaded!!!")

        elif dl == 2:
          yt.streams.filter(only_audio=True,progressive=False).first().download().all()
          # progress_bar(0, r_time)
          print("\nAudios Successfully Downloaded!!!")

        elif dl == 3:
          print("Number of videos in playlist: %s" % len(pl.video_urls))
          print("Author:", yt.author)
          print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
          print("Number of views: ", yt.views)
          print("Thumbnail Link: ", yt.thumbnail_url)

        else:
          print("Invalid Input")
  else:
      print("Invalid Input")


# Insta Downloader
def igdl():

  link = str(input("Enter the link: "))

# IMDb Scrapper
def imdb():

  from PyMovieDb import IMDB as ia

  name = str(input("\nEnter the name of movie/series you want info about:"))
  res = ia.search(name)

  id = int(
    input("\n Which One? Copy paste the exact \"id\" from above list:\n"))
  print(ia.get_by_id(id))

main_display()



#https://www.instagram.com/eel/CYa0KIwtjjL/?utm_medium=share_sheet
#indian.tweets


#Syncing download n progress bar
def progress_bar(progress,total):
  per = 100 * (progress/float(total))
  bar = '*' * int(per) + '-' * (100-int(per))
  print(f"\r |{bar}| {per:.2f}%", end="\r")
       
from pytube import YouTube as ytd

link = str(input("Enter the link: "))
yt = ytd(link)

import asyncio

async def dl():
   yt.streams.first().download()

async def pb():
   for i in range(0,100):
    progress_bar(i,)

if __name__ == "__main__":
   loop = asyncio.get_event_loop()
   loop.run_until_complete(asyncio.gather(dl(), pb()))

print("\nVideo Successfully Downloaded!!!")
