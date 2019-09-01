#!/bin/bash
echo [INFO] from scripts/convert-soundanime.sh

targetDir=${1}
if [ -z ${targetDir} ]; then
    echo "required targetDir"
    exit
fi

cp scripts/apng2gif.js "${targetDir}"
pushd "${targetDir}"
echo $(pwd)
node apng2gif.js
rm apng2gif.js

for i in $(seq -w 99); do
    if [ -f ${i}.m4a ]; then
        ffmpeg -r 30 -i ${i}.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ${i}_nosound.mp4
        ffmpeg -i ${i}_nosound.mp4 -i ${i}.m4a -acodec copy -vcodec copy ${i}.mp4
        rm ${i}_nosound.mp4
    fi
    if [ -f ${i}.mp4 ]; then
        echo ${i}.mp4
    fi
done

popd
