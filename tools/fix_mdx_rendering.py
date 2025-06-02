import os
from pathlib import Path
import shutil

# Project directory
project_path = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog")

# Step 1: Remove Contentlayer and related files
print("🧹 Removing Contentlayer...")
contentlayer_files = [
    ".contentlayer",
    "contentlayer.config.ts",
    "src/contentlayer",
]

for name in contentlayer_files:
    path = project_path / name
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
        print(f"Removed: {path}")

# Step 2: Create blog index and dynamic slug page
print("📝 Creating MDX blog pages...")
blog_dir = project_path / "src/app/blog"
slug_dir = blog_dir / "[slug]"
blog_dir.mkdir(parents=True, exist_ok=True)
slug_dir.mkdir(parents=True, exist_ok=True)

# blog/page.tsx
(blog_dir / "page.tsx").write_text("""\
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import Link from 'next/link';

export default async function BlogPage() {
    const postsDir = path.join(process.cwd(), 'content/posts');
    const files = fs.readdirSync(postsDir);
    const posts = files.map((filename) => {
        const filePath = path.join(postsDir, filename);
        const content = fs.readFileSync(filePath, 'utf-8');
        const { data } = matter(content);
        return {
            slug: filename.replace(/\\.mdx$/, ''),
            title: data.title,
            date: data.date,
        };
    });

    return (
        <main className="p-6">
            <h1 className="text-3xl font-bold mb-4">Blog</h1>
            <ul>
                {posts.map((post) => (
                    <li key={post.slug} className="mb-2">
                        <Link href={`/blog/${post.slug}`} className="text-blue-600 hover:underline">
                            {post.title} — {post.date}
                        </Link>
                    </li>
                ))}
            </ul>
        </main>
    );
}
""")

# blog/[slug]/page.tsx
(slug_dir / "page.tsx").write_text("""\
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { MDXRemote } from 'next-mdx-remote/rsc';

export async function generateStaticParams() {
    const postsDir = path.join(process.cwd(), 'content/posts');
    const files = fs.readdirSync(postsDir);
    return files.map((file) => ({
        slug: file.replace(/\\.mdx$/, '')
    }));
}

export default async function PostPage({ params }) {
    const postPath = path.join(process.cwd(), 'content/posts', `${params.slug}.mdx`);
    const source = fs.readFileSync(postPath, 'utf-8');
    const { content, data } = matter(source);

    return (
        <main className="p-6 prose prose-lg">
            <h1>{data.title}</h1>
            <p className="text-gray-500 text-sm">{data.date}</p>
            <MDXRemote source={content} />
        </main>
    );
}
""")

print("✅ MDX rendering setup complete. Run `npm run dev` and visit http://localhost:3000/blog")
