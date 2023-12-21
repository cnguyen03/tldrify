import React, { useEffect, useState } from 'react';
import Button from './Button.jsx';

function TextBox() {
    const [inputValue, setInputValue] = useState("");
    const [link, setLink] = useState("");


    const handleInputChange = (event) => {
        const value = event.target.value;
        // set input value as the given input
        setInputValue(value);
        // remove placeholder text when text is inputted
        // add placeholer text when text is empty
        if (value !== "") {
            event.target.removeAttribute("placeholder");
        } else {
            event.target.setAttribute("placeholder", "Insert link here...");
        }
    };

    const handleSubmit = () => {
        // set the link value as the given input
        setLink(inputValue);
        // reset input value
        setInputValue("");
        document.getElementById("textbox").setAttribute("placeholder", "Insert link here...");
    }
    // console.log(link);

    return (
        <div className="textbox">
            <input className="text-white mt-12 mb-5 w-80 p-3 rounded-xl bg-slate-700"
                type="text"
                id="textbox"
                placeholder="Insert link here..."
                value={inputValue}
                onChange={handleInputChange}

            />
            <div className="button">
                {/* send prop and link to Button module */}
                <Button onClick={handleSubmit} link={link}></Button>
            </div>
        </div>
    );
}
export default TextBox;