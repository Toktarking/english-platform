const uiSounds = {
    click: new Audio(
        "/static/vocabulary/sounds/click.mp3"
    ),

    correct: new Audio(
        "/static/vocabulary/sounds/correct.mp3"
    ),

    wrong: new Audio(
        "/static/vocabulary/sounds/wrong.mp3"
    ),

    complete: new Audio(
        "/static/vocabulary/sounds/complete.mp3"
    ),

    victory: new Audio(
        "/static/vocabulary/sounds/victory.mp3"
    ),

    letterAdd: new Audio(
        "/static/vocabulary/sounds/letter_add.mp3"
    ),

    letterRemove: new Audio(
        "/static/vocabulary/sounds/letter_remove.mp3"
    ),


};


uiSounds.click.volume = 0.25;
uiSounds.correct.volume = 0.35;
uiSounds.wrong.volume = 0.30;
uiSounds.complete.volume = 0.40;
uiSounds.victory.volume = 0.45;
uiSounds.letterAdd.volume = 0.25;
uiSounds.letterRemove.volume = 0.20;


function playSound(name) {

    const sound =
        uiSounds[name];

    if (!sound) {
        return;
    }

    sound.currentTime = 0;

    sound
        .play()
        .catch(() => {});
}