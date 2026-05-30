# Audio Transcriber

A Python-based audio transcription tool that automatically converts audio files to text using OpenAI's Whisper model.

## Overview

This project processes audio files from a local directory and transcribes them to Portuguese text using the Whisper ASR (Automatic Speech Recognition) model. It supports multiple audio formats and includes intelligent features like skipping already transcribed files and removing Windows metadata artifacts.

## Features

- 🎙️ **Automatic Audio Transcription** - Transcribes audio files to Portuguese text
- 📁 **Batch Processing** - Processes all audio files in the `audios/` directory
- 🔄 **Smart Skipping** - Skips files that have already been transcribed
- 🎵 **Multiple Format Support** - Handles .mp3, .mp4, .m4a, .wav, .ogg, .flac, and .mkv files
- 📝 **Error Handling** - Gracefully handles transcription errors
- 🧹 **Cleanup** - Removes Windows Zone.Identifier metadata files

## Technologies Used

- **Python** - Programming language
- **[OpenAI Whisper](https://github.com/openai/whisper)** - State-of-the-art speech recognition model
- **Turbo Model** - Fast and accurate Whisper model variant

## Project Structure

```
.
├── README.md                 # Project documentation
├── transcriber.py            # Main transcription script
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
├── audios/                   # Input directory for audio files
├── transcricoes/             # Output directory for transcriptions
└── .venv/                    # Python virtual environment
```

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone or navigate to the project directory**

   ```bash
   cd audio-transcriber
   ```

2. **Create and activate a virtual environment** (optional but recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Add audio files** to the `audios/` directory (supports: .mp3, .mp4, .m4a, .wav, .ogg, .flac, .mkv)

2. **Run the transcriber**

   ```bash
   python transcriber.py
   ```

3. **Find results** in the `transcricoes/` directory as `.txt` files

### Example

```
Input:  audios/meeting.mp3
Output: transcricoes/meeting.txt (contains the Portuguese transcription)
```

## How It Works

1. Loads the Whisper "turbo" model (lightweight and fast)
2. Scans the `audios/` directory for supported audio formats
3. For each audio file:
   - Checks if a transcription already exists (skips if it does)
   - Transcribes the audio to Portuguese
   - Saves the transcription as a text file
   - Handles errors gracefully
4. Cleans up Windows metadata files (Zone.Identifier)
5. Prints progress updates to the console

## Output

Each transcription is saved as a `.txt` file in the `transcricoes/` directory with the same name as the audio file but with a `.txt` extension.

## Error Handling

The script includes try-catch blocks to handle transcription errors. If an error occurs with a specific file, the script will:

- Print the error message
- Continue processing remaining files
- Not interrupt the entire batch operation

## Notes

- The first run may take some time as it downloads the Whisper model
- The "turbo" model is optimized for speed and accuracy
- Language is set to Portuguese - modify `language="Portuguese"` in the script to use other languages
- Already transcribed files are skipped to avoid reprocessing

## License

This project is built upon OpenAI's Whisper model.
