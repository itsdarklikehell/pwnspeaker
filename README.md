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
