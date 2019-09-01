#!/bin/bash

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
popd
