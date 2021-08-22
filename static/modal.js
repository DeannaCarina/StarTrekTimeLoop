var modal = document.getElementById("myModal");
var musicModal = document.getElementById("myMusicModal");
var btn = document.getElementById("myBtn");
var musicBtn = document.getElementById("myMusicBtn");
var span = document.getElementsByClassName("close")[0];
var musicSpan = document.getElementsByClassName("musicClose")[0];

// When the user clicks the button, open the modal 
btn.onclick = function () {
    modal.style.display = "block";
}

musicBtn.onclick = function () {
    musicModal.style.display = "block";
}

// When the user clicks on cross button, close the modal
span.onclick = function () {
    modal.style.display = "none";
}
musicSpan.onclick = function () {
    musicModal.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

window.onclick = function (event) {
    if (event.target == musicModal) {
        musicModal.style.display = "none";
    }
}