import React, { useEffect } from "react";
const ErrorPage = () => {
    useEffect(() => {
        const timeout = setTimeout(() => {
            document.body.className = "oppenheimer-mode";
            const audio = new Audio("/gg.mp3");
            document.body.addEventListener("click", () => {
                if (document.body.className === "oppenheimer-mode") {
                    audio.play();
                    document.body.addEventListener("click", () => {
                        audio.pause();
                    });
                }
            });
        }, 1000);
        return () => {
            clearTimeout(timeout);
        };
    }, []);
    return (
        <div>
            <h1>Error Page</h1>
            <h3>We are working on this page! (or not...)</h3>
            <h3>See ya later! (or not...)</h3>
        </div>
    );
};

export default ErrorPage;