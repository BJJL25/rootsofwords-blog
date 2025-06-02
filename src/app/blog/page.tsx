import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import Link from 'next/link';

type Post = {
  slug: string;
  title: string;
  date: string;
  excerpt: string;
};

export default function BlogPage() {
  const postsDirectory = path.join(process.cwd(), 'content/posts');
  const filenames = fs.readdirSync(postsDirectory);

  const posts: Post[] = filenames.map((filename) => {
    const slug = filename.replace(/\.mdx?$/, '');
    const filePath = path.join(postsDirectory, filename);
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const { data, content } = matter(fileContent);

    const excerpt = content.split(' ').slice(0, 30).join(' ') + '...';

    return {
      slug,
      title: data.title,
      date: new Date(data.date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      }),
      excerpt,
    };
  }).sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

  return (
    <main className="max-w-3xl mx-auto py-12 px-4">
      <h1 className="text-3xl font-bold mb-6">Blog</h1>
      <ul className="space-y-8">
        {posts.map((post) => (
          <li key={post.slug}>
            <h2 className="text-2xl font-semibold">
              <Link href={`/blog/${post.slug}`}>
                {post.title}
              </Link>
            </h2>
            <p className="text-sm text-gray-500 mb-2">{post.date}</p>
            <p className="mb-2">{post.excerpt}</p>
            <Link href={`/blog/${post.slug}`} className="text-blue-600 hover:underline">Read more →</Link>
          </li>
        ))}
      </ul>
    </main>
  );
}
