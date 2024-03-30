// Initialize variable to keep track of currently playing audio
var currentAudio = null;

// Function to toggle play/pause for a specific audio element
// Modify the togglePlayPause() function to accept parameters for the button and audio URL
function togglePlayPause(button, audioUrl) {
    // Get the audio element associated with the button
    var audioElement = button.parentElement.querySelector('audio');

    // Check if the audio element is currently playing
    if (audioElement.paused) {
        // Set the audio source to the provided URL
        audioElement.src = audioUrl;
        // Play the audio
        audioElement.play();
    } else {
        // Pause the audio
        audioElement.pause();
    }
}

// Event listener for updating progress bar and time info
document.addEventListener('timeupdate', function() {
    // Get all audio elements on the page
    var audioElements = document.querySelectorAll('audio');

    // Iterate over each audio element
    audioElements.forEach(function(audioElement) {
        // Update progress bar and time info for the audio element
        updateProgressBar(audioElement);
    });
});

// Helper function to update progress bar and time info for an audio element
function updateProgressBar(audioElement) {
    // Get progress bar and time info elements associated with the audio element
    var progressBarFill = audioElement.parentElement.querySelector('.progress-bar-fill');
    var currentTimeElement = audioElement.parentElement.querySelector('.current-time');
    var totalDurationElement = audioElement.parentElement.querySelector('.total-duration');

    // Check if audio duration is available
    if (!isNaN(audioElement.duration)) {
        // Calculate progress percentage
        var progress = (audioElement.currentTime / audioElement.duration) * 100;

        // Update progress bar width
        progressBarFill.style.width = progress + '%';

        // Update current time
        currentTimeElement.textContent = formatTime(audioElement.currentTime);

        // Update total duration
        totalDurationElement.textContent = formatTime(audioElement.duration);
    }
}

// Helper function to format time in mm:ss format
function formatTime(seconds) {
    var minutes = Math.floor(seconds / 60);
    var remainingSeconds = Math.floor(seconds % 60);
    return minutes + ':' + (remainingSeconds < 10 ? '0' : '') + remainingSeconds;
}
