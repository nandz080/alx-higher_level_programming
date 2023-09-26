#!/usr/bin/node
const request = require('request');
const episode_num = process.argv[2];
const landing_url = 'https://swapi-api.hbtn.io/api/films/';

request(landing_url + episode_num, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
