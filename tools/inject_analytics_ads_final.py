from pathlib import Path

layout_file = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog\src\app\layout.tsx")

layout_code = layout_file.read_text(encoding='utf-8')

# Check if already injected
if 'Google Analytics' in layout_code or 'adsbygoogle' in layout_code:
    print("⚠️  Google Analytics or AdSense already present. Skipping injection.")
else:
    new_layout_code = layout_code.replace(
        "</head>",
        """
      <!-- Google Analytics -->
      <script async src="https://www.googletagmanager.com/gtag/js?id=G-QV60M0B2J3"></script>
      <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'G-QV60M0B2J3');
      </script>

      <!-- Google AdSense -->
      <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=pub-5321928375168935"
        crossorigin="anonymous"></script>
    </head>"""
    )

    layout_file.write_text(new_layout_code, encoding='utf-8')
    print("✅ Google Analytics and AdSense have been injected into layout.tsx.")
