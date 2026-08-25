with open("log.txt", "w", encoding="utf-8") as f:
    f.write("2026-08-20,80.5\n")
    f.write("2026-08-21,80.2\n")
    f.write("2026-08-22,79.8\n")


with open("log.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)