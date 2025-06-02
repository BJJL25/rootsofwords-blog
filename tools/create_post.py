import os
from datetime import datetime
import re

# Define the content/posts directory
POSTS_DIR = os.path.join(os.getcwd(), "content", "posts")

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

def create_post():
    print("📝 Blog Post Generator")
    title = input("Enter post title: ").strip()
    date = input("Enter post date (YYYY-MM-DD) [default: today]: ").strip()
    slug = input("Enter custom slug [leave blank to auto-generate]: ").strip()

    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    if not slug:
        slug = slugify(title)

    filename = f"{slug}.mdx"
    filepath = os.path.join(POSTS_DIR, filename)

    frontmatter = f"""---
title: {title}
date: {date}
description: ""
---

Write your content here...
"""

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)

    print(f"✅ Created new post: {filepath}")

if __name__ == "__main__":
    create_post()
