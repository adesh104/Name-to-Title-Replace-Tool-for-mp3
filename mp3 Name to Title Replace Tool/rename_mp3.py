import os
import re
from mutagen.easyid3 import EasyID3

folder = r"change this"

for file in os.listdir(folder):
    if file.lower().endswith(".mp3"):
        full_path = os.path.join(folder, file)
        try:
            audio = EasyID3(full_path)
            title = audio.get("title", [None])[0]
            if title:
                clean_title = re.sub(r'[\\/*?:"<>|]', "", title).strip()
                new_file = os.path.join(folder, f"{clean_title}.mp3")
                if not os.path.exists(new_file):
                    os.rename(full_path, new_file)
                    print(f"✅ {file} → {clean_title}.mp3")
                else:
                    print(f"⚠️ Skipped: {clean_title}.mp3 already exists")
            else:
                print(f"❌ No title in metadata: {file}")
        except Exception as e:
            print(f"❌ Error in {file}: {e}")
