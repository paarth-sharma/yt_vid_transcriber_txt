import os
import requests
import yt_dlp

def download_audio_from_youtube(youtube_url, output_file):
    """
    Downloads the audio from a YouTube video and saves it to the specified file.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_file
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def transcribe_with_deepgram(audio_file_path, api_key):
    """
    Transcribes the audio file using Deepgram API and returns the transcript.
    """
    url = "https://api.deepgram.com/v1/listen"
    headers = {
        'Authorization': f'Token {api_key}'
    }
    files = {
        'file': open(audio_file_path, 'rb')
    }
    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        result = response.json()
        return result.get('results', {}).get('channels', [{}])[0].get('alternatives', [{}])[0].get('transcript', '')
    else:
        raise Exception(f"Deepgram API Error: {response.status_code} {response.text}")

def save_transcript_to_file(transcript, output_file):
    """
    Saves the transcript to a text file.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(transcript)

def youtube_to_txt(youtube_url, output_audio, output_text, deepgram_api_key):
    """
    Downloads a YouTube video, transcribes its audio, and saves the transcript to a text file.
    """
    print("Downloading audio from YouTube...")
    download_audio_from_youtube(youtube_url, output_audio)

    print("Transcribing audio with Deepgram...")
    transcript = transcribe_with_deepgram(output_audio, deepgram_api_key)

    print("Saving transcript to text file...")
    save_transcript_to_file(transcript, output_text)
    print("Process completed! Transcript saved to", output_text)

if __name__ == "__main__":
    # Replace these with your actual values
    YOUTUBE_URL = "https://www.youtube.com/watch?YOUR_VIDEO_URL"
    OUTPUT_AUDIO = "audio.mp3"
    OUTPUT_TEXT = "transcript.txt"
    DEEPGRAM_API_KEY = "YOUR_DEEPGRAM_API_KEY"

    try:
        youtube_to_txt(YOUTUBE_URL, OUTPUT_AUDIO, OUTPUT_TEXT, DEEPGRAM_API_KEY)
    except Exception as e:
        print("Error:", e)

