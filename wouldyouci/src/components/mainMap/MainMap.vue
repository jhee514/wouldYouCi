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
      기준 영화 정보입니다.
    </div>
    <v-dialog v-model="timeSelector">
      <TimeSelector v-bind:nowTime="time" @targetTime="changeTime"/>
    </v-dialog>
    <div id="map" ref="map">
    </div>
    <v-overlay :value="cardLoading">
      <v-progress-circular
        :size="70"
        :width="7"
        color="#4520EA"
        indeterminate
      ></v-progress-circular>
    </v-overlay>
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
import TheaterMovie from './theaterMovie/TheaterMovie.vue';
import { mapGetters, mapActions } from 'vuex';

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
      time: new Date().toLocaleTimeString(),
      isTimeChange: false,
      cardInfo: null,
      showMovieCard: null,
      loading: false,
      mapBound: null,
      timeSelector: false,
      theaterMovieList: [],
      markers: [],
      theaterId: null,
      cardLoading: false
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
        if (value.position.length) {
          for (const v of value.position) {
            const marker = new this.google.maps.Marker({position: {lat: Number(v.y), lng: Number(v.x)}, map: this.map, icon: value.icon, label:v.name, animation: this.google.maps.Animation.DROP})
            this.markers.push(marker);
            this.google.maps.event.addListener(marker, 'click', async function() {
              console.log(v)
              this.theaterId = v.id;
              this.cardLoading = true;
              console.log(this.theaterId)
              if (this.isTimeChange) {
                await this.bringMovies({theaterID: v.id, time: this.time});
              } else {
                await this.bringMovies({theaterID: v.id, time: null});
              }
              this.cardLoading = false;
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
        else{
          alert('해당 지역에는 영화관이 없습니다.\n지역을 다시 설정해주세요.')
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
      const mapBound = this.map.getBounds();
      this.mapBound = mapBound;
      console.log(mapBound)
      const bound = {
        x1: mapBound.Ua.i,
        y1: mapBound.Ya.i,
        x2: mapBound.Ua.j,
        y2: mapBound.Ya.j
      }
      await this.bringHereCinema(bound);
      this.theaterMovieList = this.getTheaterMovies;
      const theaterIcon = {
        url: "https://image.flaticon.com/icons/svg/2892/2892617.svg",
        scaledSize: new this.google.maps.Size(40, 40)
      }
      this.marking({type: 'theater', position: this.theaterMovieList, icon: theaterIcon});
      this.loading = false;
    },
    async changeTime(targetTime) {
      this.timeSelector = false;
      const targetTimes = targetTime.split(' ');
      const times = targetTime.split(' ')[1].split(':')
      if (targetTimes[0] !== 'null' && times[0] !== 'null' && times[1] !== 'null') {
        this.time = targetTime;
        this.isTimeChange = true;
        if (this.showMovieCard) {
          this.cardLoading = true;
          await this.bringMovies({theaterID: this.theaterId, time: this.time});
          this.cardLoading = false;
        }
      }
    },
    async setNowTime() {
      this.time = new Date().toLocaleTimeString();
      this.isTimeChange = false;
      if (this.showMovieCard) {
        this.cardLoading = true;
        await this.bringMovies({theaterID: this.theaterId, time: null});
        this.cardLoading = false;
      }
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
      console.log(this.google)
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
          this.map.setCenter(pos);
          const bound = {x1: pos.lng - 0.01544952392, y1: pos.lat - 0.01721547104, x2: pos.lng + 0.01544952392, y2: pos.lat + 0.01721150239};
          await this.bringHereCinema(bound);
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