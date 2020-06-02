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
  movieRatings: [],
  cinemaDetail: [],
  cinemaRatings: [],
};

const getters = {
  getInitialized: state => state.initialized,
  getSearchMode: state => state.searchMode,
  getTheaterMovies: state => state.theaterMovies,
  getMovies: state => state.movies,
  getNearTheater: state => state.nearTheater,
  getMovieDetail: state => state.movieDetail,
  getMovieRatings: state => state.movieRatings,
  getCinemaDetail: state => state.cinemaDetail,
  getCinemaRatings: state => state.cinemaRatings,
};

const mutations = {
  setInitialized: (state, value) => state.initialized = value,
  setSearchMode: (state, mode) => state.searchMode = mode,
  setTheaterMovies: (state, theaterMovies) => state.theaterMovies = theaterMovies,
  setMovies: (state, movies) => state.movies = movies,
  setNearTheater: (state, theaters) => state.nearTheater = theaters,
  setMovieDetail: (state, details) => state.movieDetail = details,
  setMovieRatings: (state, ratings) => state.movieRatings = ratings,
  setCinemaDetail: (state, details) => state.cinemaDetail = details,
  setCinemaRatings: (state, ratings) => state.cinemaRatings = ratings,
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
          console.log(res)
          resolve('ok')
        })
        .catch(err => {
          console.log(err);
          reject(Error('error'))
        })
    })
  },
  fetchCinemaDetail: ({ commit }, cinemaId) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`
      }
    }
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/cinema/${cinemaId}/`, options)
        .then(res => {
          commit('setCinemaDetail', res.data);
          console.log(res)
          resolve('ok')
        })
        .catch(err => {
          console.log(err);
          reject(Error('error'))
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
  togglePick: ({dispatch}, {item, itemId}) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
      }
    }
    axios.patch(`${HOST}/${item}/${itemId}/pick/`, 1, options)
      .then(res => {
        console.log(res);
        if ( item == 'cinema' ) {
          return dispatch('fetchCinemaDetail', itemId)
        } else {
          return dispatch('fetchMovieDetail', itemId);
        }
      })
      .catch(err => {
        console.log(err)
      })
  },
  fetchRatings: ({ commit }, {item, params} ) => {
    commit;
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
      },
      params: params
    }
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/${item}/rating/page/`, options)
        .then(res => {
          console.log(res.data.results)
          resolve(res.data.results)
        })
        .catch(err => {
          console.log(err);
          reject(Error('error'))
        })
    })
  },
  postRating: ({ dispatch }, {item, rating}) => {
    dispatch;
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
        "Content-Type": "application/json",
      }
    }
    return new Promise(function(resolve, reject) {
      axios.post(`${HOST}/${item}/rating/`, rating, options)
        .then(res => {
          console.log(res);
          dispatch;
          resolve(res);
        })
        .catch(err => {
          console.log(err);
          reject(Error('erroe'));
        })
      })
  },
  delRating: ({dispatch}, {item, ratingId}) => {
    dispatch;
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
      }
    }
    axios.delete(`${HOST}/${item}/rating/${ratingId}/`, options)
      .then(res => {
        console.log(res);
        }
      )
      .catch(err => {
        console.log(err);
      })
    },
  patchRating: ({dispatch}, {item, editedRating}) => {
    dispatch;
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`,
        "Content-Type": "application/json",
      }
    }
    return new Promise(function(resolve, reject) {
    axios.patch(`${HOST}/${item}/rating/${editedRating.id}/`, editedRating, options)
      .then(res => {
        console.log(res);
        resolve(res);
      })
      .catch(err => {
        console.log(err);
        reject(Error('error'));
      })
    })
  },
  

};

export default {
  state,
  getters,
  mutations,
  actions
};
