<template>
  <div class="userInfo">
    <img class="userImage" @click="isShow = !isShow" src="../../../assets/basicUserImage.png" />
    <v-dialog v-model="isShow">
      <v-row justify="center">
        <img class="bigUserImage" src="../../../assets/basicUserImage.png" />
      </v-row>
    </v-dialog>
    <span class="userName">userName</span>
  </div>
</template>

<script>
export default {
  name: 'UserInfo',
  data() {
    return {
      isShow: false
    }
  }
}
</script>

<style src="./UserInfo.css" scoped></style>