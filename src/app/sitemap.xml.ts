import fs from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

export async function GET() {
  const postsDir = path.join(process.cwd(), 'content/posts');
  const files = fs.readdirSync(postsDir);
  const baseUrl = 'https://rootsofwords.com';

  const urls = files.map((filename) => {
    const slug = filename.replace(/\.mdx$/, '');
    return `<url><loc>${baseUrl}/blog/${slug}</loc></url>`;
  });

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.join('\n')}
</urlset>`;

  return new NextResponse(xml, {
    headers: {
      'Content-Type': 'application/xml',
    },
  });
}
