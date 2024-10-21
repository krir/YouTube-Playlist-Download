import yt_dlp

# Replace with the YouTube playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=PL7GozF-qZ4KeQftuqU3yxvQ-f3eFNUiuJ'

# yt-dlp options for bypassing proxies and maximizing download success
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Download best video + audio available
    'merge_output_format': 'mp4',  # Ensure merged output is MP4
    'outtmpl': r'C:\Users\kkorir\Documents\AWS Training\%(playlist_title)s\%(playlist_index)s - %(title)s.%(ext)s',
    'yesplaylist': True,  # Ensure the entire playlist is processed
    'download_archive': 'downloaded_videos.txt',  # Avoid re-downloading already downloaded videos
    'ignoreerrors': True,  # Skip unavailable videos and continue
    'retries': 10,  # Retry downloads up to 10 times for each video
    'fragment_retries': 15,  # Retry individual video fragments 15 times if they fail
    'concurrent_fragments': 10,  # Download video fragments in parallel to increase speed
    'quiet': False,  # Show progress and logs
    'no_warnings': True,  # Suppress non-critical warnings
    'force_generic_extractor': True,  # Force extractor to avoid potential issues
    'noplaylist': False,  # Ensure full playlist processing
    'proxy': '',  # Use no proxy (forces direct connection even if firewall/proxy exists)
    'throttled-rate': None,  # Remove any throttling imposed by YouTube
}

def download_playlist(playlist_url):
    """Download the entire playlist, bypassing proxies and firewalls."""
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download of the entire playlist: {playlist_url}")
            ydl.download([playlist_url])
            print("Playlist download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    download_playlist(playlist_url)
