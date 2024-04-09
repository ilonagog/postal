import React, { useEffect, useState } from "react";

const Countries = () => {
  const [countries, setCountries] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5000/countries")
      .then((resp) => resp.json())
      .then((data) => console.log(data));
  }, []);
  console.log(countries);
  //   const countryList=countries.map((country)=>{
  //       <key={country.id}/>
  //   })
  return (
    <div>
      <h1>Hi</h1>
      {/* <ul>{countryList}</ul> */}
    </div>
  );
};

export default Countries;
