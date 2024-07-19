'use client';
import React, {useEffect, useState} from "react";
import MarkdownPreview from '@uiw/react-markdown-preview';

interface MarkdownProps {
    url: string
}

const Markdown: React.FC<MarkdownProps> = ({url}) => {
    const [onLoading, setOnLoading] = useState<boolean>(true)
    const [markdown, setMarkdown] = useState<string>('')

    useEffect(() => {
        fetch(url)
            .then(res => {
                setOnLoading(false)
                return res.text()
            })
            .then(text => setMarkdown(text))
    })


    return <>
        {
            onLoading ? <div>Loading...</div> : <MarkdownPreview source={markdown}/>
        }
    </>

}

export default Markdown;