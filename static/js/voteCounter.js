document.querySelector(".up").addEventListener("click",function () {
    var count = parseInt(document.querySelector("#count").textContent);
    count++;
    document.querySelector("#count").textContent = count.toString();
	

});

document.querySelector(".down").addEventListener("click",function () {
    var count = parseInt(document.querySelector("#count").textContent);

    if( count > 0){
        count--;
    }
    else{
        count === 0;
    }
    document.querySelector("#count").textContent = count.toString();
});