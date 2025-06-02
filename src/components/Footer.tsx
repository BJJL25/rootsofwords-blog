export default function Footer() {
  return (
    <footer className="bg-gray-100 text-center py-4 border-t mt-8">
      <p className="text-sm text-gray-600">
        &copy; {new Date().getFullYear()} Making of a Millionaire Inc. All rights reserved.
      </p>
      <p className="mt-2">
        <a
          href="/rss"
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-600 hover:underline"
        >
          📡 RSS Feed
        </a>
      </p>
    </footer>
  );
}
