<template>
  <v-app id="inspire">
    <v-content>
      <v-container
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card>
              <v-card-title>Signup</v-card-title>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Id"
                    name="Id"
                    prepend-icon="fas fa-user"
                    type="text"
                    v-model="userInfo.userName"
                  ></v-text-field>
                  <v-text-field
                    id="email"
                    label="email"
                    name="email"
                    prepend-icon="fas fa-envelope"
                    type="email"
                    v-model="userInfo.email"
                  ></v-text-field>
                  <v-text-field
                    id="password"
                    label="Password"
                    name="password"
                    prepend-icon="fas fa-lock"
                    type="password"
                    v-model="userInfo.password"
                  ></v-text-field>
                  <v-text-field
                    id="passwordConfirm"
                    label="Password Confirmation"
                    name="passwordConfirm"
                    prepend-icon="fas fa-lock"
                    type="password"
                    v-model="userInfo.passwordConfirm"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click.prevent='signup(userInfo)'>Submit</v-btn>
                <v-btn @click='setLoginMode'>Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import { mapMutations, mapActions } from 'vuex';
  export default {
    name: 'SignupForm',
    data() {
      return {
        userInfo: {
          userName: '',
          email: '',
          password: '',
          passwordConfirm: ''
        }
      }
    },
    methods: {
      ...mapMutations(['setLoginMode']),
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>