// playing the alarm-sounds if someone selects any sound from the list of sounds given.
function playsound(audio_list_id) {
  let audioList = document.getElementById(audio_list_id);
  let audioPlayer = document.getElementById("player");
  let audioSource = document.getElementById("sound-source");
  let selectedTune = audioList.value;
  if (selectedTune != "none") {
    audioSource.src = selectedTune;
    audioPlayer.load();
    audioPlayer.play();
    // stop the sound after 5seconds
    setTimeout(() => {
      audioPlayer.pause();
    }, 5000);
  } else {
    audioPlayer.pause();
  }
}
