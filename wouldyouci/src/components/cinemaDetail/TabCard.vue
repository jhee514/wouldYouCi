<template>
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
            <component v-bind:is="item.component" :movie="datail"></component>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>

</template>

<script>

export default {
  name: 'TabCard',
  components: {
  },
  props:["tap", "items", "detail"],
  data() {
    return {

    }
  },
}
</script>
