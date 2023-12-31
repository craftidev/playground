import Link from "next/link";
import './globals.css';

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="en">
        <body>
            <main>
                <nav>
                    <Link href="/">Home</Link>
                    <Link href="/contacts">Contacts</Link>
                </nav>

                {children}
            </main>
        </body>
        </html>
    );
}
