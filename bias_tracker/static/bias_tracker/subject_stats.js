'use strict';
/**
 * fill current page with result of search.
 */
function fillSubjectStatsPage(stats) {
  var totalField = $('#total');
  totalField.text(stats.total);
  console.dir(stats.total)
  var inclusionField = $('#inclusion');
  inclusionField.text(stats.inclusion);
  var exclusionField = $('#exclusion');
  exclusionField.text(stats.exclusion);
  // var descriptors = $('#descriptors');
  // descriptors.html(stats.descriptors);
}
/**
 * Fill in the current page with any error encountered.
 */
function fillError(response) {
  var errorP = $('#error');
  errorP.text(response.responseText);
}
/**
 * Clear all of the fillable elements on the current page in preparation for
 * new data.
 */
function emptyResponseElements() {
  var total = $('#total');
  total.empty();
  var inclusion = $('#inclusion');
  inclusion.empty();
  var exclusion = $('#exclusion');
  exclusion.empty();
  var errorP = $('#error');
  errorP.empty();
}
/**
 * Take in source form data, POST, update page in place.
 */
function runSubmitSourceAndUpdate() {
  var sourceForm = $('#subject-form');
  var actionURL = sourceForm.attr('action');
  var formData = sourceForm.serialize();
  $.post(actionURL, formData).
    always(emptyResponseElements).
    done(fillSubjectStatsPage).
    fail(fillError);
}
/**
 * Register form submit event handler.
 */
function registerGlobalEventHandlers() {
  var sourceForm = $('#subject-form');
  console.log('testtesttest');
  sourceForm.on('submit', function(event) {
    event.preventDefault();
    runSubmitSourceAndUpdate();
  });
}
// Register handlers for permanent elements on the page.
$(document).ready(registerGlobalEventHandlers);
