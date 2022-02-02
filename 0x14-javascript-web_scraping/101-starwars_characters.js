#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id = args[2];
const urls = [
  'https://swapi-api.hbtn.io/api/people/',
  'https://swapi-api.hbtn.io/api/people/?page=2',
  'https://swapi-api.hbtn.io/api/people/?page=3',
  'https://swapi-api.hbtn.io/api/people/?page=4',
  'https://swapi-api.hbtn.io/api/people/?page=5',
  'https://swapi-api.hbtn.io/api/people/?page=6',
  'https://swapi-api.hbtn.io/api/people/?page=7',
  'https://swapi-api.hbtn.io/api/people/?page=8',
  'https://swapi-api.hbtn.io/api/people/?page=9'
];
urls.forEach(element => {
  request(element, function (error, response, body) {
    if (error) throw error;
    const listCharacters = JSON.parse(body);
    //   console.log(listCharacters.results);
    listCharacters.results.forEach(element => {
      const name = element.name;
      element.films.forEach(element => {
        // console.log(element);
        if (element.includes(String(id))) {
          console.log(name);
        }
      });
    });
  });
});
