<template>
  <v-card class="changeUserImage">
    <v-file-input
      class="userImage"
      label="프로필 사진"
      prepend-icon="fas fa-camera"
      @change="onFileChange"
      ref="fileInput"
    >
    </v-file-input>
    <v-img
      class="prev"
      :src="showImage"
      small-chips accept="image/*"
      clearable
    >
    </v-img>
    <v-card-actions>
      <v-item-group>
        <v-btn text @click="change(image)">저장</v-btn>
        <v-btn text @click="closeDialog">취소</v-btn>
      </v-item-group>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: 'changeUserImage',
  data() {
    return {
      image: null
    }
  },
  computed: {
    showImage() {
      if (this.image) {
        const url = URL.createObjectURL(this.image)
        return url
      }
      return require("../../../assets/stars.png")
    }
  },
  methods: {
    ...mapActions(['registerProfile']),
    onFileChange(file) {
      this.image = file;
    },
    closeDialog() {
      this.$emit("changeUserImage");
    },
    async change(image) {
      if (image) {
        await this.registerProfile(image);
        this.$emit("changeP");
        this.$emit("changeUserImage");
      } else {
        alert('사진을 등록해주세요.')
      }
    }
  }
}
</script>

<style src="./ChangeUserImage.css" scoped></style>