#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(`${url}`, function (err, body) {
  if (err) throw err;
  const actorsto = JSON.parse(body).characters;
  exactOrder(actorsto, 0);
});
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
