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

// Function for edit user_data
function editPerson(){
  $("#personEdit").click(function(){
      var arr = $("#profileCheckBoxes :checkbox");

        if(arr.length > 0){
            var checkedPersons = [];
                for (i = 0; i < arr.length; i++){
                    if (arr[i].checked == true)
                       checkedPersons.push(arr[i].value);
                }
            if (checkedPersons.length == 0){
               $("#personEdit").popover('hide');
               $("#status_menu").html("<h4><b>Select one more persons to delete!</b></h4>");
            }
            else if (checkedPersons.length > 1){
               //$("#personEdit").popover('hide');
               $("#status_menu").html("<h4><b>Select only one person!</b></h4>");
            }
            else{
                                          $.ajax({
                                              url: this.href,
                                                   type: 'get',
                                                   dataType: 'json',
                                                   data: {
                                                           personIdEdit: checkedPersons[0]
                                                         },
                                                   success: function(data,status,xhr){
                                                   // alert(data.key.last_name);
                                                     $("#personEdit").popover('show');
                                                 var form = document.getElementById("formEditPer").elements;
                                          form["first_name"].value = data.key.first_name;
                                          form["last_name"].value = data.key.last_name;
                                          form["phone"].value = data.key.phone;
                                          form["email"].value = data.key.email;
                                          form["country"].value = data.key.country;
                                          form["city"].value = data.key.city;
                                          form["note"].value = data.key.note;
                                          form["birthday"].value = data.key.birthday;
                                          form["perId"].value = checkedPersons[0];

                                                     // document.getElementById("yo").value = "yo";
                                                     
                                                   }
                                               });
                 
                 
            }
        }
    return(false);
  });
}

// function for delete comments
function commentDelete(){
    $("#delComments").click(function(){
        var arr = getCheckedItems($("#profileCheckBoxesComments :checkbox"));
            if (arr.length == 0){
            $("#delComments").popover("show");
            $("#delCommentsInfo").text("Select one more person");
            }
            else if(arr.length > 0){
                $("#delComments").popover("hide");
                      $.ajax({
                                  url: $("#profileCheckBoxesComments").attr('action'),
                                  type: 'post',
                                  dataType: 'json',
                                  data: {
                                         checkedCom: arr,
                                   csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').prop ('value')
                                             },
                                  success: function(data,status,xhr){
                                      var status = $("#status_menu");
                                          status.html("<h4>Selected comments deleted...</h4>");
                                          $("#delInfo").text("Selected comments deleted...");

                                      $.ajax({
                                                   url: this.href,
                                                   type: 'get',
                                                   dataType: 'html',

                                                   success: function(data,status,xhr){
                                                     var form = $("#tabComments");
                                                     html = $(data);
                                                     form.html(html.find('#tabComments'));
                                                   }
                                               });

                                      }
                              });
            }
        return(false);
    });

}
// function that retrieve array of checked items, get form's checkboxes as argument
function getCheckedItems(formCheckboxes){
   var checkedItems = [];
    if(formCheckboxes.length > 0){
        for(i=0; i < formCheckboxes.length; i++){
            if (formCheckboxes[i].checked == true)
                checkedItems.push(formCheckboxes[i].value);
        }
    }
   return checkedItems;
}

$(document).ready(function(){
deletePersons();
editPerson();
commentDelete();
});
