from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def home():
    return {"status": "working"}

@app.get("/transcript/{video_id}")
def transcript(video_id: str):

    data = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join(
        item["text"] for item in data
    )

    return {
        "transcript": text
    }
