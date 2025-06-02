from pathlib import Path

# Define project root and content/posts folder
project_root = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog")
posts_dir = project_root / "content" / "posts"
posts_dir.mkdir(parents=True, exist_ok=True)

# Create sample post
sample_post = posts_dir / "history-of-salary.mdx"
sample_post.write_text("""---
title: "The History of Salary"
date: "2024-06-01"
tags: ["Latin", "Economics", "Word Origins"]
excerpt: "Discover how the word 'salary' traces back to Roman times and their use of salt as payment."
---

The word **salary** has surprising roots in ancient Rome. The Latin word _salarium_ referred to payments made to Roman soldiers to buy **salt**—a vital and expensive commodity.

Over centuries, the term evolved into modern usage, symbolizing monetary compensation.
""")

print(f"✅ Sample post created at: {sample_post}")
