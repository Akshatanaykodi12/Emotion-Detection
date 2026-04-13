const video = document.getElementById('video');
const captureBtn = document.getElementById('captureBtn');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

const emotionText = document.getElementById('emotion');
const scoresText = document.getElementById('scores');
const quoteText = document.getElementById('quote');
const suggestionText = document.getElementById('suggestion');
const videoList = document.getElementById('videoList');
const musicList = document.getElementById('musicList');
const exerciseText = document.getElementById('exercise');
const extraText = document.getElementById('extra');
const capturedImage = document.getElementById('capturedImage');

const textInput = document.getElementById('textInput');
const analyzeTextBtn = document.getElementById('analyzeTextBtn');

const startRecordBtn = document.getElementById('startRecordBtn');
const stopRecordBtn = document.getElementById('stopRecordBtn');
const audioStatus = document.getElementById('audioStatus');

// ---------------- START WEBCAM ----------------
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(error => {
        console.error("Webcam access error:", error);
        alert("Unable to access webcam. Please allow camera permission.");
    });


// ---------------- COMMON RESULT DISPLAY FUNCTION ----------------
function displayResults(data) {
    emotionText.innerText = data.emotion || "neutral";

    // Emotion scores
    if (data.scores && Object.keys(data.scores).length > 0) {
        let formattedScores = "";
        for (let key in data.scores) {
            formattedScores += `${key}: ${Number(data.scores[key]).toFixed(2)}%\n`;
        }
        scoresText.innerText = formattedScores;
    } else {
        scoresText.innerText = "Not available for this input type.";
    }

    quoteText.innerText = data.quote || "No quote available.";
    suggestionText.innerText = data.suggestion || "No suggestion available.";
    exerciseText.innerText = data.exercise || "No exercise available.";
    extraText.innerText = data.extra || "No extra tip available.";
    loadHistory();
    // Videos
    let videosHTML = "";
    if (data.videos && data.videos.length > 0) {
        data.videos.forEach((link, index) => {
            videosHTML += `<p><a href="${link}" target="_blank">🎥 Video ${index + 1}</a></p>`;
        });
    } else {
        videosHTML = "<p>No videos available.</p>";
    }
    videoList.innerHTML = videosHTML;

    // Music
    let musicHTML = "";
    if (data.music && data.music.length > 0) {
        data.music.forEach((link, index) => {
            musicHTML += `<p><a href="${link}" target="_blank">🎵 Music ${index + 1}</a></p>`;
        });
    } else {
        musicHTML = "<p>No music available.</p>";
    }
    musicList.innerHTML = musicHTML;
}


// ---------------- FACE EMOTION ----------------
captureBtn.addEventListener('click', () => {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageData = canvas.toDataURL('image/jpeg');
    capturedImage.src = imageData;

    fetch('/detect_emotion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData })
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => {
        console.error("Face emotion error:", error);
        alert("Error detecting face emotion.");
    });
});


// ---------------- TEXT SENTIMENT ----------------
analyzeTextBtn.addEventListener('click', () => {
    const text = textInput.value.trim();

    if (!text) {
        alert("Please type some text first.");
        return;
    }

    fetch('/analyze_text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        capturedImage.src = "";
        displayResults(data);
        scoresText.innerText = "Not available for text input.";
    })
    .catch(error => {
        console.error("Text sentiment error:", error);
        alert("Error analyzing text.");
    });
});


// ---------------- AUDIO SENTIMENT ----------------
let mediaRecorder;
let audioChunks = [];

startRecordBtn.addEventListener('click', async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = event => {
            if (event.data.size > 0) {
                audioChunks.push(event.data);
            }
        };

        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            const formData = new FormData();
            formData.append('audio', audioBlob, 'recording.webm');

            audioStatus.innerText = "Analyzing audio...";

            fetch('/analyze_audio', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                capturedImage.src = "";
                displayResults(data);
                scoresText.innerText = "Not available for audio input.";
                audioStatus.innerText = "Recognized Text: " + (data.transcribed_text || "No speech detected");
            })
            .catch(error => {
                console.error("Audio sentiment error:", error);
                audioStatus.innerText = "Error analyzing audio.";
            });
        };

        mediaRecorder.start();
        audioStatus.innerText = "Recording...";
        startRecordBtn.disabled = true;
        stopRecordBtn.disabled = false;

    } catch (error) {
        console.error("Microphone access error:", error);
        alert("Unable to access microphone. Please allow microphone permission.");
    }
});

stopRecordBtn.addEventListener('click', () => {
    if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stop();
        audioStatus.innerText = "Processing...";
        startRecordBtn.disabled = false;
        stopRecordBtn.disabled = true;
    }
});

// ------------------------------
// Emotion History + Analytics
// ------------------------------

async function loadHistory() {
    try {
        const response = await fetch('/get_history');
        const data = await response.json();

        const historyList = document.getElementById('historyTableBody');
        const analyticsBox = document.getElementById('analyticsBox');

        if (!historyList || !analyticsBox) return;

        if (data.history.length === 0) {
            historyTableBody.innerHTML = `
                <tr>
                    <td colspan="3">No history yet...</td>
                </tr>
            `;
        } else {
            historyTableBody.innerHTML = data.history.map(item => `
                <tr>
                    <td>${item.emotion}</td>
                    <td>${item.input_type}</td>
                    <td>${item.timestamp}</td>
                </tr>
            `).join('');
        }
        // Analytics
        analyticsBox.innerHTML = `
            <p>😊 Happy: ${data.analytics.happy}</p>
            <p>😢 Sad: ${data.analytics.sad}</p>
            <p>😠 Angry: ${data.analytics.angry}</p>
            <p>😨 Fear: ${data.analytics.fear}</p>
            <p>😲 Surprise: ${data.analytics.surprise}</p>
            <p>😐 Neutral: ${data.analytics.neutral}</p>
            <p>🤢 Disgust: ${data.analytics.disgust}</p>
        `;
    } catch (error) {
        console.error("Error loading history:", error);
    }
}

// Load history when page opens
window.addEventListener('load', loadHistory);

// ------------------------------
// Clear History Button
// ------------------------------

const clearHistoryBtn = document.getElementById('clearHistoryBtn');

if (clearHistoryBtn) {
    clearHistoryBtn.addEventListener('click', async () => {
        const confirmClear = confirm("Are you sure you want to clear all emotion history?");
        
        if (!confirmClear) return;

        try {
            const response = await fetch('/clear_history', {
                method: 'POST'
            });

            const data = await response.json();

            alert(data.message);
            loadHistory(); // Refresh history and analytics
        } catch (error) {
            console.error("Error clearing history:", error);
            alert("Failed to clear history.");
        }
    });
}

// ------------------------------
// Toggle Emotion History
// ------------------------------

const toggleHistoryBtn = document.getElementById('toggleHistoryBtn');
const historyContainer = document.getElementById('historyContainer');

if (toggleHistoryBtn && historyContainer) {
    toggleHistoryBtn.addEventListener('click', () => {
        if (historyContainer.style.display === 'none') {
            historyContainer.style.display = 'block';
            toggleHistoryBtn.innerText = '📁 Hide Emotion History';
        } else {
            historyContainer.style.display = 'none';
            toggleHistoryBtn.innerText = '📂 Show Emotion History';
        }
    });
}