var ROWS = 1;

function formAutoResize(textBox){
  textBox.addEventListener("scroll", AddRows);
    if(textBox.value.length <= 25){
        $("#comment_field").attr("rows","1");
        ROWS = 1;
     }
}

function AddRows(){
    ROWS+=2;
    $("#comment_field").attr("rows",ROWS);
}

// Realization of send comment to DB
function commentSend(){
$("#send_coment").click(function(event){
      var val = $(this);
      var comment = $("#comment_field").val().trim();
     if (comment == ""){
          $("#error").html("<b>Please, input data</b>");
          return(false);
      }

        $.ajax({
                  url: this.href,
                  type: 'post',
                  dataType: 'json',
                  data: {
                         person_id: val.data('person-id'),
                         user_id: val.data('user-id'),
                         comment_val: comment,
                         csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').prop('value')
                         },
                  success: function(data,status,xhr){
                            commentGet(val.data('url-for-get'));
                            $("#comment_field").val("");
                            $("#comment_field").attr("rows","1");
                            $("#error").text("");
                            //alert(data);
                           }
               });
  return(false);
});

}

// Realization of get comment from DB
function commentGet(ob_url){
    $.ajax({
               url: ob_url,
               type: 'get',
               dataType: 'html',
               success: function(data,status,xhr){
                   var content = $("#all_comments"), html = $(data);
                   content.html(html.find('#all_comments'));
                   //alert(data);
               }
          });
}

// Function add photo via link
function addPhotoLink(){
    $("#PhotoAddLink").click(function(){
       $("#photoAdd").click();
        return false;
    });
}

function photoChange(){
    $("#photoAdd").change(function(){
        $("#profileForm").submit();
    });
}

// Function for sending message through person's results
function sendMail(el){
    $("#sendMessageModal").modal();
    var form = document.getElementById("formSendMessage").elements;
        form["email"].value = el.dataset.email;
}

function onPopovers(){
    $('[data-toggle = "popover"]').popover();
}


$(document).ready(function(){
commentSend();
addPhotoLink();
photoChange();
onPopovers();
});
