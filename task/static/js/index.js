$(document).ready(function () {
    if(!localStorage.getItem("theme")){
        localStorage.setItem("theme",0);
    }

    if(localStorage.getItem("theme") == 1){
        let inputAreas = document.querySelectorAll("input,textarea,select");
        let toggle = document.getElementById("toggle");
        let navBar = document.querySelector("nav");
        let tabBar = document.querySelector(".tab");
        let bodyArea = document.querySelector("body");
        let navLogo = $("#nav-logo");
        let loginA = document.querySelectorAll(".login-form a");

        $(toggle).click();

        toggle.value = "off"

        bodyArea.style.backgroundColor = "black";
        bodyArea.style.color = "white";

        navBar.style.background = "black";
        navBar.style.border = "black";
        navBar.style.borderBottom = "1px solid white";

        if(tabBar){
            tabBar.style.background = "black";
        }

        inputAreas.forEach((input)=>{
            input.style.background = "black";
        });

        loginA.forEach((input)=>{
            input.style.color = "#6c63ff";
        });

        navLogo.attr('src', '/static/image/logo/logo_light.png')
    }

    $("#toggle").click(function(){
        let inputAreas = document.querySelectorAll("input,textarea,select");
        let toggle = document.getElementById("toggle");
        let navBar = document.querySelector("nav");
        let tabBar = document.querySelector(".tab");
        let bodyArea = document.querySelector("body");
        let navLogo = $("#nav-logo");
        let loginA = document.querySelectorAll(".login-form a");

        if(toggle.value === "off"){
            toggle.value = "on"
            bodyArea.style.backgroundColor = "white";
            bodyArea.style.color = "rgb(51, 51, 51)";

            navBar.style.background = "#f8f8f8";
            navBar.style.borderColor = "#e7e7e7";

            if(tabBar){
                tabBar.style.background = "#f1f1f1";
            }

            inputAreas.forEach((input)=>{
                input.style.background = "white";
            });

            loginA.forEach((input)=>{
                input.style.color = "#333";
            });

            localStorage.setItem("theme",0);

            navLogo.attr('src', '/static/image/logo/logo.png');
        }else{
            toggle.value = "off"

            bodyArea.style.backgroundColor = "black";
            bodyArea.style.color = "white";

            navBar.style.background = "black";
            navBar.style.border = "black";
            navBar.style.borderBottom = "1px solid white";

            if(tabBar){
                tabBar.style.background = "black";
            }

            inputAreas.forEach((input)=>{
                input.style.background = "black";
            });

            loginA.forEach((input)=>{
                input.style.color = "#6c63ff";
            });
            
            localStorage.setItem("theme",1);

            navLogo.attr('src', '/static/image/logo/logo_light.png')
        }
    });
});