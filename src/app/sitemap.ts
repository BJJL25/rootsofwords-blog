import { getAllPosts } from '@/lib/posts';
import { MetadataRoute } from 'next';

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const baseUrl = 'https://rootsofwords.com';
  const posts = await getAllPosts();
  return [
    {
      url: baseUrl,
      lastModified: new Date(),
    },
    ...posts.map((post) => ({
      url: `${baseUrl}/blog/${post.slug}`,
      lastModified: post.date,
    })),
  ];
}
