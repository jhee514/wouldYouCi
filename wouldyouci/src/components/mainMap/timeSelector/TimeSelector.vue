<template>
  <v-card class="timeCard">
    <v-container fluid>
      <div class="explanation">
        원하는 시간을 설정해주세요
      </div>
      <v-row>
        <v-col cols="12" sm="4">
          <v-select v-model="targetType" :items="type" outlined label="오전/오후"></v-select>
        </v-col>
        <v-col cols="12" sm="4">
          <v-select v-model="targetHours" :items="hours" outlined label="시간"></v-select>
        </v-col>
        <v-col cols="12" sm="4">
          <v-select v-model="targetMins" :items="mins" outlined label="분"></v-select>
        </v-col>
      </v-row>
    </v-container>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn @click="closeTimeSelector(`${targetType} ${targetHours}:${targetMins}:00`)" text>설정</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
// import { mapActions } from 'vuex';

export default {
  name: 'settingCard',
  props: ['nowTime'],
  data() {
    return{
      type: [
        '오전',
        '오후'
      ],
      hours: [
        '00',
        '01',
        '02',
        '03', 
        '04',
        '05', 
        '06',
        '07',
        '08',
        '09',
        '10',
        '11'
      ],
      mins: [
        '00', 
        '10', 
        '20',
        '30',
        '40',
        '50'
      ],
      targetType: null,
      targetHours: null,
      targetMins: null
    }
  },
  methods: {
    closeTimeSelector(targetTime) {
      this.$emit('targetTime', targetTime);
    }
  }
}
</script>

<style src="./TimeSelector.css" scoped></style>