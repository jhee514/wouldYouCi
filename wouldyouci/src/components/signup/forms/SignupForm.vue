<template>
  <v-card class="form" outlined>
    <v-card-title>Signup</v-card-title>
    <v-card-text>
      <v-form>
        <div v-if="getErrors.length" class="errors">
          <ul>
            <li v-for="(error, idx) in getErrors" :key="idx">{{ error }}</li>
          </ul>
        </div>
        <v-text-field
          label="Id"
          name="Id"
          prepend-icon="fas fa-user"
          type="text"
          v-model="userInfo.userName"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          id="email"
          label="E-mail"
          name="email"
          prepend-icon="fas fa-envelope"
          type="email"
          v-model="userInfo.email"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          id="password"
          label="Password"
          name="password"
          prepend-icon="fas fa-lock"
          type="password"
          v-model="userInfo.password"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          id="passwordConfirm"
          label="Password Confirmation"
          name="passwordConfirm"
          prepend-icon="fas fa-lock"
          type="password"
          v-model="userInfo.passwordConfirm"
          :rules="[rules.required, rules.passwordMatch]"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn text @click='setLoginMode'>Login</v-btn>
      <v-btn text @click.prevent='signup(userInfo)'>Submit</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  import { mapGetters, mapMutations, mapActions } from 'vuex';
  export default {
    name: 'SignupForm',
    data() {
      return {
        userInfo: {
          userName: '',
          email: '',
          password: '',
          passwordConfirm: ''
        },
        rules: {
          required: value => !!value || '필수 항목입니다.',
          passwordMatch: value => value === this.userInfo.password || '비밀번호가 일치하지 않습니다.'
        }
      }
    },
    computed: {
      ...mapGetters(['getErrors'])
    },
    methods: {
      ...mapMutations(['setLoginMode', 'clearErrors']),
      ...mapActions(['signup'])
    },
    created() {
      this.clearErrors();
    }
  }
</script>

<style src="./Form.css" scoped></style>