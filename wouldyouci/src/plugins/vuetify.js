import "@fortawesome/fontawesome-free/css/all.css";
import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: "fa"
  },
  theme: {
    themes: {
      light: {
        primary: '#FFC107',
        secondary: '#009688',
        accent: '#E91E63',
        error: '#b71c1c',
      },
    },
  },
});
