<template>
  <div>
    <Title />
    <div class="body">
      <v-card elevation=0>
        <div class="cinemaImage">
          <v-img
            v-if="details.img"
            class="media"
            :src="details.img"
           >
          </v-img>
          <v-img 
            v-else
            aspect-ratio=1.7
            src="../movieDetail/movieTrailer/defaultImg.jpg">
            <template v-slot:placeholder>
              <div>
                이미지 준비중
              </div>
            </template>
          </v-img>
        </div>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title class="headline">{{ details.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ details.address }}</v-list-item-subtitle>
            <v-list-item-subtitle>
              <a 
                class="tel"
                :href="'tel' + details.tel"
                >
                {{ details.tel }}
              </a>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn 
            icon 
            :color="(isPicked) ? 'pink' : 'grey'"
            @click.prevent="togglePickCinema">
            <v-icon>mdi-heart</v-icon>
          </v-btn>

          <v-dialog v-model="dialog">
            <template v-slot:activator="{ on }">
              <v-btn
                v-on="on"
                icon 
                color="pink"
                >
                <v-icon>mdi-filmstrip</v-icon>
              </v-btn>
            </template>
            <CinemaOnScreens :onscreens="details.onscreens" @close="closeModal" />
          </v-dialog>
        </v-card-actions>

        <v-tabs
          v-model="tab"
          background-color="white"
          color="amber"
          centered
          fixed-tabs
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
                <component 
                  v-bind:is="item.component" 
                  :details="details"
                  ></component>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items>

      </v-card>
    </div>
  </div>
</template>

<script>
import Title from '../nav/Title.vue';
import CinemaInfo from './cinemaInfo/CinemaInfo';
import CinemaRatings from './cinemaRatings/CinemaRatings';
import CinemaOnScreens from './cinemaInfo/CinemaOnScreens';
import Score from '../ratingForm/Score';
import { mapGetters, mapActions } from 'vuex';


export default {
  name: 'CinemaDetail',
  components: {
    Title,
    CinemaInfo,
    CinemaRatings,
    Score,
    CinemaOnScreens,
  },

  data() {
    return {
      tab: null,
      items: [
        {tab: 'Info', component: "CinemaInfo"},
        {tab: 'Reviews', component: "CinemaRatings"}
      ],
      expand: false,
      isPicked: false,
      dialog: false,

    }
  },
  
  async created() {
    await this.fetchCinemaDetail(this.$route.params.id);
  },

  computed: {
    ...mapGetters({
      details: 'getCinemaDetail',
      }),
  },

  methods: {
    ...mapActions(['fetchCinemaDetail', 'togglePick', ]),
    async togglePickCinema() {
      const item = 'cinema'
      const itemId = this.details.id
      await this.togglePick({item, itemId})
      this.isPicked = !this.isPicked
    },
    closeModal() {
      this.dialog = false;
    },
    // TODO 텍스트 예쁘게 잘 잘라
    splitText() {

    }

  },

}
</script>


<style src="./CinemaDetail.css" scoped></style>