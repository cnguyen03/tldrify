import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

function Button({ onClick, link }) {
    const [content, setContent] = useState("");
    const [buttonClicked, setButtonClicked] = useState(false);

    useEffect(() => {
        if (buttonClicked) {
            setContent("Loading summary for " + link);
            console.log(content);
            fetch("http://localhost:8080/api/home",
                {
                    method: 'POST',
                    headers: {
                        "Content-Type":
                            "application/json"
                    },
                    body: JSON.stringify({ link: link })
                })
                .then((response) => response.json())
                .then((data) => {
                    setContent(data.message);
                });
            setButtonClicked(false);
        }
    }, [buttonClicked, content]);
    return (
        <div>
            <button onClick={() => { onClick(); setButtonClicked(true); }}>Generate Summary!</button>
            <div class="content">
                {content}
            </div>
        </div>
    );
}
Button.propTypes = {
    onClick: PropTypes.func.isRequiried,
};

export default Button;