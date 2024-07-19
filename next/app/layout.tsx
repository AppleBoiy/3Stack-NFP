import {Inter} from "next/font/google";
import "./globals.css";
import PageHeader from "./header";

const inter = Inter({subsets: ["latin"]});

export default function RootLayout({
                                       children,
                                   }: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
        <body className={inter.className}>
        <header>
            <PageHeader/>
        </header>

        <div className="content-area">
            {children}
        </div>
        </body>
        </html>
    );
}