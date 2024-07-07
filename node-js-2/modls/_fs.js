const fs = require('fs')

fs.readFile('./me.txt', (err, data) => {
    if (err){
        console.log(err);
    }
    console.log(data)
    console.log(data.toString())
});

console.log('pop')


fs.writeFile('./you.txt', 'lolx', () => {
    console.log('Filw written')
})


// folder
if (! fs.existsSync('./assets')){
    fs.mkdir('./assets', (err) => {
        if (err){
            console.log(err);
        }
        console.log('folder created')
    })
}else{
    fs.rmdir('./assets', (err) => {
        if (err){
            console.log(err);
        }
        console.log('folder deleted')
    })
}


// delete file
if (fs.existsSync('./c')){
    fs.unlink('./c', (err) => {
        if (err){
            console.log(err);
        }
        console.log('folder deleted')
    })
}



// stream
//const rs = fs.createReadStream('./info.txt')
const rs = fs.createReadStream('./info.txt', { encoding: 'utf8'});
const ws = fs.createWriteStream('./about.txt');

rs.on('data', (chunk) => {
    console.log(chunk);
    console.log(chunk.toString());
    ws.write(chunk);
});
