import { getAllPosts } from '@/lib/posts';
import { Feed } from 'feed';
import { NextRequest } from 'next/server';
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

export async function GET(req: NextRequest) {
  const siteUrl = 'https://rootsofwords-blog.vercel.app';
  const allPosts = getAllPosts();

  const feed = new Feed({
    title: 'Roots of Words',
    description: 'RSS feed for Roots of Words blog',
    id: siteUrl,
    link: siteUrl,
    language: 'en',
    image: `${siteUrl}/logo.png`,
    favicon: `${siteUrl}/favicon.ico`,
    copyright: `All rights reserved ${new Date().getFullYear()}, Making of a Millionaire Inc.`,
    updated: new Date(allPosts[0]?.date || new Date()),
    generator: 'Feed for Node.js',
    feedLinks: {
      rss: `${siteUrl}/rss.xml`,
    },
    author: {
      name: 'Roots of Words',
      link: siteUrl,
    },
  });

  for (const post of allPosts) {
    const filePath = path.join(process.cwd(), 'content/posts', `${post.slug}.mdx`);
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const { content, data } = matter(fileContent);

    feed.addItem({
      title: post.title,
      id: `${siteUrl}/blog/${post.slug}`,
      link: `${siteUrl}/blog/${post.slug}`,
      date: new Date(post.date),
      description: post.excerpt || '',
      content,
      author: [
        {
          name: 'Roots of Words',
          link: siteUrl,
        },
      ],
      category: (data.tags || []).map((tag: string) => ({ name: tag })),
    });
  }

  return new Response(feed.rss2(), {
    headers: {
      'Content-Type': 'application/rss+xml',
    },
  });
}
