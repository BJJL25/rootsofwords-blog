from pathlib import Path

project_root = Path(r"C:\Users\benle\OneDrive\Desktop\MOAM Files\rootsofwords-blog")
app_dir = project_root / "src" / "app"
components_dir = project_root / "src" / "components"
layout_file = app_dir / "layout.tsx"
globals_css = app_dir / "globals.css"

components_dir.mkdir(parents=True, exist_ok=True)
globals_css.parent.mkdir(parents=True, exist_ok=True)

layout_tsx = """import "./globals.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import type { ReactNode } from "react";

export const metadata = {
  title: "Roots of Words",
  description: "Uncover the surprising histories behind everyday English words",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="flex flex-col min-h-screen bg-gray-50 text-gray-900">
        <Navbar />
        <main className="flex-grow container mx-auto px-4 py-6">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
"""
navbar_tsx = """export default function Navbar() {
  return (
    <nav className="w-full bg-white shadow-md px-6 py-4 flex justify-between items-center">
      <div className="text-xl font-bold">Roots of Words</div>
      <ul className="flex gap-4 text-sm">
        <li><a href="/" className="hover:underline">Home</a></li>
        <li><a href="/blog" className="hover:underline">Blog</a></li>
        <li><a href="/about" className="hover:underline">About</a></li>
        <li><a href="/privacy-policy" className="hover:underline">Privacy</a></li>
        <li><a href="/terms-of-use" className="hover:underline">Terms</a></li>
      </ul>
    </nav>
  );
}
"""
footer_tsx = """export default function Footer() {
  return (
    <footer className="text-center text-xs text-gray-600 py-4 mt-12 border-t">
      © {new Date().getFullYear()} Roots of Words. All rights reserved.
    </footer>
  );
}
"""

layout_file.write_text(layout_tsx)
(components_dir / "Navbar.tsx").write_text(navbar_tsx)
(components_dir / "Footer.tsx").write_text(footer_tsx)

globals_css.write_text("@tailwind base;\n@tailwind components;\n@tailwind utilities;\n")

print("✅ Global layout, Navbar, Footer, and Tailwind globals applied.")
