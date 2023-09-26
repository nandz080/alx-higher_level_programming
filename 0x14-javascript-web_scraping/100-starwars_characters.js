#!/usr/bin/node

const requests = require('request');
const id = process.argv[2];
const landing_url = 'https://swapi-api.hbtn.io/api/films/';
requests.get(landing_url + id, function (error, reponse, body) {
  if (error) {
    console.log(error);
  }
  const movie_data = JSON.parse(body);
  const char_data = movie_data.characters;
  for (const i of char_data) {
    requests.get(i, function (error, response, body_1) {
      if (error) {
        console.log(error);
      }
      const character = JSON.parse(body_1);
      console.log(character.name);
    });
  }
});
