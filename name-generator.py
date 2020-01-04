import os
from ypackage.markdown import read_first_header


DESC_DERS = r"""---
description: >-
  Mobil programlama (Mobile Programming) için ders konuları, içeriği veya
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
    lesson = os.path.basename(os.path.dirname(os.path.dirname(path))).split("-")

    lesson_name = ""
    pattern = ""
    for name in lesson:
        if "ve" == name or "to" == name or "and" == name:
            lesson_name += name + " "
            key = name[0]
        else:
            lesson_name += name[0].upper() + name[1:] + " "
            key = name[0].upper()
        pattern += key

    lesson_name = lesson_name[:-1]
    pattern = r" \| " + pattern
    if not pattern in header:
        newheader = header + pattern
    else:
        newheader = header

    filestr = ""
    if "Öğrenci" in header:
        filestr = DESC_OGR.format(lesson_name)
    elif "Ders" in header:
        filestr = DESC_OGR.format(lesson_name)
    elif "Sınav" in header:
        filestr = DESC_SINAV.format(lesson_name)

    read = False
    filestr += "# " + newheader + "\n"
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
