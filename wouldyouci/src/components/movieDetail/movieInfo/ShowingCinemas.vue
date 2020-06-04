<template>
  <v-container class="grey lighten-5">
    <v-row>
      <div
        v-for="(data, idx) in cinemas.data"
        :key="idx"
        >
        <p>
          {{ data }}
        </p>
      </div>

    </v-row>
    
    
    
    
    <v-row>
      <v-btn
        icon
        absolute
        center
        @click="closeMe"
      >
        <v-icon>mdi-close</v-icon>
      </v-btn>
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