<template>
  <v-card class="timeCard">
    <v-container fluid>
      <div class="explanation">
        원하는 반경을 설정해주세요
      </div>
      <v-radio-group v-model="targetKm" column>
        <v-radio color="#00A06D" label="1 Km" value=1></v-radio>
        <v-radio color="#00A06D" label="3 Km" value=3></v-radio>
        <v-radio color="#00A06D" label="5 Km" value=5></v-radio>
      </v-radio-group>
    </v-container>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn @click="closeKmSelector(targetKm)" text>설정</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
// import { mapActions } from 'vuex';

export default {
  name: 'settingCard',
  props: ['nowKm'],
  data() {
    return{
      targetKm: 3
    }
  },
  methods: {
    closeKmSelector(targetKm) {
      this.$emit('targetKm', targetKm);
    }
  }
}
</script>

<style src="./KmSelector.css" scoped></style>