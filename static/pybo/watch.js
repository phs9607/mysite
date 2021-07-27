// 디지털 시계 구현
setInterval(myWatch, 1000) //1초 간격으로 시간 설정

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString()  // 시간을 문자열로 반환
    document.getElementById("demo").innerHTML = now;
}

