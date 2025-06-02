export default function Navbar() {
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
