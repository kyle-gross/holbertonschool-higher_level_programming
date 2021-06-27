#!/usr/bin/node
/* Fetches and displays value of 'hello' from DIV#hello */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').html(data.hello);
});
