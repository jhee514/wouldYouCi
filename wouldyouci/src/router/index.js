import Vue from 'vue';
import VueRouter from 'vue-router';
import MainMap from '../components/mainMap/MainMap.vue';
import MovieDetail from '../components/movieDetail/MovieDetail.vue';
import Search from '../components/search/Search.vue';
import Signup from '../components/signup/Signup.vue';
import UserPage from '../components/userPage/UserPage.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/mainMap',
    name: 'MainMap',
    component: MainMap
  },
  {
    path: '/movieDetail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/userPage',
    name: 'UserPage',
    component: UserPage
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
