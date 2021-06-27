#!/usr/bin/node
/* Adds a list item when the add_item div is clicked */
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
