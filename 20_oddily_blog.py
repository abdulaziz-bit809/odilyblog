#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""20. Oddiy Blog"""
import os
from datetime import datetime
class Blog:
    def __init__(self):
        self.folder = "blog_posts"
        os.makedirs(self.folder, exist_ok=True)
    def create(self, title, content, tags=None):
        date = datetime.now().strftime("%Y-%m-%d")
        fname = f"{date}_{title.replace(' ','_')[:30]}.md"
        path = os.path.join(self.folder, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n*{date}*\n\n")
            if tags: f.write("Teglar: " + ", ".join(tags) + "\n\n")
            f.write(content)
        print("✅", path)
    def list(self):
        for f in sorted(os.listdir(self.folder), reverse=True): print("•", f)
def main():
    b = Blog()
    while True:
        print("\n1.Post 2.Royxat 3.Chiqish")
        c = input("> ")
        if c=="1":
            title = input("Sarlavha: ")
            print("Matn (bosh qator = tugat):")
            lines = []
            while True:
                line = input()
                if not line: break
                lines.append(line)
            tags = [t.strip() for t in input("Teglar: ").split(",") if t.strip()]
            b.create(title, "\n".join(lines), tags)
        elif c=="2": b.list()
        elif c=="3": break
if __name__ == "__main__": main()
