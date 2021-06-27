#!/usr/bin/node
/* Updates text color of <header> to red when red_header div is clicked */
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
