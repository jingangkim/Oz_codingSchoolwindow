const clock = document.getElementById("clock");

function getclock(){
    const now = new Date();
    const month = now.getMonth();
    const date = now.getDate();
    const hour = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    clock.innerText = `${month}월${date}일${hour}시${minutes}분${seconds}초`;
}
getclock();
setInterval(getclock,1000);