"""
Prerequisites:
instalation using pip
    pytube
    instaloader
    PyMovieDb

"""

#Function for Display  
def main_display():
  print(" \t\t********************************************")
  print("\t\t   What type of action you want to execute")
  print(" \t\t********************************************")
  print("\n\t\t\t 1. YouTube Downloder")
  print("\n\t\t\t 2. Instagram Downloder")
  print("\n\t\t\t 3. IDMb Downloder\n\n")

  choice = int(input("Enter your choice: "))

  if (choice == 1):
    print("YouTube Downloader Activated!")
    ytdl()

  elif (choice == 2):
    print("Instagram Downloader Activated!")
    igdl()

  elif (choice == 3):
    print("IMDb Servers loading...")
    imdb()

  else:
    print("Invalid Input")

# For Download Choice
def download_choice():
  print(" \t\t****************************************")
  print("\t\t    What do you want me to download")
  print(" \t\t****************************************")
  print("\n\t\t\t\t 1. Video")
  print("\n\t\t\t\t 2. Audio")
  print("\n\t\t\t\t 3. Info")

# YouTube Downloder
def ytdl():

  from pytube import YouTube as ytd, Playlist as pld
  from pytube.cli import on_progress

  link = str(input("Enter the link: "))
  yt = ytd(link,on_progress_callback=on_progress)
  pl = pld(link)

  a = int(input("The Link you entered is a:- 1.Single Video 2.Playlist: "))
  download_choice()
  dl = int(input("\t: "))

  #for video
  if (a == 1 and dl == 1):
        rel = input("\nEnter the Resolution you need:- 1.High 2.Low: ")
        if (rel == 1):
          yt.streams.filter(resolution= "720p", subtype= ".mkv").first().download()
          print("\nVideo Successfully Downloaded!!!")

        else:
          yt.streams.last().download()
          print("\nVideo Successfully Downloaded!!!")

  elif (a == 1 and dl == 2):
        yt.streams.filter(only_audio=True, progressive=False).first().download()
        print("\nAudio Successfully Downloaded!!!")

  elif (a == 1 and dl == 3):
        print("Title: ", yt.title)
        print("Author: ", yt.author)
        print("Published date: ", yt.publish_date.strftime("%Y-%m-%d"))
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length, "seconds")
        print("Thumbnail Link: ", yt.thumbnail_url)

  #for playlist
  elif (a == 2 and dl == 1):
   
        rel = input("\nEnter the Resolution you need: 1.High 2.Low: \n")
        if (rel == 1):
          for video in pl.videos:
            video.streams.first().download()
          print("\nPlaylist Successfully Downloaded!!!")

        else:
          for video in pl.videos:
            video.streams.last().download()
          print("\nPlaylist Successfully Downloaded!!!")

  elif (a == 2 and dl == 2):
        yt.streams.filter(only_audio=True,progressive=False).first().download().all()
        print("\nAudios Successfully Downloaded!!!")

  elif (a == 2 and dl == 3):
        print("Number of videos in playlist: %s" % len(pl.video_urls))
        print("Author:", yt.author)
        print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
        print("Number of views: ", yt.views)
        print("Thumbnail Link: ", yt.thumbnail_url)

  else:
      print("Invalid Input")

# Insta Downloader
from instaloader import Instaloader as ig
def igdl():

  dp = input("Enter Insta username : ")
  print("Downloading media...")
  ig.download_profile(dp , profile_pic_only=True)
  print("Download complete")
  
# IMDb Scrapper
def imdb():

  from PyMovieDb import IMDB as ia

  name = str(input("\nEnter the name of movie/series you want info about:"))
  res = ia.search(name)

  id = int(input("\n Which One? Copy paste the exact \"id\" from above list:\n"))
  print(ia.get_by_id(id))

main_display()