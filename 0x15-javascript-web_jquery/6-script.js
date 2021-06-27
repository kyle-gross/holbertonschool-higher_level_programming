#!/usr/bin/node
/* Updates header when the update_header div is clicked */
$('DIV#update_header').click(function () {
  $('header').replaceWith('<header>New Header!!!</header>');
});
