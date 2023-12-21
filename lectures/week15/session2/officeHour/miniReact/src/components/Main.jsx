import React from 'react'


function Main() {
    const arr = ['hi', 'hello', 'whats up']


    return (
        <>
        {arr.map((greeting, index) => (
        // Each greeting is like a message to display
        <h3 key={index}>{greeting}</h3>
      ))}
        </>
    )
}

export default Main