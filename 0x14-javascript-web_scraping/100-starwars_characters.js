#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id = args[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request(url, function (error, response, body) {
  if (error) throw error;
  const film = JSON.parse(body);
  film.characters.forEach(element => {
    request(element, function (error, response, body) {
      if (error) throw error;
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
