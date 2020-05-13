const state = {
  LoginMode: true,
  token: null,
  
};
const getters = {
  isLoginMode: state => state.LoginMode,
  isLoggedIn: state => !!state.token
};
const mutations = {
  setLoginMode: state => (state.LoginMode = !state.LoginMode),
  setToken: (state, token) => {
    state.token = token;
    sessionStorage.setItem("jwt", token);
  },
};
const actions = {
  login: ({ commit, getters }, userInfo) => {
    if (getters.isLoggedIn) {
      console.log('로그인 된 유저');
    } else {
      commit;
      console.log(userInfo);
      // 이후로 axios 요청 보내야 함
    }
  },
  signup: ({ commit, getters }, userInfo) => {
    if (getters.isLoggedIn) {
      console.log('로그인 된 유저');
    } else {
      commit;
      console.log(userInfo);
    }
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};
