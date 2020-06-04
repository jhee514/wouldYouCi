<template>
  <v-container class="grey lighten-5">

    
      <v-btn
        icon
        absolute
        center
        @click="closeMe"
        >
        <v-icon>mdi-close</v-icon>
      </v-btn>

      <v-row>
        <v-col cols="12">
          <v-card
            color="#385F73"
            dark
            v-for="(data, idx) in cinemas.data"            
            :key="idx"
            >
            <v-list-item>
              <v-avatar
                class="ma-3"
                width="20vw"
                height="5vh"
                tile
                >
                <v-img :src="data.img" />
              </v-avatar>
              <div>
                <v-card-subtitle>
                  {{ data.name }} « 
                  {{ data.type }}
                </v-card-subtitle>
                <v-card-actions>
                  {{ data.address }}
                  {{ data.area }}
                </v-card-actions>
                <v-btn
                  text
                  target="_blank"
                  :href="data.url" 
                  >
                  예매
                </v-btn>
              </div>
            </v-list-item>
          </v-card>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: "ShowingCinemas",

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
  },

  async created() {
    await this.fetchMovieShowingCinemas(this.$route.params.id);
    
  }
  
}
</script>

<style>

</style>