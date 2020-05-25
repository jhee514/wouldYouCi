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
      기준 반경
      <v-btn outlined small color="#000000" @click="kmSelector=!kmSelector">
        {{ km }}
        <v-icon class="angleDown">fas fa-angle-down</v-icon>
      </v-btn>
      Km
    </div>
    <v-dialog v-model="timeSelector">
      <TimeSelector v-bind:nowTime="time" @targetTime="changeTime"/>
    </v-dialog>
    <v-dialog v-model="kmSelector">
      <KmSelector v-bind:nowKm="km" @targetKm="changeKm"/>
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
      <TheaterMovie v-bind:theaterMovieList="getMovies"/>
    </div>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import TimeSelector from './timeSelector/TimeSelector.vue';
import KmSelector from './timeSelector/KmSelector.vue';
import TheaterMovie from './theaterMovie/TheaterMovie.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'MainMap',
  components: {
    Nav,
    Title,
    TimeSelector,
    KmSelector,
    TheaterMovie
  },
  data() {
    return {
      map: null,
      google: null,
      nowHere: null,
      time: new Date().toLocaleTimeString(),
      km: 3,
      cardInfo: null,
      showMovieCard: null,
      loading: false,
      mapCenter: null,
      timeSelector: false,
      kmSelector: false,
      theaterMovieList: [],
      markers: [],
      // movieList: []
    }
  },
  computed: {
    ...mapGetters(['getTheaterMovies', 'getMovies'])
  },
  methods: {
    ...mapActions(['init', 'bringHereCinema', 'bringMovies']),
    marking(value) {
      console.log(value)
      if (value.type === 'user') {
        const marker = new this.google.maps.Marker({position: value.position, map: this.map, icon: value.icon})
        this.google.maps.event.addListener(marker, 'click', function() {
          if (this.showMovieCard) {
            this.closeMovieCard();
          }
          const infoWindow = new window.google.maps.InfoWindow;
          infoWindow.setPosition({lat: value.position.lat, lng: value.position.lng});
          infoWindow.setContent('현재 위치입니다. 실제 위치와 500m 정도 차이가 날 수 있습니다.');
          infoWindow.open(this.map);
        }.bind(this))
      } else {
        for (const v of value.position) {
          const marker = new this.google.maps.Marker({position: {lat: Number(v.y), lng: Number(v.x)}, map: this.map, icon: value.icon, label:v.name, animation: this.google.maps.Animation.DROP})
          this.markers.push(marker);
          this.google.maps.event.addListener(marker, 'click', async function() {
            console.log(v)
            await this.bringMovies({theaterID: v.id, time: null});
            console.log(this.getMovies);
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
                              '오류: 지리적 위치 서비스가 실패했습니다. 위치 제공을 허용해주세요':
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
    async changeLoading() {
      this.loading = true;
      this.clearMarker();
      const center = this.map.getCenter();
      const centerValue = {lat: center.lat(), lng: center.lng()};
      this.mapCenter = centerValue;
      await this.bringHereCinema({center: centerValue, radius: this.km});
      this.theaterMovieList = this.getTheaterMovies;
      const theaterIcon = {
        url: "https://image.flaticon.com/icons/svg/2892/2892617.svg",
        scaledSize: new this.google.maps.Size(40, 40)
      }
      this.marking({type: 'theater', position: this.theaterMovieList, icon: theaterIcon});
      this.loading = false;
    },
    changeTime(targetTime) {
      this.timeSelector = false;
      this.time = targetTime;
    },
    setNowTime() {
      this.time = new Date().toLocaleTimeString();
    },
    changeKm(targetKm) {
      this.kmSelector = false;
      this.km = targetKm;
      this.changeLoading();
    },
    clearMarker() {
      for (const marker of this.markers) {
        marker.setMap(null);
      }
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
        navigator.geolocation.getCurrentPosition(async function(position) {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          await this.bringHereCinema({center: pos, radius: 3})
          this.theaterMovieList = this.getTheaterMovies;
          console.log(this.theaterMovieList);
          this.nowHere = pos;
          const hereIcon = {
            url : "https://image.flaticon.com/icons/svg/684/684908.svg",
            scaledSize: new this.google.maps.Size(40, 40)
          }
          const theaterIcon = {
            url: "https://image.flaticon.com/icons/svg/2892/2892617.svg",
            scaledSize: new this.google.maps.Size(40, 40)
          }
          this.marking({type: 'user', position: pos, icon: hereIcon});
          this.marking({type: 'theater', position: this.theaterMovieList, icon: theaterIcon});
          this.map.setCenter(pos);
          // let bound = this.map.getBounds();
          // console.log(bound);
          // this.bound = bound;
        }.bind(this), function() {
          this.handleLocationError(true, this.map.getCenter());
        }.bind(this))
      }
    } catch (error) {
      console.log(error);
    }
  }
}
</script>

<style src="./MainMap.css" scoped></style>