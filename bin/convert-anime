#!/bin/bash
echo [INFO] run scripts/convert-anime.sh

targetDir=${1}
if [ -z ${targetDir} ]; then
    echo "required targetDir"
    exit
fi

pushd "${targetDir}"
echo [INFO] now on $(pwd)

for file in *.png; do
    apng2gif $file
    gif=${file/.png/.gif/}
    if [ -f $gif ]; then
        echo [INFO] save $dif
    fi
done

popd
