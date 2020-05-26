const axios = require("axios");

const instance = axios.create({
  // baseURL: process.env.VUE_APP_SERVER_HOST,
  // baseURL: "http://62f15d4f.ngrok.io/",
  baseURL: "https://wouldyouci.ga/",
  headers: {
    'Content-Type' : 'application/json'
  }
});

export function fetchMovie(id) {
  return instance.get(`/movie/${id}`);
}

export function fetchCinema(id) {
  return instance.get(`cinema/${id}`);
}