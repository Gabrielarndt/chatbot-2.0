document.addEventListener("DOMContentLoaded", function() {
    const chatLog = document.getElementById("chat-log");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");

    function appendMessage(sender, message) {
        const messageContainer = document.createElement("div");
        messageContainer.classList.add("message-container");

        const senderElement = document.createElement("span");
        senderElement.classList.add("sender");
        senderElement.textContent = sender;

        const messageElement = document.createElement("span");
        messageElement.classList.add("message");
        messageElement.textContent = message;

        messageContainer.appendChild(senderElement);
        messageContainer.appendChild(messageElement);
        chatLog.appendChild(messageContainer);
    }

    function sendMessage() {
        const userMessage = userInput.value;
        appendMessage("Você: ", userMessage);

        const url = "http://localhost:5000/api/chat"; // Atualize a URL para o endpoint do seu backend Flask

        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: userMessage
            })
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = data.message;
            appendMessage("Chat Bot: ", botMessage);
        })
        .catch(error => {
            console.error("Ocorreu um erro", error);
        });

        userInput.value = "";
    }
    
    const botMessage = " Olá! Sou um chat bot engraçado.";
    setTimeout(function() {
        appendMessage("Chat Bot", botMessage);
    }, 500);

    sendBtn.addEventListener("click", sendMessage);

    userInput.value = "";

    userInput.addEventListener("keydown", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            sendMessage();
        }
    });
});
