<template>
  <div class='signup'>
    <div class='logo'>
      <img class='logo' src='../../assets/saturn-309071_640.png' />
    </div>
    <div class='title'>
      <img class='title' src='../../assets/title.png' />
    </div>
    <LoginForm v-if="isLoginMode" />
    <SignupForm v-else />
  </div>
</template>

<script>
  import LoginForm from './forms/LoginForm.vue';
  import SignupForm from './forms/SignupForm.vue';
  import { mapGetters } from 'vuex';
  import router from "../../router";

  export default {
    name: 'Signup',
    components: {
      SignupForm,
      LoginForm
    },
    computed: {
      ...mapGetters(['isLoginMode', 'isLoggedIn'])
    },
    created() {
      if (this.isLoggedIn) {
        router.push('/');
      }
    }
  }
</script>

<style src="./Signup.css" scoped></style>