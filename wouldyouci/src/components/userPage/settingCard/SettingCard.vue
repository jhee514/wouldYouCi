<template>
  <v-card>
    <div @click="isShow = !isShow">
      <v-icon>fas fa-user-circle</v-icon>
      프로필 사진 변경
    </div>
    <v-divider></v-divider>
    <div @click="isShow = !isShow">
      <v-icon>fas fa-key</v-icon>
      비밀번호 변경
    </div>
    <v-divider></v-divider>
    <div @click="isShow = !isShow">
      <v-icon>fas fa-sign-out-alt</v-icon>
      로그아웃
    </div>
  </v-card>
</template>

<script>
export default {
  name: 'settingCard',
}
</script>

<style src="./SettingCard.css" scoped></style>