import "./globals.css";
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
      <head>
        <link
          rel="alternate"
          type="application/rss+xml"
          title="RSS Feed for Roots of Words"
          href="/rss"
        />
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      </head>
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
