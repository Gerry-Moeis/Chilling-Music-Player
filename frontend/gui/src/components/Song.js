import React, { useEffect, useState } from "react"

export default function Song() {
    const [songs, setSongs] = useState()

    useEffect(() => {
        const url = "http://127.0.0.1:8000/api/"

        fetch(url).then(
            response => response.json()
        ).then(
            data => {
                setSongs(data)
            }
        )
    }, [])

    return (
        <div>
            {songs ? songs.map((song) => {
                return (
                    <h1>Title: {song.title}</h1>
                )
            }) : ""}
        </div>
    )
}