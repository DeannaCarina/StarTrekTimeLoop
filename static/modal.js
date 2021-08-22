var modal = document.getElementById("myModal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on cross button, close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// YouTube video ID
var videoID = "w1Cvyrvxlbk";

// Fetch video info (using a proxy to avoid CORS errors)
fetch('https://cors-anywhere.herokuapp.com/' + "https://www.youtube.com/get_video_info?video_id=" + videoID).then(response => {
    if (response.ok) {
        response.text().then(ytData => {

            // parse response to find audio info
            var ytData = parse_str(ytData);
            var getAdaptiveFormats = JSON.parse(ytData.player_response).streamingData.adaptiveFormats;
            var findAudioInfo = getAdaptiveFormats.findIndex(obj => obj.audioQuality);

            // get the URL for the audio file
            var audioURL = getAdaptiveFormats[findAudioInfo].url;

            // update the <audio> element src
            var youtubeAudio = document.getElementById('youtube');
            youtubeAudio.src = audioURL;

        });
    }
});

function parse_str(str) {
    return str.split('&').reduce(function (params, param) {
        var paramSplit = param.split('=').map(function (value) {
            return decodeURIComponent(value.replace('+', ' '));
        });
        params[paramSplit[0]] = paramSplit[1];
        return params;
    }, {});
}