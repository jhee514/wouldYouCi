<template>
  <v-card class="changeUserPass">
    <v-card-text>
      <p>
        아이디
      </p>
      <h3>
        userName
      </h3>
      <v-text-field
        label="New Password"
        prepend-icon="fas fa-lock"
        type="password"
        v-model="userInfo.password"
        :rules="[rules.required]"
      ></v-text-field>
      <v-text-field
        label="Password Confirmation"
        prepend-icon="fas fa-lock"
        type="password"
        v-model="userInfo.passwordConfirm"
        :rules="[rules.required, rules.passwordMatch]"
      ></v-text-field>
    </v-card-text>
    <v-card-actions>
      <v-item-group>
        <v-btn text @click="closeDialog">변경</v-btn>
        <v-btn text @click="closeDialog">취소</v-btn>
      </v-item-group>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'changeUserPass',
  data() {
    return {
      userInfo: {
        password: null,
        passwordConfirm: null
      },
      rules: {
        required: value => !!value || '필수 항목입니다.',
        passwordMatch: value => value === this.userInfo.password || '비밀번호가 일치하지 않습니다.'
      }
    }
  },
  methods: {
    closeDialog() {
      this.$emit("changeUserPass", false);
    }
  }
}
</script>

<style src="./ChangeUserPass.css" scoped></style>