import { useState } from 'react'
import './App.css'
import Main from './components/Main'
import AltMain from './components/Alternate'

function App() {
  const [count, setCount] = useState(0) // useState is like session for 1 page

  

  return (
    <>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
      <Main />
      {/* <AltMain /> */}
    </>
  )
}

export default App
