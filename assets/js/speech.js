document.addEventListener('DOMContentLoaded', function () {
    const inputElement = document.getElementById('user-message');
    const startButton = document.getElementById('start-mic');

    // Check if the browser supports the SpeechRecognition API
    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();

        recognition.continuous = true;

        recognition.onstart = function () {
            console.log('Speech recognition started');
        };

        recognition.onresult = function (event) {
            const transcript = event.results[event.results.length - 1][0].transcript;
            updateTextInput(transcript);
        };

        recognition.onerror = function (event) {
            console.error('Speech recognition error:', event.error);
        };

        recognition.onend = function () {
            console.log('Speech recognition ended');
        };

        startButton.addEventListener('click', function () {
            recognition.start();
            startButton.disabled = true;
        });

        function updateTextInput(message) {
            inputElement.value = message;
        }
    } else {
        console.error('Speech recognition not supported in this browser.');
        startButton.disabled = true;
    }
});