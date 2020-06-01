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
  ratings: [],
  
};

const getters = {
  getInitialized: state => state.initialized,
  getSearchMode: state => state.searchMode,
  getTheaterMovies: state => state.theaterMovies,
  getMovies: state => state.movies,
  getNearTheater: state => state.nearTheater,
  getMovieDetail: state => state.movieDetail,
  getRatings: state => state.ratings,

};

const mutations = {
  setInitialized: (state, value) => state.initialized = value,
  setSearchMode: (state, mode) => state.searchMode = mode,
  setTheaterMovies: (state, theaterMovies) => state.theaterMovies = theaterMovies,
  setMovies: (state, movies) => state.movies = movies,
  setNearTheater: (state, theaters) => state.nearTheater = theaters,
  setMovieDetail: (state, details) => state.movieDetail = details,
  setRatings: (state, ratings) => state.ratings = ratings,

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
    // console.log(initPromise)
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
  fetchRatings: ({ commit }, { movieId, page }) => {
    const params = {movieId, page}
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`
      }
    }
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/movie/rating/page/`, params, options)
        .then(res => {
          commit('setRatings', res.data);
          if (!getters.getRatings) {
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
  postRating: ({ dispatch }, rating) => {
    dispatch;
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
        "Content-Type": "application/json",
      }
    }
    return new Promise(function(resolve, reject) {
      axios.post(`${HOST}/movie/rating/`, rating, options)
        .then(res => {
          console.log(res);
          dispatch('fetchMovieDetail', rating.movie);
          resolve('ok');
        })
        .catch(err => {
          console.log(err);
          reject(Error('erroe'));
        })
      })
  },
  delRating: ({dispatch}, {ratingId, movieId}) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
      }
    }
    axios.delete(`${HOST}/movie/rating/${ratingId}/`, options)
      .then(res => {
        console.log(res);
        return dispatch('fetchMovieDetail', movieId);
        }
      )
      .catch(err => {
        console.log(err);
      })
    },
  patchRating: ({dispatch}, rating) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
        "Content-Type": "application/json",
      }
    }
    return new Promise(function(resolve, reject) {
    axios.patch(`${HOST}/movie/rating/${rating.id}/`, rating, options)
      .then(res => {
        console.log(res);
        dispatch('fetchMovieDetail', rating.movie);
        resolve('ok');
      })
      .catch(err => {
        console.log(err);
        reject(Error('erroe'));
      })
    })
  },
  togglePickMovie: ({dispatch}, movieId ) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
      }
    }
    axios.patch(`${HOST}/movie/${movieId}/pick/`, movieId, options)
      .then(res => {
        console.log(res);
        return dispatch('fetchMovieDetail', movieId);
      })
      .catch(err => {
        console.log(err)
      })
  },

};

export default {
  state,
  getters,
  mutations,
  actions
};
