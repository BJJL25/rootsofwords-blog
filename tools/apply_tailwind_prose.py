from pathlib import Path

blog_index_path = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog\src\app\blog\page.tsx")
blog_post_path = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog\src\app\blog\[slug]\page.tsx")

blog_index_path.write_text("""import fs from 'fs';
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
    const slug = filename.replace(/\.mdx$/, '');
    return { ...data, slug };
  });

  return (
    <div className="prose prose-lg max-w-none">
      <h1>Blog</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.slug}>
            <Link href={`/blog/${post.slug}`}>
              <strong>{post.title}</strong> — {post.date}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
""")
blog_post_path.write_text("""import fs from 'fs';
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
    <article className="prose prose-lg max-w-none">
      <h1>{data.title}</h1>
      <p className="text-gray-500 text-sm">{data.date}</p>
      <MDXRemote source={content} />
    </article>
  );
}
""")

print("✅ Tailwind prose styling applied to blog index and post pages.")
