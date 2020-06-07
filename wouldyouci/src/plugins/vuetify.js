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
      // },
      // main: {
        pink: '#F25CA2',
        clearBlue: '#0433BF',
        blue: '#032CA6',
        darkBlue:'#021859',
        lightBlue: '#0B9ED9',
        grey: '#0D2C40',
        lightYellow: '#F2E6A7',
        yellow: '#F2CF63',
        lightPink:'#D9A796',
        white: '#F2F2F2',
      }
    },
  },
});
