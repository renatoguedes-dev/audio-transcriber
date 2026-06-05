import os

import whisper
from dotenv import load_config, load_dotenv

model = whisper.load_model("turbo")

# Puxa os caminhos do arquivo .env (com um valor padrão caso não encontre)
audio_dir = os.getenv("AUDIO_DIR", "audios")
output_dir = os.getenv("OUTPUT_DIR", "transcricoes")

os.makedirs(output_dir, exist_ok=True)

formats = (".mp3", ".mp4", ".m4a", ".wav", ".ogg", ".flac", ".mkv")


def delete_zone_identifiers(directory):
    for file in os.listdir(directory):
        if "Zone.Identifier" in file:
            zone_path = os.path.join(directory, file)
            os.remove(zone_path)
            print(f"Removido: {file}")


delete_zone_identifiers(audio_dir)

for audio_file in os.listdir(audio_dir):
    if not audio_file.lower().endswith(formats):
        continue

    base_name = os.path.splitext(audio_file)[0]
    output_file = os.path.join(output_dir, f"{base_name}.txt")

    if os.path.exists(output_file):
        print(f"Pulando (já transcrito): {audio_file}")
        continue

    file_path = os.path.join(audio_dir, audio_file)
    print(f"Transcrevendo: {audio_file}")

    try:
        result = model.transcribe(file_path, language="Portuguese")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"  -> Salvo em: {output_file}")

    except Exception as e:
        print(f"  -> ERRO em '{audio_file}': {e}")

print("Concluído!")
