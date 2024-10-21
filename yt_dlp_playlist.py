import yt_dlp

# The playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=PL7GozF-qZ4KeQftuqU3yxvQ-f3eFNUiuJ'

# yt-dlp options
ydl_opts = {
    'format': 'best',  # Download the best available quality
    'outtmpl': r'C:\Users\kkorir\Documents\AWS Training\%(playlist_title)s\%(playlist_index)s - %(title)s.%(ext)s',
    # Save videos in a folder named after the playlist, with numbered filenames
    'playlist_items': '1-10',  # Download only the first 5 videos; remove or modify to download more
    'yesplaylist': True,  # Ensure the entire playlist is processed
}

try:
    # Create a YoutubeDL instance with the provided options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading playlist from: {playlist_url}")
        ydl.download([playlist_url])
    print("Playlist download completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
