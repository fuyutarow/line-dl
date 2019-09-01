const fs = require('fs');
const path = require('path');
const apng2gif = require("apng2gif");

const pwd = process.cwd();

fs.readdir(pwd, (err, files) => {
    files.forEach( fname => {
        if (path.extname(fname) != ".png") return;

        gif = fname.replace(".png",".gif");
        apng2gif.sync(fname, gif);
        console.log(`${gif}`);
    })
});
