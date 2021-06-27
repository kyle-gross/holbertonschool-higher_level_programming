#!/usr/bin/node
/* Updates text color of <header> to red when red_header div is clicked */
$('DIV#red_header').click(function() {
  $('header').addClass('red');
});
