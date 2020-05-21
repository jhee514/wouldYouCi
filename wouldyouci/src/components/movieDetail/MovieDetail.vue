<template>
  <v-app>
    <Title />
    <div class="movieDetail">
      <v-list-item two-line>
        <v-list-item-content>
          <iframe 
            title=details.fields.name
            height=auto
            width=auto
            :src=details.fields.trailer
            allowfullscreen 
            frameborder="0" 
            scrolling="no" 
            allow="autoplay"
            ></iframe>
          <v-list-item-title class="headline">{{ details.fields.name }}</v-list-item-title>
          <v-list-item-subtitle>{{ details.fields.name_eng }}</v-list-item-subtitle>
          <v-list-item-subtitle>{{ details.fields.watch_grade }}</v-list-item-subtitle>
          <v-list-item-subtitle>
            <v-rating
              :value=rating
              background-color="orange lighten-3"
              color="amber"
              dense
              half-increments
              readonly
              size="14"></v-rating>
          </v-list-item-subtitle>

            {{ details.fields.summary }}

          <v-card>
            <v-tabs
              fixed-tabs
              v-model="tab"
              background-color="orange lighten-3"
              dark
            >
              <v-tab
                v-for="item in items"
                :key="item.tab"
              >
                {{ item.tab }}
              </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
              <v-tab-item
                v-for="item in items"
                :key="item.tab"
              >
                <v-card flat>
                  <v-card-text>
                    <component v-bind:is="item.component" :movie="details"></component>
                  </v-card-text>
                </v-card>
              </v-tab-item>
            </v-tabs-items>
          </v-card>
        </v-list-item-content>
      </v-list-item>
    </div>
    <Nav />
  </v-app>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import MovieInfo from './movieInfo/MovieInfo';
import MovieReview from './movieReview/MovieReview';
export default {
  name: 'MovieDetail',
  components: {
    Nav,
    Title,
    MovieInfo,
    MovieReview,
  },
  data() {
    return {
      tab: null,
      items: [
        {tab: 'Info', component: "MovieInfo"},
        {tab: 'Reviews', component: "MovieReview"}
      ],
      rating: 1.5,
      details: {
        "pk": 152691,
        "fields": {
          "name": "\uace0\uc591\uc774 \uc9d1\uc0ac",
          "name_eng": "Our Cat",
          "watch_grade": "\uc804\uccb4 \uad00\ub78c\uac00",
          "running_time": "97\ubd84",
          "summary": "\ub0d0\uc639~\u2665\uc774\ub780 \ub9c8\ubc95\uc5d0 \ube60\uc838\ubc84\ub838\ub2e4!\r\n\uc774\ub984 \ube7c\uace0 \ub2e4 \uc8fc\ub294 \ubc14\uc774\uc62c\ub9b0 \uac00\uac8c \uc544\uc800\uc528,\r\n \uc9dc\uc7a5\uba74 \ub300\uc2e0 \uace0\uc591\uc774 \ub3c4\uc2dc\ub77d \ubc30\ub2ec\ud558\ub294 \uc911\uad6d\uc9d1 \uc0ac\uc7a5\ub2d8\ubd80\ud130\r\n \uae09\uc2dd\uc18c \ub9cc\ub4e4\uc5b4 \uc8fc\ub294 \uc8fc\ubbfc\uc13c\ud130 \uc0ac\ub78c\ub4e4,\r\n \ub0a8\uaca8\uc9c8 \uace0\uc591\uc774\ub4e4\uc744 \uac71\uc815\ud558\uba70 \ubc25\uc744 \uc8fc\ub294 \uc0dd\uc120\uac00\uac8c \ud560\uba38\ub2c8,\r\n \uae09\uc2dd\uc18c\ub97c \uc81c\uc791\ud558\ub294 \uccad\uc0ac\ud3ec \ub9c8\uc744 \uccad\ub144 \uc0ac\uc5c5\uac00\uae4c\uc9c0!\r\n \ud568\uaed8 \uc0b4\uc544\uac08 \uc218 \uc788\ub2e4\uba74 \ubaa8\ub4e0 \uac83\uc744 \ud138\ub824\ub3c4 \ud589\ubcf5\ud55c \uc9d1\uc0ac\ub4e4\uc758 \uc0ac\ub791 \uc774\uc57c\uae30\uac00 \uc2dc\uc791\ub41c\ub2e4!",
          "open_date": "2020-05-14",
          "trailer": "https://tv.naver.com/embed/13771927?autoPlay=true",
          "poster": "https://movie-phinf.pstatic.net/20200427_139/1587954977691kaCua_JPEG/movie_image.jpg",
          "directors": [
              1
          ],
          "genres": [
              1
          ],
          "actors": [
              2
          ]
        }
      }
    }
  },
}
</script>

<style src="./MovieDetail.css" scoped></style>