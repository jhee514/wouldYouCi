const API_KEY = process.env.VUE_APP_GOOGLE_MAP_API_KEY;
const KAKAO_API_KEY = process.env.VUE_APP_KAKAO_API_KEY;
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
  movieDetail: [],
  searchList: [],
  searchSimiList: [],
  initSearchInfo: null,
  address: null
};

const getters = {
  getInitialized: state => state.initialized,
  getSearchMode: state => state.searchMode,
  getTheaterMovies: state => state.theaterMovies,
  getMovies: state => state.movies,
  getMovieDetail: state => state.movieDetail,
  getSearchList: state => state.searchList,
  getSearchSimiList: state => state.searchSimiList,
  getInitSearchInfo: state => state.initSearchInfo,
  getAddress: state => state.address
};

const mutations = {
  setInitialized: (state, value) => state.initialized = value,
  setSearchMode: (state, mode) => state.searchMode = mode,
  setTheaterMovies: (state, theaterMovies) => state.theaterMovies = theaterMovies,
  setMovies: (state, movies) => state.movies = movies,
  setMovieDetail: (state, details) => state.movieDetail = details,
  setSearchList: (state, movies) => state.searchList = movies,
  setSearchSimiList: (state, movies) => state.searchSimiList = movies,
  setInitSearchInfo: (state, info) => state.initSearchInfo = info,
  setAddress: (state, address) => state.address = address
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
  bringHereCinema: ({ commit }, bound) => {
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
  searchMovies: ({ commit }, keywords) => {
    console.log(keywords);
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/search/movie/${keywords}/`)
        .then(res => {
          console.log(res);
          commit('setSearchList', res.data.search_result);
          commit('setSearchSimiList', res.data.similar_result);
          resolve(res.data);
        })
        .catch(err => {
          console.log(err);
          commit('setSearchList', null);
          commit('setSearchSimiList', null);
          reject(Error('error'));
        })
    })
  },
  searchTheater: ({ commit }, keywords) => {
    console.log(keywords);
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/search/cinema/${keywords}/`)
        .then(res => {
          console.log(res);
          commit('setSearchList', res.data.search_result);
          commit('setSearchSimiList', res.data.similar_result);
          resolve('ok');
        })
        .catch(err => {
          console.log(err);
          commit('setSearchList', null);
          commit('setSearchSimiList', null);
          reject(Error('error'));
        })
    })
  },
  bringAddress: ({ commit }, pos) => {
    const KOptions = {
      headers: {
        Authorization: `KakaoAK ${KAKAO_API_KEY}`
      }
    }
    return new Promise(function(resolve, reject) {
      axios.get(`https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=${pos.lng}&y=${pos.lat}`, KOptions)
      .then(res => {
        console.log(res);
        commit('setAddress', res.data.documents[0].address_name);
        resolve('ok')
      })
      .catch(err => {
        console.log(err);
        reject(Error('error'));
      })
    })
  },
  bringInitSearchInfo: ({ commit }, pos) => {
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`
      },
      params: {
        x: pos.lng,
        y: pos.lat
      }
    }
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/search/`, options)
      .then(res => {
        console.log(res);
        commit('setInitSearchInfo', res.data);
        resolve('ok');
      })
      .catch(err => {
        console.log(err);
        reject(Error('error'));
      })
    })
  },
  bringRatingMovies: ({ getters }) => {
    getters;
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`
      }
    }
    return new Promise(function(resolve, reject) {
      axios.get(`${HOST}/user/rating/page/`, options)
        .then(res => {
          console.log(res);
          resolve(res.data);
        })
        .catch(err => {
          console.log(err);
          reject(Error('error'));
        })
    })
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};
