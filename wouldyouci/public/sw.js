//push & notification 하기전에 예제로 만들어봤습니다.
let CACHE_NAME = 'pwa-offline-v1';
let filesToCache = [
    //캐싱할것 
];

//서비스 워커 설치(웹 지원 캐싱)
self.addEventListener('install',function(event){
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then(function(cache){
            return cache.addAll(filesToCache); //pwa 파일에 다 집어 넣어라
        })
        .catch(function(error){
            console.log('caching error : ' + error);
        })
    );
});