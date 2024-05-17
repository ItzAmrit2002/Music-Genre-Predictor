import { useState } from 'react';
import './App.css';
import axios from 'axios'
import Navbar from './Navbar';
import Home from './Home';
import Lyrics from './Lyrics';
function App() {
  const [inputText, setInputText] = useState('');
  const [resultMessage, setResultMessage] = useState('');
  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleButtonClick = async () => {
    try {
      // Format the input text as JSON
    const formattedText = inputText
    .replace(/\n/g, '. ') // Replace newlines with full stops
    .replace(/"/g, "'");   // Replace double quotes with single quotes
      // Make a POST request to localhost:8000 with the inputText
      const response = await axios.post('https://mlbackend-2kql.onrender.com', { lyrics: formattedText });
      console.log(response.data)

      // Extract the result message from the response
      

      // Update the state with the result message
      setResultMessage(response.data);
    } catch (error) {
      console.error('Error posting data:', error);

      // Update the state with an error message
      setResultMessage('Error posting data. Please try again.');
    }
  };

  return (
    <div>
      {/* <Navbar/>
    
    <div className='container'>
      <div className='box'>
        <h1>Enter your song lyrics: </h1>
      <textarea
        value={inputText}
        onChange={handleInputChange}
        placeholder="Enter lyrics here"
      />
      <button onClick={handleButtonClick}>Predict Genre</button>
      <h2>The predicted Genre is: {resultMessage? resultMessage.toUpperCase()+" MUSIC" : "Provide your lyrics to check"} </h2>
      </div>
      
    </div> */}
    <Home/>
    <Lyrics/>
    </div>
  );
}

export default App;
