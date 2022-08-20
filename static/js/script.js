document.body.addEventListener("click", function (evt) {
    document.getElementById('enter').focus();
});

window.setInterval(function(){ 
    document.getElementById('enter').focus();
}, 100); 
