var settingsWindow = document.getElementById('settings-window')
var overlay = document.getElementById('overlay')
// Функция-инструмент для того чтобы ставить  куки
// 
// 
function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}



// Функция-инструмент для того чтобы брать куки у юзера
//  
// 
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;

}
// Функция-инструмент для того чтобы стирать куки
//  
// 


function eraseCookie(name) {
    document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}



function promptMe() {
    var userAdjective = prompt("Введите идентификатор сессии, которую вы хотите восстановить");
}
function openSettings() {
    

    overlay.style.display = "block"
    settingsWindow.style.display = "block"
    var ball = document.getElementById('settings-window-header')
    ball.onmousedown = function (event) {

        let shiftX = event.clientX - ball.getBoundingClientRect().left;
        let shiftY = event.clientY - ball.getBoundingClientRect().top;


        moveAt(event.pageX, event.pageY);

        // moves the ball at (pageX, pageY) coordinates
        // taking initial shifts into account
        function moveAt(pageX, pageY) {
            settingsWindow.style.left = pageX - shiftX - 1 + 'px';
            settingsWindow.style.top = pageY - shiftY - 1 + 'px';
        }

        function onMouseMove(event) {
            moveAt(event.pageX, event.pageY);
        }

        // move the ball on mousemove
        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
        // drop the ball, remove unneeded handlers
        function onMouseUp() {
            document.removeEventListener('mousemove', onMouseMove);
            document.removeEventListener('mouseup', onMouseUp);

            ball.onmouseup = null;
        };

    };

}
function closeSettings() {
    overlay.style.display = "none"
    settingsWindow.style.display = "none"
}
function setStyleSheet(ss) {
    var other = document.head.querySelectorAll('link[rel="stylesheet"]')[1];
    var newss = document.head.querySelector(`link[title = "${ss}"]`);
    other.setAttribute('disabled', '');
    other.setAttribute('rel', 'alternate stylesheet');
    newss.removeAttribute('disabled');
    newss.setAttribute('rel', 'stylesheet');

}

function setFont(font) {
    document.body.style.fontFamily = font
}


function setFontfromCookies(font) {
    if (style_cookie) {
        var title = get_active_stylesheet();
        set_cookie(font_cookie, title, 365);
    }
}