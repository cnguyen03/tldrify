import React, { useState } from 'react';

function Menu() {
    return (
        <div className="menu">
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
        // sets link to input and clears input
        if (link !== inputValue) {
            setLink(inputValue);
            setInputValue("");
            document.getElementById("textbox").setAttribute("placeholder", "Insert link here...");
        }
    }
    // console.log(link);

    return (
        <div className="textbox">
            <input
                type="text"
                id="textbox"
                placeholder="Insert link here..."
                value={inputValue}
                onChange={handleInputChange}
            />
            <div className="button">
                <button onClick={handleSubmit}>Generate Summary!</button>
            </div>
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
