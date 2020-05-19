<template>
  <div class='movieDetail'>
    <Title />
    MovieDetail
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
export default {
  name: 'MovieDetail',
  components: {
    Nav,
    Title,
  }
}
</script>

<style src="./MovieDetail.css" scoped></style>