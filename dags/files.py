import json 
from pathlib import Path
import requests

def _get_pictures():
    Path("/tmp/images").mkdir(parents=True, exist_ok=True)
    with open("/tmp/launches.json") as f:
        launches = json.load(f)
        image_urls = [launch["image"] for launch in launches["results"] if "image" in launch]
        for url in image_urls:
            try:
                response = requests.get(url)
                image_filename = f"/tmp/images/{url.split('/')[-1]}"
                target_files = Path("/tmp/images") / image_filename
                with open(target_files, "wb") as img_file:
                    img_file.write(response.content)
            except Exception as e:
                print(f"Error processing {url}: {e}")
                