from pathlib import Path

slug_page = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog\src\app\blog\[slug]\page.tsx")
slug_page.write_text("""import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { MDXRemote } from 'next-mdx-remote/rsc';

export async function generateStaticParams() {
  const postsDir = path.join(process.cwd(), 'content/posts');
  const files = fs.readdirSync(postsDir);
  return files.map((file) => ({
    slug: file.replace(/\.mdx$/, '')
  }));
}

// Dynamic SEO meta
export async function generateMetadata({ params }) {
  const postPath = path.join(process.cwd(), 'content/posts', `${params.slug}.mdx`);
  const source = fs.readFileSync(postPath, 'utf-8');
  const { data } = matter(source);

  return {
    title: data.title,
    description: data.excerpt || `Read about the origins of ${data.title}`,
    openGraph: {
      title: data.title,
      description: data.excerpt || `Word origin story: ${data.title}`,
    },
    twitter: {
      card: "summary",
      title: data.title,
      description: data.excerpt || `Word origin story: ${data.title}`,
    },
  };
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

print("✅ SEO metadata injection added to blog/[slug]/page.tsx")
