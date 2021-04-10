$(document).ready(function () {
    $("#toggle").click(function(){
        if(document.getElementById("toggle").value === "off"){
            console.log("off")
            document.getElementById("toggle").value = "on"
        }else{
            console.log("on")
            document.getElementById("toggle").value = "off"
        }
    });
});