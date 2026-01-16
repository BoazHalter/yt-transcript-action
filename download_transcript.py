import sys
from urllib.parse import urlparse, parse_qs

import youtube_transcript_api
print("Loaded module from:", youtube_transcript_api.__file__)

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    parsed = urlparse(url)
    if parsed.hostname == "youtu.be":
        return parsed.path[1:]
    if parsed.hostname in ("www.youtube.com", "youtube.com", "m.youtube.com"):
        return parse_qs(parsed.query).get("v", [None])[0]
    return None


if __name__ == "__main__":
    url = sys.argv[1]
    video_id = extract_video_id(url)

    if not video_id:
        raise ValueError("Could not extract video ID")

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open("transcript.txt", "w", encoding="utf-8") as f:
        for entry in transcript:
            f.write(entry["text"] + "\n")

    print("Transcript saved.")
