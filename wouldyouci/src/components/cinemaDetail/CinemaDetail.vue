<template>
  <v-app>
    <Title />

    <div class="cinemaInfo">
      <v-list-item two-line>
        <v-list-item-content>
          <v-img :src=details.fields.image />
          
          <v-list-item-title class="headline">{{ details.fields.name }}</v-list-item-title>
          
          <v-list-item-subtitle>{{ details.fields.name_eng }}</v-list-item-subtitle>
          
          <v-list-item-subtitle>
            <v-rating
              :value=rating
              background-color="orange lighten-3"
              color="amber"
              dense
              half-increments
              readonly
              size="14" />
          </v-list-item-subtitle>

          <v-card>
            <v-tabs
              fixed-tabs
              v-model="tab"
              background-color="orange lighten-3"
              dark>
              <v-tab
                v-for="item in items"
                :key="item.tab">
                {{ item.tab }}
              </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
              <v-tab-item
                v-for="item in items"
                :key="item.tab">
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
import CinemaInfo from './cinemaInfo/CinemaInfo';
export default {
  name: 'CinemaDetail',
  components: {
    Nav,
    Title,
		CinemaInfo,
  },
  data() {
    return {
      tab: null,
      items: [
        {tab: 'Info', component: "CinemaInfo"},
        {tab: 'Reviews', component: "MovieReview"}
      ],
      details: {
        "pk": 152691,
        "fields": {
          "name": "\uace0\uc591\uc774 \uc9d1\uc0ac",
          "name_eng": "Our Cat",
          "watch_grade": "\uc804\uccb4 \uad00\ub78c\uac00",
          "running_time": "97\ubd84",
          "open_date": "2020-05-14",
          "image": "http://img.cgv.co.kr/Theater/Theater/2014/1211/CGVgangnam.jpg",
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

<style src="./CinemaDetail.css" scoped></style>