import router from "../../router";

const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require("axios");

const state = {
  LoginMode: true,
  token: null,
  userName: null,
  errors: []
};

const getters = { 
  isLoginMode: state => state.LoginMode,
  isLoggedIn: state => !!state.token,
  getUserName: state => state.userName,
  getErrors: state => state.errors
};

const mutations = {
  setLoginMode: state => (state.LoginMode = !state.LoginMode),
  setToken: (state, token) => {
    state.token = token;
    sessionStorage.setItem("jwt", token);
  },
  setUserName: (state, userName) => {
    state.userName = userName;
    sessionStorage.setItem("name", userName);
  },
  pushError: (state, error) => state.errors.push(error),
  clearErrors: state => state.errors = []
};

const actions = {
  initialLogin: ({ commit }) => {
    const token = sessionStorage.getItem("jwt");
    const userName = sessionStorage.getItem("name");
    if (token) {
      commit("setToken", token);
      commit("setUserName", userName);
    }
  },
  login: ({ getters, commit, dispatch }, userInfo) => {
    if (getters.isLoggedIn) {
      router.push("/");
    } else {
      commit("clearErrors");
      const data = {
        username: userInfo.userName,
        password: userInfo.password
      }
      const options = {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json"
        }
      }
      if (!userInfo.userName && !userInfo.password) {
        commit("pushError", "아이디를 입력해주세요.")
        commit("pushError", "비밀번호를 입력해주세요.")
      } else if (!userInfo.password) {
        commit("pushError", "비밀번호를 입력해주세요.")
      } else if (!userInfo.userName) {
        commit("pushError", "아이디를 입력해주세요.")
      } else {
        axios.post(`${HOST}/user/login/`, data, options)
        .then(res => {
          console.log(res)
          commit("setToken", res.data.token);
          commit("setUserName", userInfo.userName);
          dispatch("checkRating");
          // router.push("/firstRating");
        })
        .catch(err => {
          console.log(err)
          console.log(userInfo)
          if (err.response && err.response.data.non_field_errors.length) {
            commit("pushError", "아이디 혹은 패스워드가 올바르지 않습니다.")
          }
        })
      }
    }
  },
  signup: ({ getters, commit, dispatch }, userInfo) => {
    if (getters.isLoggedIn) {
      router.push("/");
    }
    commit("clearErrors");
    if (!userInfo.userName && !userInfo.password && !userInfo.email) {
      commit("pushError", "아이디를 입력해주세요.")
      commit("pushError", "이메일을 입력해주세요.")
      commit("pushError", "비밀번호를 입력해주세요.")
    } else if (!userInfo.userName && !userInfo.password) {
      commit("pushError", "아이디를 입력해주세요.")
      commit("pushError", "비밀번호를 입력해주세요.")
    } else if (!userInfo.userName && !userInfo.email) {
      commit("pushError", "아이디를 입력해주세요.")
      commit("pushError", "이메일을 입력해주세요.")
    } else if (!userInfo.email && !userInfo.password) {
      commit("pushError", "이메일을 입력해주세요.")
      commit("pushError", "비밀번호를 입력해주세요.")
    } else if (!userInfo.userName) {
      commit("pushError", "아이디를 입력해주세요.")
    } else if (!userInfo.email) {
      commit("pushError", "이메일을 입력해주세요.")
    } else if (!userInfo.password) {
      commit("pushError", "비밀번호를 입력해주세요.")
    } else {
      if (userInfo.password !== userInfo.passwordConfirm) {
        commit("pushError", "비밀번호가 일치하지 않습니다.")
      } else {
        const data = {
          username: userInfo.userName,
          password: userInfo.password,
          email: userInfo.email
        }
        const options = {
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json"
          }
        }
        axios.post(`${HOST}/user/`, data, options)
          .then(res => {
            console.log(res);
            const credentials = {
              userName: userInfo.userName,
              password: userInfo.password
            }
            dispatch("login", credentials);
          })
          .catch(err => {
            console.log(err.response);
            console.log(userInfo);
            if (err.response && err.response.data.message.username){
              for (let i=0; i<err.response.data.message.username.length; i++){
                if (err.response.data.message.username[i] === "user의 username은/는 이미 존재합니다.") {
                  commit("pushError", "이미 존재하는 아이디입니다.");
                } else if (err.response.data.message.username[i] === "이 필드의 글자 수가 20 이하인지 확인하십시오.") {
                  commit("pushError", "아이디는 20자 이하만 가능합니다.");
                } else {
                  commit("pushError", err.response.data.message.username[i]);
                }
              }
            }
            if (err.response && err.response.data.message.email) {
              for (let i=0; i<err.response.data.message.email.length; i++){
                commit("pushError", err.response.data.message.email[i]);
              }
            }
            if (err.response && err.response.data.message.password) {
              for (let i=0; i<err.response.data.message.password.length; i++) {
                commit("pushError", err.response.data.message.password[i]);
              }
            }
          })
      }
    }
  },
  logout: ({ commit }) => {
    commit("setToken", null);
    commit("setUserName", null);
    sessionStorage.removeItem("jwt");
    sessionStorage.removeItem("name");
    router.push("/signup");
  },
  checkRating: ({ getters }) => {
    getters;
    const token = sessionStorage.getItem('jwt');
    const options = {
      headers: {
        Authorization: `JWT ${token}`
      }
    }
    axios.get(`${HOST}/user/login/rating/`, options)
      .then(res => {
        if (!res.data.rating_tf) {
          console.log('평가 안 함');
          router.push('/firstRating');
        } else {
          console.log('평가 함');
          router.push('/');
        }
        console.log(res);
      })
      .catch(err => {
        console.log(err);
      })
  }
};

export default {
  state,
  getters,
  mutations,
  actions
};
