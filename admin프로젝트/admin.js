const clock = document.getElementById("clock");

function getclock(){
    const now = new Date();
    const month = now.getMonth()+1;
    const date = now.getDate();
    const hour = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    clock.innerText = `${month}월${date}일${hour}시${minutes}분${seconds}초`;
}
getclock();
setInterval(getclock,1000);

  function darkmode() { // 야간모드 호출
    let body = document.body; 
    body.classList.toggle("dark-mode");
    let darkmodeButton = document.getElementById("darkmode");
    if (body.classList.contains("dark-mode")) {
        darkmodeButton.innerText = "주간모드";
    } else {
        darkmodeButton.innerText = "야간모드";
    }
}


