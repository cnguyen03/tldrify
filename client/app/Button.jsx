import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

function Button({ onClick, link }) {
    const [content, setContent] = useState("");
    const [buttonClicked, setButtonClicked] = useState(false);

    useEffect(() => {
        if (buttonClicked) {
            setContent("Loading summary for " + link);
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
                    // setContent(data.message);
                    // console.log(data.message);
                    const message = data.message
                    let index = 0;
                    const interval = setInterval(() => {
                        setContent(message.substring(0, index));
                        index++;
                        if (index > message.length) {
                            clearInterval(interval);
                        }
                    }, 15);
                });
            setButtonClicked(false);
        }
    }, [buttonClicked, content]);
    return (
        <div>
            <button class="bg-slate-700 text-white px-4 py-2 rounded-xl transition duration-300 ease-in-out transform hover:scale-110 hover:bg-slate-600" onClick={() => { onClick(); setButtonClicked(true); }}>Generate Summary!</button>
            <div class="ml-40 mr-40 mt-5 text-white">
                {content}
            </div>
        </div>
    );
}
Button.propTypes = {
    onClick: PropTypes.func.isRequiried,
};

export default Button;