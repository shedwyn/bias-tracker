'use strict';
/**
* Take item (descriptor or subject), return one <li> element complete.
*/
function createListItem(listItem) {
  var liElement =
    '<li><mark>' +
    listItem +
    '</mark></li>';
  return liElement;
}
/**
 * fill current page with result of search.
 */
function fillIncidentPage(stats) {
  var filingDate = $('#filing-date');
  filingDate.text(stats.filing_date);
  var incidentDate = $('#incident-date');
  incidentDate.text(stats.incident_date);
  var incidentTime = $('#incident-time');
  incidentTime.text(stats.incident_time);
  var subjectsArea = $('#subjects-list');
  var subjectArray = stats.subjects;
  for (var i = 0; i < subjectArray.length; i += 1) {
    var liElement = createListItem(subjectArray[i]);
    subjectsArea.append(liElement);
  }
  var incidentType = $('type');
  incidentType.text(stats.incident_type);
  var descriptorsArea = $('#descriptors-list');
  var descriptorArray = stats.descriptors;
  for (var i = 0; i < descriptorArray.length; i += 1) {
    var liElement = createListItem(descriptorArray[i]);
    descriptorsArea.append(liElement);
  }
  var textDescription = $('#text-description');
  textDescription.text(stats.text_description);
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
  var filingDate = $('#filing-date');
  filingDate.empty();
  var incidentDate = $('#incident-date');
  incidentDate.empty();
  var incidentTime = $('#incident-time');
  incidentTime.empty();
  var subjectsList = $('#subjects-list');
  subjectsList.empty();
  var incidentType = $('type');
  incidentType.empty();
  var descriptorsList = $('#descriptors-list');
  descriptorsList.empty();
  var textDescription = $('#text-description');
  textDescription.empty();
  var errorP = $('#error');
  errorP.empty();
}
/**
 * Take in source form data, POST, update page in place.
 */
function runSubmitSourceAndUpdate() {
  var sourceForm = $('#incident-form');
  var actionURL = sourceForm.attr('action');
  var formData = sourceForm.serialize();
  $.post(actionURL, formData).
    always(emptyResponseElements).
    done(fillIncidentPage).
    fail(fillError);
}
/**
 * Register form submit event handler.
 */
function registerGlobalEventHandlers() {
  var sourceForm = $('#incident-form');
  sourceForm.on('submit', function(event) {
    event.preventDefault();
    runSubmitSourceAndUpdate();
  });
}
// Register handlers for permanent elements on the page.
$(document).ready(registerGlobalEventHandlers);
