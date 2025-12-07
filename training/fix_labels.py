import os

# Etiket klasörlerinin yolları
label_dirs = [
    "C:/Users/iremd/cv-advanced-assessment/dataset/labels/train",
    "C:/Users/iremd/cv-advanced-assessment/dataset/labels/val"
]

# COCO → YOLO yeni mapping
mapping = {
    0: 0,   # person
    2: 1,   # car
    7: 2    # truck
}

def fix_label_file(path):
    new_lines = []
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            cls = int(parts[0])
            coords = parts[1:]

            if cls in mapping:
                new_cls = mapping[cls]
                new_line = str(new_cls) + " " + " ".join(coords)
                new_lines.append(new_line)

    # Eğer hiç uygun sınıf yoksa dosyayı boş bırakıyoruz
    with open(path, "w") as f:
        f.write("\n".join(new_lines))


print("Dönüşüm başlıyor...\n")

for folder in label_dirs:
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            fix_label_file(os.path.join(folder, file))

print("Bitti! ✔ Etiketler başarıyla dönüştürüldü.")
print("Artık YOLOv8 eğitimi çalışabilir.")
