#!/usr/bin/node
/* Fetches and lists title of all movies from URL */
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (title, movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
