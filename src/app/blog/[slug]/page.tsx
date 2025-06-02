import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';

// Generate SEO metadata
export async function generateMetadata({ params }: { params: { slug: string } }): Promise<Metadata> {
  const filePath = path.join(process.cwd(), 'content/posts', `${params.slug}.mdx`);

  if (!fs.existsSync(filePath)) {
    return notFound();
  }

  const fileContent = fs.readFileSync(filePath, 'utf-8');
  const { data } = matter(fileContent);

  return {
    title: data.title,
    description: data.excerpt || 'Roots of Words blog post',
  };
}

export default async function BlogPost({ params }: { params: { slug: string } }) {
  const filePath = path.join(process.cwd(), 'content/posts', `${params.slug}.mdx`);

  if (!fs.existsSync(filePath)) {
    return notFound();
  }

  const fileContent = fs.readFileSync(filePath, 'utf-8');
  const { content, data } = matter(fileContent);

  // ✅ Dynamically import & safely cast rehype-highlight to avoid type conflict
  const rehypeHighlight = (await import('rehype-highlight')).default as any;

  return (
    <article className="prose lg:prose-xl max-w-3xl mx-auto">
      <h1>{data.title}</h1>
      <p className="text-sm text-gray-500">{data.date}</p>
      <hr className="my-4" />
      <MDXRemote source={content} options={{ mdxOptions: { rehypePlugins: [rehypeHighlight] } }} />
    </article>
  );
}
