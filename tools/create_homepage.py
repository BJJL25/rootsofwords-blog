from pathlib import Path

output_file = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog\src\app\page.tsx")
output_file.write_text('import Link from \'next/link\';\n\nexport default function HomePage() {\n  return (\n    <main className="prose prose-lg max-w-none p-6">\n      <h1>Welcome to Roots of Words</h1>\n      <p>\n        Dive into the fascinating etymology and surprising origins of everyday English words.\n        Explore the stories behind the language we use — one word at a time.\n      </p>\n      <p>\n        <Link href="/blog">📚 Browse all blog posts</Link>\n      </p>\n    </main>\n  );\n}\n', encoding='utf-8')

print("✅ Homepage (page.tsx) has been written correctly.")
