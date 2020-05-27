<template>
  <div class="userInfo">
    <img v-if="UserProfile" class="userImage" @click="isShow = !isShow" :src="UserProfile" />
    <img v-else class="userImage" @click="isShow = !isShow" src="../../../assets/basicUserImage.png" />
    <v-dialog v-model="isShow">
      <v-row justify="center">
        <div v-if="UserProfile">
          <img class="bigUserImage canSee" :src="UserProfile" />
          <v-btn text small class="btnTrash" @click="deleteP"><v-icon>fas fa-trash</v-icon></v-btn>
        </div>
        <img v-else class="bigUserImage" src="../../../assets/basicUserImage.png" />
      </v-row>
    </v-dialog>
    <span class="userName">{{ UserName }}</span>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'UserInfo',
  props: ['UserName', 'UserProfile'],
  data() {
    return {
      isShow: false
    }
  },
  methods: {
    ...mapActions(['deleteProfile', 'bringUserInfo']),
    async deleteP() {
      this.isShow = false;
      await this.deleteProfile();
      this.$emit("deleteP");
    }
  },
}
</script>

<style src="./UserInfo.css" scoped></style>