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
  theaterMovies: [],
  movies: [],
  nearTheater: [],
  movieDetail: [],
  
};

const getters = {
  getInitialized: state => state.initialized,
  getSearchMode: state => state.searchMode,
  getTheaterMovies: state => state.theaterMovies,
  getMovies: state => state.movies,
  getNearTheater: state => state.nearTheater,
  getMovieDetail: state => state.movieDetail,

};

const mutations = {
  setInitialized: (state, value) => state.initialized = value,
  setSearchMode: (state, mode) => state.searchMode = mode,
  setTheaterMovies: (state, theaterMovies) => state.theaterMovies = theaterMovies,
  setMovies: (state, movies) => state.movies = movies,
  setNearTheater: (state, theaters) => state.nearTheater = theaters,
  setMovieDetail: (state, details) => state.movieDetail = details,

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
  bringHereCinema: ({ getters, commit }, bound) => {
    console.log(bound)
    const params = {
      params: {
        x1: bound.x1,
        y1: bound.y1,
        x2: bound.x2,
        y2: bound.y2
      }
    }
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/cinema/map/`, params)
        .then(res => {
          console.log(res);
          commit('setTheaterMovies', res.data.documents);
          if (!getters.getNearTheater.length) {
            if (!res.data.documents.length) {
              commit('setNearTheater', ['Nothing']);
            } else {
              commit('setNearTheater', res.data.documents)
            }
          }
          resolve('ok');
        })
        .catch(err => {
          console.log(err);
          reject(Error('error'))
        })
    })
  },
  bringMovies: ({ commit }, {theaterID, time}) => {
    let params = null;
    if (time) {
      const amPm = time.split(' ')[0];
      const times = time.split(' ')[1].split(':');
      let startH = null;
      if (amPm === '오전') {
        if (times[0] === '12') {
          startH = '24'
        } else {
          startH = '0'+times[0];
        }
      } else {
        if (times[0] === '12') {
          startH = times[0];
        } else {
          startH = String(Number(times[0])+12);
        }
      }
      params = {
        params: {
          start_time: `${startH}:${times[1]}`
        }
      };
    }
    console.log(params);
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/cinema/map/${theaterID}/movie/`, params)
        .then(res => {
          console.log(res);
          commit('setMovies', res.data.documents);
          resolve('ok');
        })
        .catch(err => {
          console.log(err);
          reject(Error('error'))
        })
    })
  },
  fetchMovieDetail: ({ getters, commit }, movieId) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`
      }
    }
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/movie/${movieId}/`, options)
        .then(res => {
          commit('setMovieDetail', res.data);
          if (!getters.getMovieDetail) {
            console.log('no movie data')
          }
          resolve('ok')
        })
        .catch(err => {
          console.log(err);
          reject(Error('error'))
        })
    })

  },
  postRating: ( {commit}, rating) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        "Content-Type": "application/json",
        Authorization: `JWT ${token}`,
      }
    }
    axios.post(`${HOST}/movie/rating/`, rating, options)
      .then(res => {
        console.log(res);
        commit();
      })
      .catch(err => {
        console.log(err);
      })
  },
  delRating: ({dispatch}, ratingId) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
      }
    }
    axios.delete(`${HOST}/movie/rating/${ratingId}/`, options)
      .then(res => {
        console.log(res);
        dispatch();
      })
      .catch(err => {
        console.log("erorororororo")
        console.log(err);
      })
  },

};

export default {
  state,
  getters,
  mutations,
  actions
};
