#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  const film = JSON.parse(body);

  if (film.title === 'Not Found') {
    console.error('Movie not found');
    process.exit(1);
  }

  const charactersUrls = film.characters;

  charactersUrls.forEach((charactersUrl, index) => {
    request(charactersUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      const character = JSON.parse(body);

      console.log(`${index + 1}. ${character.name}`);
    });
  });
});
