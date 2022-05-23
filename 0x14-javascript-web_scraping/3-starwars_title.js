#!/usr/bin/node
const axios = require('axios').default;
const process = require('process');
const x = process.argv[2];
axios.get('https://swapi-api.hbtn.io/api/films')
  .then(function (response) {
    console.log(response.data.results[x - 1].title);
  })
  .catch(function (error) {
    console.log(error);
  });
