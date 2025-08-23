from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable,NoTranscriptFound

from pytube import YouTube
from typing import Optional, List
import yt_dlp
import logging
from functools import lru_cache
import logging
import os
import tempfile
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def _normalize_text(chunks:List[dict]) -> str:
    return " ".join(chunks.get("text", "").strip() for chunks in chunks if chunks.get("text"))


# helps to retry the function in case of errors
@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.8, min=1, max=6),
    retry=retry_if_exception_type(
        (Exception, TranscriptsDisabled, VideoUnavailable, NoTranscriptFound)
    )
)

# fetching from youtube api
def _fetch_transcript(video_id: str) -> Optional[str]:
    try:
        transcript = YouTubeTranscriptApi.fetch(video_id, languages=["en"])
        return _normalize_text(transcript)
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        logger.error(f"Captions not  for video {video_id}: {e}")
    except VideoUnavailable as e:
        logger.error(f"Video {video_id} is unavailable: {e}")
    return None
    
     
#if auto captions are not available, we can use yt-dlp to download the video and extract the captions 
def fetch_with_yt_dlp(video_id: str) -> Optional[str]:  
        url = f"https://www.youtube.com/watch?v={video_id}"
        
        with tempfile.TemporaryDirectory() as tempdir:
            ydl_opts = {
            "skip_download": True,
            "writesubtitles": True,
            "writeautomaticsub": True,     # allow auto-generated
            "subtitlesformat": "srt",      # easier to parse into text
            "subtitleslangs": ["en", "en-US", "en-GB"],
            "outtmpl": os.path.join(tempdir, "%(id)s.%(ext)s"),
            "quiet": True,
            "nocheckcertificate": True,
        }
            
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                ydl.download([url])  
                
                 # Find a downloaded .srt (if any)
            for fname in os.listdir(tempdir):
                if fname.startswith(video_id) and fname.endswith(".srt"):
                    path = os.path.join(tempdir, fname)
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        # SRT format: keep only the text lines
                        lines = []
                        for line in f:
                            line = line.strip()
                            # skip numeric indexes and timecodes
                            if not line.isdigit() and "-->" not in line and line:
                                lines.append(line)
                        return " ".join(lines)
        except Exception as e:
            logger.info(f"yt-dlp subtitles not available or failed: {e}")

        return None  


def _fetch_with_pytube(video_id: str) -> Optional[str]:
    try:
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        # Try English
        if yt.captions.get("en"):
            return yt.captions["en"].generate_srt_captions()
        # Fallback: any available caption track
        if yt.captions:
            first_key = list(yt.captions.keys())[0]
            return yt.captions[first_key].generate_srt_captions()
    except Exception as e:
        logger.info(f"pytube captions not available or failed: {e}")
    return None


@lru_cache(maxsize=128)

def fetch_transcript_text(video_id: str) -> Optional[str]:
    text = _fetch_transcript(video_id)
    if text:
        return text
    
    text  = fetch_with_yt_dlp(video_id) 
    if text:
        return text
    
    text = _fetch_with_pytube(video_id)
    if text:
        return text 
    
    return None