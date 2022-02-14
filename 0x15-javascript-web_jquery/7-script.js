const $ = window.jQuery;
getCharacter();

async function getCharacter () {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await response.json();
  $('DIV#character').append(data.name);
}
