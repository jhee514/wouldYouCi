const API_KEY = process.env.VUE_APP_GOOGLE_MAP_API_KEY;
const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require("axios");

var resolveInitPromise;
var rejectInitPromise;

const initPromise = new Promise((resolve, reject) => {
  console.log('in initPromise')
  resolveInitPromise = resolve;
  rejectInitPromise = reject;
});

const state = {
  initialized: !!window.google,
  searchMode: "before",
  theaterMovies: []
};

const getters = {
  getInitialized: state => state.initialized,
  getSearchMode: state => state.searchMode,
  getTheaterMovies: state => state.theaterMovies
};

const mutations = {
  setInitialized: (state, value) => state.initialized = value,
  setSearchMode: (state, mode) => state.searchMode = mode,
  setTheaterMovies: (state, theaterMovies) => state.theaterMovies = theaterMovies
};

const actions = {
  init: ({ getters, commit }) => {
    console.log('init')
    if (getters.getInitialized) return initPromise;
    commit("setInitialized", true);
    window["initMap"] = () => resolveInitPromise(window.google);
    const script = document.createElement("script");
    script.async = true;
    script.defer = true;
    script.src = `https://maps.googleapis.com/maps/api/js?key=${API_KEY}&callback=initMap`;
    script.type="text/javascript"
    script.onerror = rejectInitPromise;
    document.querySelector("body").appendChild(script);
    return initPromise;
  },
  bringHereCinema: ({ commit }, {center, radius}) => {
    console.log(radius)
    console.log(center)
    const params = {
      params: {
        x: center.lng,
        y: center.lat,
        radius: radius
      }
    }
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/cinema/map/`, params)
      .then(res => {
        console.log(res);
        commit('setTheaterMovies', res.data.documents);
        resolve('ok');
      })
      .catch(err => {
        console.log(err);
        reject(Error('error'))
      })
    })
    // axios.get(`${HOST}/cinema/map/`, params)
    //   .then(res => {
    //     console.log(res);
    //     commit('setTheaterMovies', res.data.documents);
    //     // return initPromise;
    //   })
    //   .catch(err => {
    //     console.log(err);
    //     // return initPromise;
    //   })
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};
