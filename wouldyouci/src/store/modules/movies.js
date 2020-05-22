// const HOST = process.env.VUE_APP_SERVER_HOST;
const API_KEY = process.env.VUE_APP_GOOGLE_MAP_API_KEY;

var resolveInitPromise;
var rejectInitPromise;

const initPromise = new Promise((resolve, reject) => {
  console.log('in initPromise')
  resolveInitPromise = resolve;
  rejectInitPromise = reject;
});

const state = {
  initialized: !!window.google,
  searchMode: "before"
};

const getters = {
  getInitialized: state => state.initialized,
  getSearchMode: state => state.searchMode
};

const mutations = {
  setInitialized: (state, value) => state.initialized = value,
  setSearchMode: (state, mode) => state.searchMode = mode
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
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};
