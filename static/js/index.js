
script>
// Function to toggle play/pause for each audio
function togglePlayPause(button, audioUrl) {
    var audio = button.nextElementSibling;
    if (audio.paused) {
        audio.src = audioUrl;
        audio.play();
         button.innerHTML = '<i class="fas fa-pause"></i>';
    } else {
        audio.pause();
        button.innerHTML = '<i class="fas fa-play"></i>';
    }
}

// Function to increase the volume of the audio with specific ID
function increaseVolume(id) {
    var player = document.getElementById('player_' + id);
    if (player.volume < 1) {
        player.volume += 0.1;
    }
}

// Function to decrease the volume of the audio with specific ID
function decreaseVolume(id) {
    var player = document.getElementById('player_' + id);
    if (player.volume > 0) {
        player.volume -= 0.1;
    }
}




