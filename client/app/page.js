"use client";

import React from 'react';
import Menu from './Menu.jsx';


function page() {
  // useEffect(() => {
  //   fetch("http://localhost:8080/api/home")
  //     .then((response) => response.json())
  //     .then((data) => {
  //       // message = 'Loading'
  //       // once data is retrieved
  //       // message = 'data.message'
  //       setMessage(data.message);
  //       setPeople(data.people);
  //     });
  // }, []);

  return (
    <div>
      <Menu></Menu>
    </div>
  )
}

export default page;