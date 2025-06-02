import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

export type PostMeta = {
  slug: string;
  title: string;
  date: string;
  excerpt: string;
};

const postsDirectory = path.join(process.cwd(), 'content/posts');

export function getAllPosts(): PostMeta[] {
  const fileNames = fs.readdirSync(postsDirectory);

  const posts = fileNames
    .filter((file) => file.endsWith('.mdx'))
    .map((fileName) => {
      const slug = fileName.replace(/\.mdx$/, '');
      const filePath = path.join(postsDirectory, fileName);
      const fileContents = fs.readFileSync(filePath, 'utf8');
      const { data } = matter(fileContents);

      return {
        slug,
        title: data.title,
        date: data.date,
        excerpt: data.excerpt || '',
      };
    });

  return posts.sort(
    (a, b) => new Date(b.date).getTime() - new Date(a.date).getTime()
  );
}
