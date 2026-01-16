import sys
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    query = urlparse(url)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(query.query).get("v", [None])[0]
    return None

if __name__ == "__main__":
    url = sys.argv[1]
    video_id = extract_video_id(url)

    if not video_id:
        raise ValueError("Could not extract video ID from URL")

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open("transcript.txt", "w", encoding="utf-8") as f:
        for entry in transcript:
            f.write(entry["text"] + "\n")

    print("Transcript saved to transcript.txt")
