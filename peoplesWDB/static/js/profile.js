// Those function delete persons from user profile
function deletePersons(){
    $("#personDel").click(function(){
        var arr = $("#profileCheckBoxes :checkbox");
        if(arr.length > 0){
            var checkedPersons = [];
                for (i = 0; i < arr.length; i++){
                    if (arr[i].checked == true)
                       checkedPersons.push(arr[i].value);
                }
                   if(checkedPersons.length > 0){
                             $.ajax({
                                  url: $("#profileCheckBoxes").attr('action'),
                                  type: 'post',
                                  dataType: 'json',
                                  data: {
                                         checkedPer: checkedPersons,
                                   csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').prop ('value')
                                             },
                                  success: function(data,status,xhr){
                                            //alert(data['deletedPersons']);
                                          var status = $("#status_menu");
                                              status.html("<h4>Deleted persons:</h4>");
                                              delPer = data['deletedPersons'];
                                              for(i = 0; i < delPer.length; i++){
                                                   status.append("<h5>. <b>" + delPer[i] + "</b></h5>")
                                              }
      
                                               $.ajax({
                                                   url: this.href,
                                                   type: 'get',
                                                   dataType: 'html',
                                                   success: function(data,status,xhr){
                                                     var form = $("#profileCheckBoxes");
                                                     html = $(data);
                                                     form.html(html.find('#profileCheckBoxes'));
                                                   }
                                               });
                                      }
                              });
                        
                   }
                   else{
                         $("#status_menu").html("<h4><b>Select one more persons to delete!</b></h4>");
                       }
        }
        else
          $("#status_menu").html("<h4><b>There isn't persons!</b></h4>");

       return false;
    });
    }


$(document).ready(function(){
deletePersons();
});
