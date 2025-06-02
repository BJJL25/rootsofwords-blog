from pathlib import Path

home_file = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog\src\app\page.tsx")

content = home_file.read_text(encoding='utf-8')

if 'adsbygoogle' in content:
    print("⚠️  AdSense ad already injected in homepage.")
else:
    updated_content = content.replace(
        "</main>",
        """
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
      </main>"""
    )

    home_file.write_text(updated_content, encoding='utf-8')
    print("✅ AdSense banner added to homepage.")
