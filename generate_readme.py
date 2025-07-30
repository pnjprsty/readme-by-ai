import os
from dotenv import load_dotenv
from groq import Groq
import pathspec

# === Load API Key dari .env ===
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. CONFIG
EXTENSIONS = ['.js', '.ts', '.vue', '.py', '.json', '.md']
EXCLUDE_DIRS = ['node_modules', '.git', 'dist', 'build', '__pycache__']
MAX_TOTAL_CHARS = 100000  # Batas karakter agar tidak overload

def load_ignore_spec(ignore_file=".fileignore"):
    if not os.path.exists(ignore_file):
        return pathspec.PathSpec.from_lines("gitwildmatch", [])
    
    with open(ignore_file) as f:
        patterns = f.read().splitlines()
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)

def get_all_code_files(base_dir):
    files = []
    ignore_spec = load_ignore_spec()
    for root, dirs, filenames in os.walk(base_dir):
        # Filter direktori yang di-ignore
        dirs[:] = [d for d in dirs if not ignore_spec.match_file(os.path.relpath(os.path.join(root, d), base_dir))]
        
        for fname in filenames:
            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, base_dir)

            if ignore_spec.match_file(rel_path):
                continue

            if any(fname.endswith(ext) for ext in EXTENSIONS):
                files.append(full_path)
    return files


def read_files(files, max_chars=MAX_TOTAL_CHARS):
    contents = []
    total = 0
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as file:
                code = file.read()
                if total + len(code) > max_chars:
                    break
                contents.append(f"\n\n# File: {f}\n```{os.path.splitext(f)[1][1:]}\n{code}\n```")
                total += len(code)
        except Exception as e:
            print(f"❌ Skip {f}: {e}")
    return '\n'.join(contents)
def generate_readme_with_llama(prompt_text: str):
    from groq import Groq

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    full_response = ""
    try:
        stream = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": "Kamu adalah asisten yang membantu menulis README.md berkualitas tinggi untuk proyek GitHub."},
                {
                "role": "user",
                "content": (
                    f"Buatkan README.md yang menjelaskan proyek ini, berdasarkan file-file berikut:\n\n"
                    f"{prompt_text}\n\n"
                    "Tulis README dalam bahasa Inggris."
                )
            }
            ],
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            stream=True,
        )

        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content

    except Exception as e:
        print("[❌] Gagal generate README:", str(e))
        return ""

    return full_response

if __name__ == "__main__":
    folder_path = "."  # Ganti dengan path proyek kamu
    files = get_all_code_files(folder_path)
    print(f"📁 Ditemukan {len(files)} file yang relevan")

    content = read_files(files)
    print("📦 Mengirim ke OpenAI...")

    readme = generate_readme_with_llama(content)

    with open("README.md", "w", encoding="utf-8") as out:
        out.write(readme)
    print("✅ README.md berhasil dibuat!")
