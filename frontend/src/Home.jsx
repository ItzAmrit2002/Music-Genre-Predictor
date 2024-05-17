import React from 'react'
import './Home.css'
import { Link } from 'react-scroll'
const Home = () => {
  return (
    <div className="container">
       <h1>Music Genre Predictor</h1>
       <p>Have you ever wondered what genre your song lyrics belong to? Enter your lyrics and let our tool do the magic!</p>
       <p>With an accuracy of 77.8%, our Machine Learning model is trained to make reliable predictions.</p>
       <Link to="Lyrics" smooth={true} duration={1000}>
       <button class="button-64" role="button"><span class="text">Get Started</span></button>
         </Link>
    </div>
  )
}

export default Home