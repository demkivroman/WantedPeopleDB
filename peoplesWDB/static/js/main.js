var ROWS = 1;

function formAutoResize(textBox){
textBox.addEventListener("scroll", AddRows);
    if(textBox.value.length == 15){
        $("#comment_field").attr("rows","1");
        ROWS = 1;
     }
}

function AddRows(){
ROWS+=2;
$("#comment_field").attr("rows",ROWS);
}




$(document).ready(function(){
//formAutoResize();
});
