import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="prose prose-lg max-w-none p-6">
      <h1>Welcome to Roots of Words</h1>
      <p>
        Dive into the fascinating etymology and surprising origins of everyday English words.
        Explore the stories behind the language we use — one word at a time.
      </p>
      <p>
        <Link href="/blog">📚 Browse all blog posts</Link>
      </p>
    
        <div style={{ marginTop: '2rem', marginBottom: '2rem' }}>
          <ins className="adsbygoogle"
               style={{ display: 'block', textAlign: 'center' }}
               data-ad-client="ca-pub-5321928375168935"
               data-ad-slot="9876543210"
               data-ad-format="auto"
               data-full-width-responsive="true"></ins>
          <script>
            (adsbygoogle = window.adsbygoogle || []).push({});
          </script>
        </div>
      </main>
  );
}
