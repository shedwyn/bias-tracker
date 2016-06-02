'use strict';
/**
 * fills or deletes message based on 'trigger' value.
 */
function triggerHiddenText() {
  if ($('#trigger') === 'submit_new') {
    $('#newIncidentMessage').removeClass('invisible');
  }  else {
    $('#newIncidentMessage').addClass('invisible');
  }
}



//
// transform
//
// create
//
// modify & sync
//
// main
//
// registerEventHandlers
