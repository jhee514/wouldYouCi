<template>
  <div >
    <div v-if="details.trailer">
      <div class="image-container"
        >
        <v-img
          v-if="details.poster"
          @click.stop="dialog = true"
          class="media"
          :src="details.poster" />
        <v-img 
          v-else
          class="media"
          @click.stop="dialog = true"
          src="./defaultImg.jpg" />
      </div>
      <v-dialog
        v-model="dialog"
        min-width="290"
      >
        <v-card>
          <div class="trailer-container">
            <iframe 
              class="iframe"
              type="text/html" 
              frameborder=0
              allowfullscreen
              :src="details.trailer"
              ></iframe>
          </div>
          <v-card-actions>

            <v-btn
              class="align-center"
              color="green darken-1"
              text
              @click="dialog = false"
              >
              close
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>

    <div v-else>
      <v-img
        v-if="details.poster"
        class="media"
        :src="details.poster" />
      <v-img 
        v-else
        class="media"
        src="./defaultImg.jpg" />
    </div>
  </div>
</template>

<script>

export default {
  name: "MovieTrailer",
  props: ["details"],
  data() {
    return {
      dialog: false,
    }
  },

}
</script>

<style src="./MovieTrailer.css" scoped></style>