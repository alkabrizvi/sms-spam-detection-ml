async function checkSpam() {

    const messageBox = document.getElementById("message");
    const resultBox = document.getElementById("result");
    const button = document.querySelector("button");

    const message = messageBox.value.trim();

    if (!message) {
        alert("Please enter a message!");
        return;
    }

    button.disabled = true;
    button.innerText = "Analyzing...";
    resultBox.style.display = "block";
    resultBox.className = "";
    resultBox.innerText = "Checking your message...";

    try {

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();

        if (data.prediction === "Spam") {
            resultBox.className = "spam";
            resultBox.innerText = "⚠️ SPAM MESSAGE DETECTED";
        } else {
            resultBox.className = "ham";
            resultBox.innerText = "✓ SAFE MESSAGE (HAM)";
        }

    } catch (error) {

        resultBox.className = "";
        resultBox.innerText = "Server connection failed!";

    } finally {

        button.disabled = false;
        button.innerText = "Check Message";

    }
}