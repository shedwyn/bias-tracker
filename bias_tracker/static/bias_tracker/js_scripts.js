'use strict';
/**
 * fills or deletes message based on 'trigger' value.
 */
function triggerHiddenText() {
  if ($('#trigger') === 'default') {
    $('newIncidentMessage').toggleClass('invisible');
  }
  else if ($('#trigger') === 'submit_new') {
    $('newIncidentMessage').toggleClass('invisible');
  }
}
