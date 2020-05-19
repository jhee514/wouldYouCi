<template>


  <v-sheet
      class="mx-auto"
      elevation="0"
      max-width="100%"
      max-height="100%"
    >
      <v-slide-group
        v-model="model"
        class="pa-1"
        active-class="success"
        show-arrows
      >
        <v-slide-item
          v-for="card in cards"
            :key="card"
            v-slot:default="{ active, toggle }"
        >
        
          <v-card
            :color="active ? 'primary' : 'grey lighten-1'"
            class="ma-10"
            height="150"
            width="150"
            @click="toggle"
          >
      

            <v-row
              class="fill-height"
              align="center"
              justify="center"
            >
            <v-scale-transition>
                  
                <v-icon
                  v-if="active"
                  color="white"
                  size="48"
                  v-text="'mdi-close-circle-outline'"
                ></v-icon>
              </v-scale-transition>
        
           <v-img
                :src="card.src"
                class="white--text "
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                witdh="150"
                height="150"
              >
           <vue-star animate="animated bounceIn" color="#F05654">
             
    <i slot="icon"  class="fas fa-star fa-2x"></i>
  </vue-star>
       
        <!-- <v-checkbox
          v-model="caseSensitive"
          dark
         
          hide-details
        ></v-checkbox> -->
          <!--use animate.css and font-awesome -->

        
               
              </v-img>
             
            </v-row>
              <v-card-title v-text="card.title" ></v-card-title>
          </v-card>
          
        </v-slide-item>
      </v-slide-group>
    </v-sheet>


</template>

<script>
import VueStar from 'vue-star'
export default {
 components : {
     VueStar,
 },
 data: () => ({
     cards: [
      { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex:4},
      { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex:4 },
      { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex:4 },
      { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex:4},
      { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex:4 },
      { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex:4 },
    ],
 })
}
</script>

<style>

</style>