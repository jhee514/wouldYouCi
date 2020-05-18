<template>
  <div class='search'>
    search
    <div class ="grid">
      <div class="header">
        🍿우리 주변의 씨네마<br/>
        현재위치 
      </div>

      <div class="search">
        
         <v-form v-model="valid">
      <v-container>
            <v-text-field
              v-model="firstname"
              prepend-icon="fa fa-search"
              :rules="rules"
              :counter="10"
              label="영화관을 찾아보세요!"
              required
            ></v-text-field>
      </v-container>
     </v-form> 
      </div>
      <div class="content">
        근처 영화관<br/>


        현재 사영작 순위<br/>

        개봉예정작<br/>

      </div>
      <div class="nav">
      

      </div>
      <div class="footer">
        Would Ci !

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Search',
   data: () => ({
    rules: [
      value => !!value || '영화관을 검색해보세요!',
      value => (value || '').length <= 20 || '최대 글자수는 20글자 입니다.',
      value => {
        const pattern =  /([^가-힣ㄱ-ㅎㅏ-ㅣ\x20])/i
        return !pattern.test(value) || '한글만 적어주세요.'
      },
    ],
  }),

}
</script>

<style src="./Search.css" scoped></style>