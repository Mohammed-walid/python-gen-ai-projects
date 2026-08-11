let savedpasttext = []; // Variable to store the message
let savedpastresponse = []; // Variable to store the message

// Section: get the Id of the talking container
const messagesContainer = document.getElementById('messages-container');
const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');
//

//Section: function to creat the dialogue window
const addMessage = (message, role, imgSrc) => {
  // creat elements in the dialogue window
  const messageElement = document.createElement('div');
  const textElement = document.createElement('p');
  messageElement.className = `message ${role}`;
  const imgElement = document.createElement('img');
  imgElement.src = `${imgSrc}`;
  // append the image and message to the message element
  messageElement.appendChild(imgElement);
  textElement.innerText = message;
  messageElement.appendChild(textElement);
  messagesContainer.appendChild(messageElement);
  // creat the ending of the message
  var clearDiv = document.createElement("div");
  clearDiv.style.clear = "both";
  messagesContainer.appendChild(clearDiv);
};
//


//Section: Calling the model
const sendMessage = async (message) => {
  // FIXED: Changed image path to correctly route through Flask's static folder
  addMessage(message, 'user','/static/user.jpeg');

  // Loading animation
  const loadingElement = document.createElement('div');
  const loadingtextElement = document.createElement('p');
  loadingElement.className = `loading-animation`;
  loadingtextElement.className = `loading-text`;
  loadingtextElement.innerText = 'Loading....Please wait';
  messagesContainer.appendChild(loadingElement);
  messagesContainer.appendChild(loadingtextElement);

  async function makePostRequest(msg) {
    // FIXED: Point to your actual local Flask backend instead of example.com
    const url = 'http://127.0.0.1:5000/chatbot';
    const requestBody = {
      prompt: msg
    };

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      // FIXED: Parse the response as JSON so we can extract the text properly
      const data = await response.json();
      console.log(data);
      return data;
    } catch (error) {
      console.error('Error:', error);
      return { error: true };
    }
  }

  var data = await makePostRequest(message);

  // Deleting the loading animation
  const loadanimation = document.querySelector('.loading-animation');
  const loadtxt = document.querySelector('.loading-text');
  if(loadanimation) loadanimation.remove();
  if(loadtxt) loadtxt.remove();

  if (data.error) {
    const errorMessage = "Could not connect to the server.";
    // FIXED: Corrected error image path
    addMessage(errorMessage, 'error','/static/Error.png');
  } else {
    const responseMessage = data['response'];
    // FIXED: Corrected bot logo image path
    addMessage(responseMessage, 'aibot','/static/Bot_logo.png');
  }
};
//

//Section: Button to submit to the model and get the response
messageForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const message = messageInput.value.trim();
  if (message !== '') {
    messageInput.value = '';
    await sendMessage(message);
  }
});