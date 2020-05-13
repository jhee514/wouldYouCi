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
              <v-card-title>Login</v-card-title>
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
                    id="password"
                    label="Password"
                    name="password"
                    prepend-icon="fas fa-lock"
                    type="password"
                    v-model="userInfo.password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click.prevent="login(userInfo)">Submit</v-btn>
                <v-btn @click="setLoginMode">Signup</v-btn>
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
    name: 'LoginForm',
    data() {
      return {
        userInfo: {
          userName: '',
          password: '',
        }
      }
    },
    methods: {
      ...mapMutations(['setLoginMode']),
      ...mapActions(['login'])
    }
  }
</script>

<style></style>