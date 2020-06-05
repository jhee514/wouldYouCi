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
