import requests, json, base64
import subprocess
ffmpeg = "/usr/local/bin/ffmpeg"

def get_mp3(text):
    ENDPOINT = "https://tiktok-tts.weilnet.workers.dev"
    GEN_ENDPOINT = ENDPOINT + "/api/generation"

    payload = {"text": text, "voice": "en_us_001"}

    x = requests.post(GEN_ENDPOINT, json = payload)
    b64 = json.loads(x.text)['data']
    decoded = base64.b64decode(b64)

    file = open('temp.mp3', 'wb')
    file.write(decoded)
    file.close()

def gen_vid():
    commands = [
        "ffmpeg",
        "-i",
        "/home/nathan/projects/tttts_bot/temp.mp3",
        "-filter_complex",
        "[0:a]showwaves=s=1280x720:mode=line:rate=25,format=yuv420p[v]",
        '-map',
        "[v]",
        '-map',
        '0:a',
        'output.mp4'
    ]

    subprocess.run(commands)

get_mp3("Poo poo pee pee")
gen_vid()