'use strict';
/**
* Take in descriptor and count list item pair, create one list item from each
* array item which will have two parts - the descriptor name and it's count.
*/
function createListItem(descriptorArrayPair) {
  var descriptor = descriptorArrayPair.descriptor;
  var count = descriptorArrayPair.count;
  var liElement = '<li><u>' +
  descriptor +
  '</u> used <u>' +
  count +
  '</u> time(s)</li>';
  return liElement;
}
/**
 * fill current page with result of search.
 */
function fillSubjectStatsPage(stats) {
  var subjectName = $('#subject-name');
  subjectName.text(stats.subName);
  var totalField = $('#total');
  totalField.text(stats.total);
  var inclusionField = $('#inclusion');
  inclusionField.text(stats.inclusion);
  var exclusionField = $('#exclusion');
  exclusionField.text(stats.exclusion);
  var descriptorsArea = $('#descriptorsList');
  var descriptorArray = stats.descriptors;
  for (var i = 0; i < descriptorArray.length; i += 1) {
    var liElement = createListItem(descriptorArray[i]);
    descriptorsArea.append(liElement);
  }
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
  var descriptor = $('#descriptorsList');
  descriptor.empty();
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
  sourceForm.on('submit', function(event) {
    event.preventDefault();
    runSubmitSourceAndUpdate();
  });
}
// Register handlers for permanent elements on the page.
$(document).ready(registerGlobalEventHandlers);
