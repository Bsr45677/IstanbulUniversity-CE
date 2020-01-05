import os
from ypackage.markdown import read_first_header


DESC_DERS = r"""---
description: >-
  {} için ders konuları, içeriği veya
  notları
---

"""
DESC_SINAV = r"""---
description: >-
  {} için sınav soruları, çıkmış sorular, çıkmışlar, önceki senelerde çıkan sorular
---

"""
DESC_OGR = r"""---
description: >-
  {} için öğrenci notları, el yazıları, tutulmuş notlar
  notları
---

"""

DESC_KARMA = r"""---
description: >-
  {} için karışık, düzenlememiş, eski içerikler
---

"""

DESC_GENEL = r"""---
description: >-
  {} için genel, düzenlenmemiş, duyuru veya ek ders kaynağı notları
---

"""


def repeat(func):
    for l1 in os.listdir():
        if "donem" in l1:
            l1 = os.path.join(os.getcwd(), l1)
            for l2 in os.listdir(l1):
                l2 = os.path.join(l1, l2)
                if os.path.isdir(l2):
                    for l3 in os.listdir(l2):
                        l3 = os.path.join(l2, l3)
                        if os.path.isdir(l3):
                            for l4 in os.listdir(l3):
                                if "README" in l4:
                                    l4 = os.path.join(l3, l4)
                                    func(l4)


def renew(path):
    header = read_first_header(path)

    lesson_path = os.path.join(os.path.dirname(os.path.dirname(path)), "README.md")
    lesson_header = read_first_header(lesson_path)
    lesson_header = lesson_header[lesson_header.find(" ") + 1:]  # Emojiyi kaldırma

    pattern = ""
    for name in lesson_header.split(" "):
        pattern += name[0]

    pattern = r" \| " + pattern
    if r" \| " in header:
        header = header[:header.find(r" \| ")]

    header += pattern

    filestr = ""
    description = ""
    if "Öğrenci" in header:
        description = DESC_OGR
    elif "Ders" in header:
        description = DESC_DERS
    elif "Sınav" in header:
        description = DESC_SINAV
    elif "Karma" in header:
        description = DESC_KARMA
    elif "Genel" in header:
        description = DESC_GENEL
    filestr = description.format(lesson_header)

    read = False
    filestr += "# " + header + "\n"
    with open(path, "r+", encoding="utf-8") as file:
        for line in file:
            if not read and "# " in line:
                read = True
                continue
            if read:
                filestr += line
    with open(path, "w", encoding="utf-8") as file:
        file.write(filestr)


repeat(renew)
