\
import os
from pathlib import Path
from datetime import datetime

# Define paths
project_root = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog")
posts_dir = project_root / "content" / "posts"
public_dir = project_root / "public"
sitemap_path = public_dir / "sitemap.xml"
robots_path = public_dir / "robots.txt"

# Base site URL
base_url = "https://rootsofwords.com"

# Create public dir if it doesn't exist
public_dir.mkdir(parents=True, exist_ok=True)

# Build sitemap
sitemap_entries = [
    f"<url><loc>{base_url}/</loc><lastmod>{datetime.today().date()}</lastmod></url>",
    f"<url><loc>{base_url}/blog</loc><lastmod>{datetime.today().date()}</lastmod></url>"
]

for file in sorted(posts_dir.glob("*.mdx")):
    slug = file.stem
    sitemap_entries.append(
        f"<url><loc>{base_url}/blog/{slug}</loc><lastmod>{datetime.today().date()}</lastmod></url>"
    )

sitemap_xml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    '\n'.join(sitemap_entries) +
    '\n</urlset>'
)

sitemap_path.write_text(sitemap_xml, encoding="utf-8")

# Create robots.txt
robots_txt = (
    "User-agent: *\n"
    "Allow: /\n\n"
    f"Sitemap: {base_url}/sitemap.xml\n"
)

robots_path.write_text(robots_txt, encoding="utf-8")

print("✅ Generated sitemap.xml and robots.txt in /public")
