<template>
  <div class="cinemaInfo">
    <p>
      <span class="item">
        홈페이지
      </span>
      <span class="content">
        <v-btn :href="details.url" text>홈페이지</v-btn>
      </span>
    </p>
    <p>
      <span class="item">
        대중교통
      </span>
      <span class="content">
        {{ details.public }}
      </span>
    </p>
    <p>
      <span class="item">
        주차 
      </span>
      <span class="content">
        {{ details.parking }}
      </span>
    </p>
    <p>
      <span class="item">
        회사 
      </span>
      <span class="content">
        {{ details.type }}
      </span>
    </p>
     <p>
      <span class="item">
        전화
      </span>
      <span class="content">
      {{ details.tel }}
      </span>
    </p>
  </div>
</template>
<script>
export default {
  name: 'CinemaInfo',
  props: ["details"],
  components: {
  },
  data() {
    return {
    }
  },
}
</script>

<style src="./CinemaInfo.css" scoped></style>