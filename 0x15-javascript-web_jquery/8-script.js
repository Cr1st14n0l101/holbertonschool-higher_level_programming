const $ = window.jQuery;
moviesList();

async function moviesList () {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const result = await response.json();
  const movies = result.results;
  movies.forEach(element => {
    $('UL#list_movies').append(element.title + '<br>');
  });
}
