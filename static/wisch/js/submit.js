
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function test() {
    sleep(2000)
    console.log("LOL")
}