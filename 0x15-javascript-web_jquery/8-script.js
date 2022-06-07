// $(document).ready(function updateAll () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function updateMovies (data) {
    const list_movies = data.results;
    let i = 0;
    while (i <= list_movies.length) {
      const movie_title = list_movies[i].title; const content = $('<li></li>').text(movie_title);
      $('ul#list_movies').append(content);
      i++;
    }
  });