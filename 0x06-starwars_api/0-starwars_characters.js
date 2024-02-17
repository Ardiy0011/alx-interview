#!/usr/bin/node

const request = require('request');

const args = 'https://swapi-api.hbtn.io/api/films/';
request(`${args}` + process.argv[2], function (err, body) {
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
