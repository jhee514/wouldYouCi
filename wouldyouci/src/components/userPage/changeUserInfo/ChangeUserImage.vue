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
        <v-btn text @click="closeDialog">저장</v-btn>
        <v-btn text @click="closeDialog">취소</v-btn>
      </v-item-group>
    </v-card-actions>
  </v-card>
</template>

<script>
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
    onFileChange(file) {
      this.image = file;
    },
    closeDialog() {
      this.$emit("changeUserImage", "close");
    },
  }
}
</script>

<style src="./ChangeUserImage.css" scoped></style>