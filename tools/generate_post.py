from pathlib import Path
from datetime import datetime
import re

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

def create_post():
    title = input("📝 Title of the post: ").strip()
    date = input("📅 Date (YYYY-MM-DD) [leave empty for today]: ").strip()
    tags = input("🏷️  Tags (comma separated): ").strip()
    excerpt = input("✏️  Short excerpt (1 sentence): ").strip()

    if not date:
        date = datetime.now().strftime('%Y-%m-%d')

    slug = slugify(title)
    filename = f"{slug}.mdx"
    post_path = Path("content/posts") / filename

    tags_list = [tag.strip() for tag in tags.split(",") if tag.strip()]
    tags_str = "[" + ", ".join(f'\"{tag}\"' for tag in tags_list) + "]"

    frontmatter = f"""---
title: "{title}"
date: "{date}"
tags: {tags_str}
excerpt: "{excerpt}"
---

Start writing **{title}** here.
"""

    post_path.parent.mkdir(parents=True, exist_ok=True)
    post_path.write_text(frontmatter)

    print(f"✅ Post created: {post_path}")

if __name__ == "__main__":
    create_post()
