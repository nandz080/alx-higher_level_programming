#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;

request(filmUrl, function (error, response, body) {
  if (!error) {
    const characterUrls = JSON.parse(body).characters;
    printCharacters(characterUrls, 0);
  }
});

function printCharacters(characterUrls, index) {
  request(characterUrls[index], function (error, response, body) {
    if (!error) {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      if (index + 1 < characterUrls.length) {
        printCharacters(characterUrls, index + 1);
      }
    }
  });
}
