'use client';

import Markdown from "@/components/markdown";

const USER_DOC = 'https://raw.githubusercontent.com/AppleBoiy/3Stack-NFP/main/docs/user.md'

export default function User() {
    return <div>
        <Markdown url={USER_DOC}/>
    </div>
}
