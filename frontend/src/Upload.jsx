import React, { useState } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './Upload.css';
function FileUpload() {
    const [file, setFile] = useState(null);

    const submitFile = () => {
        try {
            const formData = new FormData();
            formData.append('file', file);
    
            toast.promise(
                axios.post('https://mlbackend-2kql.onrender.com/uploadfile', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }),
                {
                    pending: 'Uploading file',
                    success: {
                        render({data}){
                            console.log(data.data)
                        return "The predicted Genre is: " + data.data['Predicted label'].toUpperCase();
                        },
                        // other options
                        
                      },
                    error: 'Upload failed'
                },
                
            );
        } catch (error) {
            console.error("Error uploading file: ", error);
        }
    };

    return (
        <div className='upload_container'>
            

            <ToastContainer
            position="bottom-center"
            theme="dark"
            closeOnClick={true}
            hideProgressBar={true}
            transition="Zoom"
            autoClose={3500}
            />
            <h2 id='Upload'>Upload your own music and predict the genre</h2>
            <div className="upload_box">
            <input className='input_audio' type="file" onChange={event => setFile(event.target.files[0])} />
            <button className='button-63' onClick={submitFile}>Predict Genre</button>
            </div>
        </div>
    );
}

export default FileUpload;