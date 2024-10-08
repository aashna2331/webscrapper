import streamlit as st
from pytube import YouTube as ytd, Playlist as pld
from pytube.cli import on_progress
from instaloader import Instaloader as ig
from PyMovieDb import IMDB as ia

def main_display():
    st.title("Media Downloader")
    st.sidebar.header("Choose an action")
    choice = st.sidebar.radio("Select an option:", ("YouTube Downloader", "Instagram Downloader", "IMDb Downloader"))

    if choice == "YouTube Downloader":
        st.subheader("YouTube Downloader Activated!")
        ytdl()
    elif choice == "Instagram Downloader":
        st.subheader("Instagram Downloader Activated!")
        igdl()
    elif choice == "IMDb Downloader":
        st.subheader("IMDb Servers loading...")
        imdb()

# YouTube Downloader
def ytdl():
    link = st.text_input("Enter the YouTube link:")
    if st.button("Submit"):
        yt = ytd(link, on_progress_callback=progress_bar)
        content_type = st.selectbox("The Link you entered is a:", ("Select", "Single Video", "Playlist"))

        if content_type == "Single Video":
            download_choice = st.selectbox("What do you want me to download:", ("Select", "Video", "Audio", "Info"))
            if download_choice == "Video":
                resolution = st.selectbox("Enter the Resolution you need:", ("Select", "High (720p)", "Low"))
                if resolution:
                    stream = yt.streams.filter(resolution="720p").first() if resolution == "High (720p)" else yt.streams.last()
                    stream.download()
                    st.success("Video Successfully Downloaded!!!")
            elif download_choice == "Audio":
                yt.streams.filter(only_audio=True, progressive=False).first().download()
                st.success("Audio Successfully Downloaded!!!")
            elif download_choice == "Info":
                st.write(f"Title: {yt.title}")
                st.write(f"Author: {yt.author}")
                st.write(f"Published date: {yt.publish_date.strftime('%Y-%m-%d')}")
                st.write(f"Number of views: {yt.views}")
                st.write(f"Length of video: {yt.length} seconds")
                st.image(yt.thumbnail_url)

        elif content_type == "Playlist":
            pl = pld(link)
            download_choice = st.selectbox("What do you want me to download:", ("Select", "Video", "Audio", "Info"))
            if download_choice == "Video":
                for video in pl.videos:
                    video.streams.first().download()
                st.success("Playlist Successfully Downloaded!!!")
            elif download_choice == "Audio":
                for video in pl.videos:
                    video.streams.filter(only_audio=True, progressive=False).first().download()
                st.success("Audios Successfully Downloaded!!!")
            elif download_choice == "Info":
                st.write(f"Number of videos in playlist: {len(pl.video_urls)}")
                st.write(f"Author: {pl.title}")

def progress_bar(stream, chunk, bytes_remaining):
    total = stream.filesize
    current = total - bytes_remaining
    percent = 100 * (current / total)
    st.progress(percent)

# Instagram Downloader
def igdl():
    profile_loader = ig()
    choice = st.selectbox("Select an option:", ("Select", "Download Profile Picture", "Download IGTV Videos"))
    username = st.text_input("Enter the username:")
    
    if st.button("Download"):
        try:
            if choice == "Download Profile Picture":
                profile_loader.download_profile(username, profile_pic_only=True)
                st.success("Profile picture downloaded successfully!")
            elif choice == "Download IGTV Videos":
                profile_loader.download_igtv(username)
                st.success("IGTV videos downloaded successfully!")
            else:
                st.warning("Please select a valid option.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# IMDb Scraper
def imdb():
    name = st.text_input("Enter the name of the movie/series you want info about:")
    if st.button("Search"):
        res = ia.search(name)
        if res:
            id = st.selectbox("Which One? Copy-paste the exact \"id\" from the above list:", [r.id for r in res])
            st.write(ia.get_by_id(id))
        else:
            st.warning("No results found.")

if __name__ == "__main__":
    main_display()
