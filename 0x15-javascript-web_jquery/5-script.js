$(document).ready(function add_element () {
    $('DIV#add_item').click(function element_add() {
        const add = $('<li></li>').text("Item");
      $('UL.my_list').append(Item);
    });
  });