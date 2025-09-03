document.addEventListener('DOMContentLoaded', () => {


    async function sendData() {
        // 1. Get the data from the form
        const usernameInput = document.getElementById('master-username');
        const passwordInput = document.getElementById('master-password');
        const responseElement = document.getElementById('response'); // Get the element once

        if (!usernameInput || !passwordInput || !responseElement) {
            console.error("A form element was not found in the HTML.");
            return;
        }

        const dataToSend = {
            name: usernameInput.value,
            message: passwordInput.value
        };

        try {
            const response = await fetch('http://127.0.0.1:5999/process-data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataToSend)
            });

            const result = await response.json();

            // Update the webpage with the server's response
            responseElement.textContent = JSON.stringify(result, null, 2);

        } catch (error) {
            console.error('Error:', error);
            responseElement.textContent = 'Error sending data: ' + error;
        }
    }


    const loginButton = document.getElementById('login-button');
    if (loginButton) {
        loginButton.addEventListener('click', sendData);
    } else {
        console.error("Login button not found!");
    }

});