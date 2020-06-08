<template>
    <v-container class="ranklist" fluid grid-list-xl>
      <v-layout justify-center row wrap x12 md8>
        <v-flex>
          <v-row dense>
            <v-col 
              v-for="(data, idx) in cinemas.data"            
              :key="idx"
              :cols="12">
              <v-card
                @click="goTheaterDetail(data.id)"
                class="mycard"
                elevation="0">
                <v-row>
                  <v-col class="col-4">
                    <v-img
                      :src="data.img"
                      class="card_image"
                    >
                    </v-img>
                  </v-col>
                   <v-col class="pl-1 pb-0 col-8">
                    <v-list-item>
                      <v-list-item-content class="pt-3 pb-2">
                        <v-list-item-title class="mytitle">{{ data.name }}</v-list-item-title>
                        <v-list-item-subtitle class="mysubtitle">{{ data.address }}</v-list-item-subtitle>
                        <v-list-item>{{data.onscreens}}</v-list-item>
                        <!-- <v-list-item-subtitle class="mysubtitle">{{ data.tel }}</v-list-item-subtitle> -->
                      </v-list-item-content>
                    </v-list-item>
                    <v-card-text class="movieInfo">
                      <p>{{ data.tel }}</p>
                    </v-card-text>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>
          </v-row>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: "MovieShowingCinemas",

  computed: {
    ...mapGetters({
      cinemas: 'getMovieShowingCinemas'
    }),

  },

  methods: {
    ...mapActions(['fetchMovieShowingCinemas', ]),
    closeMe() {
      this.$emit("close");
      },
    goTheaterDetail(id) {
      this.$router.push(`/cinema/${id}`);
    }
  },

  async created() {
    await this.fetchMovieShowingCinemas(this.$route.params.id);
    
  }
  
}
</script>

<style src="./MovieShowingCinemas.css"></style>