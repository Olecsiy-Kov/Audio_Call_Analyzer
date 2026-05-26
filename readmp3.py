import whisper

model = whisper.load_model("medium")

result = model.transcribe("sound.mp3", language="uk", fp16=False)

'''text = " ".join([s["text"].strip() for s in result["segments"]])
print(text)

for s in result["segments"]:
    if s["text"].strip().endswith("?"):
        print(s["text"].strip())
    else:
        print(s["text"].strip(), end=" ")

for s in result["segments"]:
    print(f"{s['start']:.1f}-{s['end']:.1f}: {s['text']}")'''

with open("result.txt", "w", encoding="utf-8") as f:
    for s in result["segments"]:
        line = f"[{s['start']:.1f}-{s['end']:.1f}] {s['text']}\n"
        f.write(line)
