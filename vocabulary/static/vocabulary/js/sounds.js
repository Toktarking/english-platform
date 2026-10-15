const soundSources = {
    click: "/static/vocabulary/sounds/click.mp3",
    victory: "/static/vocabulary/sounds/victory.mp3",
    correct: "/static/vocabulary/sounds/correct.mp3",
    wrong: "/static/vocabulary/sounds/wrong.mp3",
    letterAdd: "/static/vocabulary/sounds/letter_add.mp3",
    letterRemove: "/static/vocabulary/sounds/letter_remove.mp3",
};


const soundVolumes = {
    click: 0.30,
    victory: 0.45,
    correct: 0.40,
    wrong: 0.35,
    letterAdd: 0.25,
    letterRemove: 0.20,
};


const SOUND_POOL_SIZE = 4;

const soundPools = {};
const soundPoolIndexes = {};


Object.entries(soundSources).forEach(
    ([name, src]) => {

        soundPools[name] = [];

        soundPoolIndexes[name] = 0;


        for (
            let i = 0;
            i < SOUND_POOL_SIZE;
            i++
        ) {

            const audio =
                new Audio(src);


            audio.preload =
                "auto";


            audio.volume =
                soundVolumes[name] ?? 0.3;


            audio.load();


            soundPools[name].push(
                audio
            );

        }

    }
);


window.playSound =
    function (name) {

        const pool =
            soundPools[name];


        if (
            !pool
            ||
            pool.length === 0
        ) {

            return;

        }


        const index =
            soundPoolIndexes[name];


        const audio =
            pool[index];


        soundPoolIndexes[name] =
            (
                index + 1
            )
            %
            pool.length;


        try {

            audio.pause();

            audio.currentTime = 0;


            const playPromise =
                audio.play();


            if (
                playPromise
                &&
                typeof playPromise.catch
                === "function"
            ) {

                playPromise.catch(
                    () => {}
                );

            }

        }

        catch (error) {

            console.log(
                "Sound playback error:",
                error
            );

        }

    };