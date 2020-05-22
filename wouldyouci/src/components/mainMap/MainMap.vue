<template>
  <div>
    <Title />
    <div class="time">
      <v-btn text small @click="setNowTime">
        <v-icon small>fas fa-history</v-icon>
      </v-btn>
      <v-btn outlined small color="#000000" @click="timeSelector=!timeSelector">
        {{ time }}
        <v-icon class="angleDown">fas fa-angle-down</v-icon>
      </v-btn>
      기준 영화입니다.
    </div>
    <v-dialog v-model="timeSelector">
      <TimeSelector v-bind:nowTime="time" @targetTime="changeTime"/>
    </v-dialog>
    <div id="map" ref="map">
    </div>
    <div class="nowArea">
      <v-btn v-if="loading" fab height="30" width="30" loading>
        <v-icon small>fas fa-undo-alt</v-icon>
      </v-btn>
      <v-btn @click="changeLoading" v-else fab height="30" width="30">
        <v-icon small>fas fa-undo-alt</v-icon>
      </v-btn>
    </div>
    <div class="movieCard" v-if="showMovieCard">
      <TheaterMovie v-bind:theaterMovieList="theaterMovieList"/>
    </div>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import TimeSelector from './timeSelector/TimeSelector.vue';
import TheaterMovie from './theaterMovie/TheaterMovie.vue';
import { mapActions } from 'vuex';

export default {
  name: 'MainMap',
  components: {
    Nav,
    Title,
    TimeSelector,
    TheaterMovie
  },
  data() {
    return {
      map: null,
      google: null,
      nowHere: null,
      positions: [
        {lat: 37.498, lng: 127.04},
        {lat: 37.500, lng: 127.055},
        {lat: 37.510, lng: 127.06},
        {lat: 37.505, lng: 127.05}
      ],
      time: new Date().toLocaleTimeString(),
      cardInfo: null,
      showMovieCard: null,
      loading: false,
      mapCenter: null,
      timeSelector: false,
      theaterMovieList: ['배고파...', '집이지만', '집에 가고파', '금요일', '불금', '놀고싶다']
    }
  },
  methods: {
    ...mapActions(['init']),
    marking(value) {
      for (const v of value.position) {
        if (value.type === 'user') {
          const marker = new this.google.maps.Marker({position: v, map: this.map, icon: value.icon})
          this.google.maps.event.addListener(marker, 'click', function() {
            if (this.showMovieCard) {
              this.closeMovieCard();
            }
            const infoWindow = new window.google.maps.InfoWindow;
            infoWindow.setPosition({lat: v.lat, lng: v.lng});
            infoWindow.setContent('현재 위치입니다. 실제 위치와 500m 정도 차이가 날 수 있습니다.');
            infoWindow.open(this.map);
          }.bind(this))
        } else {
          const marker = new this.google.maps.Marker({position: v, map: this.map, icon: value.icon, label:'cgv', animation: this.google.maps.Animation.DROP})
          this.google.maps.event.addListener(marker, 'click', function() {
            if (this.cardInfo && this.cardInfo !== marker) {
              this.toggleBounce(this.cardInfo);
              this.toggleBounce(marker);
              this.cardInfo = marker;
              this.showMovieCard = true;
            } else if (!this.cardInfo) {
              this.toggleBounce(marker);
              this.cardInfo = marker;
              this.showMovieCard = true;
            }
          }.bind(this))
        }
      }
    },
    handleLocationError(browserHasGeolocation, pos) {
      const infoWindow = new window.google.maps.InfoWindow;
      infoWindow.setPosition(pos);
      infoWindow.setContent(browserHasGeolocation?
                              '오류: 지리적 위치 서비스가 실패했습니다.':
                              '오류: 브라우저가 지리적 위치를 지원하지 않습니다.');
      infoWindow.open(this.map)
    },
    toggleBounce(marker) {
      if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
        this.cardInfo = null;
      } else {
        marker.setAnimation(window.google.maps.Animation.BOUNCE);
      }
    },
    closeMovieCard() {
      this.showMovieCard = false;
      this.toggleBounce(this.cardInfo);
    },
    changeLoading() {
      this.loading = true;
      setTimeout(function() {
        this.loading = false;
        const center = this.map.getCenter()
        const centerValue = {lat: center.lat(), lng: center.lng()};
        console.log(centerValue)
        this.mapCenter = centerValue;
      }.bind(this), 1000)
    },
    changeTime(targetTime) {
      this.timeSelector = false;
      this.time = targetTime;
    },
    setNowTime() {
      this.time = new Date().toLocaleTimeString();
    }
  },
  async mounted() {
    try {
      console.log(this)
      this.google = await this.init();
      this.map = new this.google.maps.Map(this.$refs.map, {
        center: { lat: 37.501401, lng: 127.039686 },
        zoom: 14,
        disableDefaultUI: true
      });
      this.google.maps.event.addListener(this.map, 'click', function() {
        if (this.showMovieCard) {
          this.closeMovieCard();
        }
      }.bind(this))
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          this.nowHere = pos
          const hereIcon = {
            url : "https://image.flaticon.com/icons/svg/684/684908.svg",
            scaledSize: new this.google.maps.Size(40, 40)
          }
          const theaterIcon = {
            url: "https://image.flaticon.com/icons/svg/2892/2892617.svg",
            scaledSize: new this.google.maps.Size(40, 40)
          }
          this.marking({type: 'user', position: [pos], icon: hereIcon});
          this.marking({type: 'theater', position: this.positions, icon: theaterIcon});
          this.map.setCenter(pos);
          // let bound = this.map.getBounds();
          // console.log(bound);
          // this.bound = bound;
        }.bind(this), function() {
          this.handleLocationError(true, this.map.getCenter());
        })
      }
    } catch (error) {
      console.log(error);
    }
  }
}
</script>

<style src="./MainMap.css" scoped></style>