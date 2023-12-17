import React, { useState } from 'react';

function Menu() {
    return (
        <div>
            <h1>TLDRify</h1>
        </div>
    );
}

function TextBox() {
    const [inputValue, setInputValue] = useState("");
    const [link, setLink] = useState("");

    const handleInputChange = (event) => {
        const value = event.target.value;
        setInputValue(value);

        // remove placeholder text when text is inputted
        // add placeholer text when text is empty
        if (value !== "") {
            event.target.removeAttribute("placeholder");
        } else {
            event.target.setAttribute("placeholder", "Insert link here...");
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (link !== inputValue) {
            setLink(inputValue);
            setInputValue("Insert link here...");
        }
    }
    console.log(link);

    return (
        <div>
            <input
                type="text"
                id="textbox"
                placeholder="Insert link here..."
                value={inputValue}
                onChange={handleInputChange}
            />
            <button onClick={handleSubmit}>Generate Summary!</button>
        </div>
    );
}

function Home(props) {
    return (
        <div>
            <Menu></Menu>
            <TextBox></TextBox>
        </div>
    )
}
export default Home;
