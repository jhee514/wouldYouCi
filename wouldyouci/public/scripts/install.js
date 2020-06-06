// CODELAB: Add event listener for appinstalled event
window.addEventListener('appinstalled', logAppInstalled);
/**
 * Event handler for appinstalled event.
 *   Log the installation to analytics or save the event somehow.
 *
 * @param {Event} evt
 */
function logAppInstalled(evt) {
  // CODELAB: Add code to log the event
  console.log('Cinema App was installed.', evt);
}


// push 알람

const applicationServerPublicKey = 'BKW2ouzP7qpBa_Gg_enNAq7rGCGAePEha4uaOl-0n5vyLLhRGcACDTrhARKm6ZGMBjRmDV90xC8tnzdvlqAygNQ';
let swRegistration = null;

if('serviceWorker' in navigator && 'PushManager' in window){
  navigator.serviceWorker.register('/sw.js')//serviceWorker등록 
    .then(function(swReg){
        console.log('Service Worker 등록 완료', swReg);
        swRegistration = swReg;
        subscribeUser();
    })
    .catch(function(error){
        console.log('Service Worker 등록 실패', error);
    })
} else {
  console.log('pushmanager is not supported')
}

function subscribeUser() {
  const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
  swRegistration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: applicationServerKey
  })
    .then(function(pushSubscription) {
      // console.log(pushSubscription);
      const jsonSub = JSON.stringify(pushSubscription);
      console.log(jsonSub)
    })
    .catch(err => {
      console.log(err);
      console.log(Notification.permission)
    })
}

function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}