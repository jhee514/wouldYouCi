<template>
  <div>
    <Title />
    <div class='userPage'>
      userPage
    </div>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';

export default {
  name: 'UserPage',
  components: {
    Nav,
    Title
  }
}
</script>

<style src="./UserPage.css" scoped></style>