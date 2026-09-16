# pwnspeaker

Two pwnagotchi plugins:

- **pwnspeaker.py** — text-to-speech: lets your pwnagotchi speak.
- **pwnassistant.py** — voice assistant: reads your Google Calendar and answers by voice.

## Installation

### 1. System dependencies

```bash
sudo apt-get install espeak libespeak1 portaudio19-dev
```

### 2. Python dependencies

```bash
pip3 install -r requirements.txt
```

or manually:

```bash
# pwnspeaker (TTS)
pip3 install pyttsx3 pytz

# pwnassistant (Google Calendar + speech recognition)
pip3 install google-api-python-client google-auth-oauthlib SpeechRecognition pyaudio
```

> **Note:** `googleapiclient` (from the error log `No module named 'googleapiclient'`)
> is provided by the `google-api-python-client` package — the pip name differs from
> the import name. If you see that error, this step was missed.

### 3. Plugins installeren

Copy both plugin files to your custom plugins directory:

```bash
cp pwnspeaker.py pwnassistant.py /etc/pwnagotchi/plugins.d/   # or your custom-plugin path
```

### 4. Config

Add to `/etc/pwnagotchi/config.toml` (or `config.yaml` on older installs):

```toml
[main.plugins.pwnspeaker]
enabled = true

[main.plugins.pwnassistant]
enabled = true
# pwnassistant expects Google OAuth credentials:
# - credentials.json (OAuth client) next to the plugin
# - first run opens a browser flow to authorize calendar read access
```

### 5. Herstart

```bash
sudo systemctl restart pwnagotchi
```

---

## 🎥 Gource Visualization

De ontwikkelhistorie van dit project in een film:

<video src="https://raw.githubusercontent.com/itsdarklikehell/pwnspeaker/master/gource.mp4" controls width="100%"></video>

*De video wordt automatisch gegenereerd door de [Gource workflow](.github/workflows/gource.yml) bij elke push.*

Lokale video genereren:
```bash
gource --max-files 1000 --key -800x600 \
  --highlight-users --filename-time 3 --output-framerate 25 \
  -s 0.6 --multi-sampling --auto-skip-seconds 0.1 \
  --stop-at-end --hide mouse,progress -o gource.ppm

ffmpeg -y -r 15 -f image2pipe -vcodec ppm -i gource.ppm \
  -vcodec libx264 -preset medium -pix_fmt yuv420p \
  -crf 1 -threads 0 -bf 0 gource.mp4
```
