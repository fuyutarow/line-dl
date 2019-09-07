#!/bin/bash
echo [INFO] run scripts/convert-sound.sh

targetDir=${1}
if [ -z ${targetDir} ]; then
    echo "required targetDir"
    exit
fi

pushd "${targetDir}"
echo [INFO] now on $(pwd)

for i in $(seq -w 99); do
    if [ -f ${i}.m4a ]; then
        ffmpeg -loop 1 -i ${i}.png -i ${i}.m4a:loop=0 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest ${i}.mp4
    fi
    if [ -f ${i}.mp4 ]; then
        echo [INFO] save ${i}.mp4
    fi
done

popd
