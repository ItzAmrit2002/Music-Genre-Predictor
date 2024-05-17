import React, {useState} from "react";
import "./Lyrics.css";
import axios from "axios";
import { ToastContainer, toast } from 'react-toastify';

  import 'react-toastify/dist/ReactToastify.css';
const Lyrics = () => {
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
        //   const response = await axios.post('https://mlbackend-2kql.onrender.com', { lyrics: formattedText });
        //   console.log(response.data)
    
          // Extract the result message from the response
          console.log("clicked")
          toast.promise(axios.post("https://mlbackend-2kql.onrender.com", {
          lyrics: formattedText
        }), {
          pending: "Predicting Genre",
          success: {
            render({data}){
                
            return "The predicted Genre is: " + data.data.toUpperCase();
            },
            // other options
            autoClose: 5500
          },
          error: {
            render({data}){
              console.log(data)
              return `${data.response.data.message}`
            },
            // other options
            autoClose: 1500
          },
          autoClose: 1000, // Close success toasts after 1500ms
        });
    
          // Update the state with the result message
        //   setResultMessage(response.data);
        } catch (error) {
          console.error('Error posting data:', error);
    
          // Update the state with an error message
          setResultMessage('Error posting data. Please try again.');
        }
      };

	return (
		<div className="lyrics_container">
            <ToastContainer
            position="bottom-center"
            theme="dark"
            closeOnClick={true}
            hideProgressBar={true}
            transition="Zoom"
            />
			<h2 id="Lyrics">Enter your lyrics in the below box:</h2>
			<div class="textarea-wrapper">
				<textarea placeholder="Enter your Lyrics"></textarea>
			</div>
			<button class="button_65" role="button" onClick={handleButtonClick}><span class="text">Predict Genre</span></button>
    
		</div>
	);
};

export default Lyrics;
