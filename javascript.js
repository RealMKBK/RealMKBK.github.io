var musicPlaying = false;

document.addEventListener('DOMContentLoaded', function() {
  document.addEventListener('click', function() {
    if (!musicPlaying) {
      var audio = new Audio('http://music.163.com/song/media/outer/url?id=1406083061.mp3');
      audio.play();
      musicPlaying = true;

      audio.onended = function() {
        musicPlaying = false;
      };
    }
  });
});