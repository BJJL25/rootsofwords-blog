from pathlib import Path

# Path to your post template file (blog/[slug]/page.tsx)
target_file = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog\src\app\blog\[slug]\page.tsx")

# Read the original code
code = target_file.read_text(encoding='utf-8')

# Check if ad already added
if 'adsbygoogle' in code:
    print("⚠️  AdSense ad component already present. Skipping.")
else:
    updated_code = code.replace(
        "</article>",
        """
        <div style={{ marginTop: '2rem', marginBottom: '2rem' }}>
          <ins className="adsbygoogle"
               style={{ display: 'block', textAlign: 'center' }}
               data-ad-client="ca-pub-5321928375168935"
               data-ad-slot="1234567890"
               data-ad-format="auto"
               data-full-width-responsive="true"></ins>
          <script>
            (adsbygoogle = window.adsbygoogle || []).push({});
          </script>
        </div>
      </article>"""
    )

    target_file.write_text(updated_code, encoding='utf-8')
    print("✅ AdSense ad unit injected into blog post layout.")
