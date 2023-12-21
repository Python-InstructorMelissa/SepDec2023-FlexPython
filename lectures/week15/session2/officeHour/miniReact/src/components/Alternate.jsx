import React from 'react'


function AltMain() {
    const arr = [1,2,3,4,5,6,]


    return (
        <>
        {arr.map((greeting, index) => (
        // Each greeting is like a message to display
        <h3 key={index}>{greeting}</h3>
      ))}
        </>
    )
}

export default AltMain