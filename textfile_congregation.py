import os

texts = []
for filename in os.listdir('texts'):
    with open(os.path.join('texts', filename), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        texts.append([filename, len(lines), lines])

texts.sort(key=lambda x: x[2], reverse=True)

with open('congregated.txt', 'w', encoding='utf-8') as f:
    for i in texts:
        f.write(f"{i[0]}\n")
        f.write(f"{i[1]}\n")
        for y in i[2]:
            f.write(y)
        f.write("\n")
