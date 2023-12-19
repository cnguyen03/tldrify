import React, { useEffect } from 'react';
import PropTypes from 'prop-types';

function Button({ onClick, link }) {
    return (
        <div>
            <button onClick={onClick}>Generate Summary!</button>
            {link.length > 0 &&
                <div class="content">
                    Loading summary for {link}
                </div>
            }
        </div>
    );
}

Button.propTypes = {
    onClick: PropTypes.func.isRequiried,
};

export default Button;