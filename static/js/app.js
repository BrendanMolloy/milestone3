/* Javascript */
 
//Make sure that the dom is ready
$(document).ready(function () {
 
  $("#rateYo").rateYo({
    rating: 3.6
  });
 
});

// Getter
var normalFill = $("#rateYo").rateYo("option", "halfStar"); //returns true
 
// Setter
$("#rateYo").rateYo("option", "halfStar", true); //returns a jQuery Element