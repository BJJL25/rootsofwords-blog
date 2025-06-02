import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { MDXRemote } from 'next-mdx-remote/rsc';
import rehypeHighlight from 'rehype-highlight';
import { notFound } from 'next/navigation';

interface Params {
  slug: string;
}

export async function generateStaticParams() {
  const postsDir = path.join(process.cwd(), 'content/posts');
  const filenames = fs.readdirSync(postsDir);

  return filenames
    .filter((name) => name.endsWith('.mdx'))
    .map((name) => ({
      slug: name.replace(/\.mdx$/, ''),
    }));
}

export async function generateMetadata({ params }: { params: Params }) {
  const filePath = path.join(process.cwd(), 'content/posts', `${params.slug}.mdx`);
  const fileContent = fs.readFileSync(filePath, 'utf-8');
  const { data } = matter(fileContent);

  return {
    title: data.title,
    description: data.description,
  };
}

export default function BlogPostPage({ params }: { params: Params }) {
  const filePath = path.join(process.cwd(), 'content/posts', `${params.slug}.mdx`);

  if (!fs.existsSync(filePath)) {
    notFound();
  }

  const fileContent = fs.readFileSync(filePath, 'utf-8');
  const { content, data } = matter(fileContent);

  return (
    <main className="prose mx-auto px-4">
      <h1>{data.title}</h1>
      <p className="text-sm text-gray-500">{data.date}</p>
      <hr className="my-4" />
      <MDXRemote
        source={content}
        options={{
          mdxOptions: {
            rehypePlugins: [rehypeHighlight as any], // 🔧 Fixed: type conflict workaround
          },
        }}
      />
    </main>
  );
}
