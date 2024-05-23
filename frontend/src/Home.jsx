import React from 'react'
import './Home.css'
import { Link } from 'react-scroll'
const Home = () => {
  return (
    <div className="container">
       <h1>Music Genre Predictor</h1>
       <p>Have you ever wondered what genre your song belongs to? Enter your lyrics or upload the audio, and let our tool do the magic!</p>
       <p>With stunning accuracy, our Machine Learning models are trained to make reliable predictions.</p>
       
        <div className="button_container">
        <Link to="Lyrics" smooth={true} duration={1000}>
       <button class="button-64" role="button"><span class="text">Use Lyrics</span></button>
       </Link>
        <Link to="Upload" smooth={true} duration={1000}>
       <button class="button-64" role="button"><span class="text">Use Audio</span></button>
        </Link>
       </div>
         
    </div>
  )
}

export default Home