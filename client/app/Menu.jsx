import TextBox from './TextBoxAndButton.jsx';
import 'tailwindcss/tailwind.css';

function Menu() {
    return (
        <div className="menu">
            {/* <h1 className="text-8xl mb-3 mt-20 text-white" style={{ fontFamily: 'Gotham, sans-serif' }}>TLDRify</h1> */}
            <img src="https://see.fontimg.com/api/renderfont4/mnOV/eyJyIjoiZnMiLCJoIjoxNTgsInciOjIwMDAsImZzIjo3OSwiZmdjIjoiI0RCREJEQiIsImJnYyI6IiMxMjEyMTIiLCJ0IjoxfQ/VExEUmlmeQ/moiser.png" alt="Space fonts" className="mx-auto mt-20" />
            <TextBox></TextBox>
        </div>
    );
}
export default Menu;