'use strict';
//
// INPUT
//
/**
 * return user input value.
 */
// function fetchDateInput(){
//     return $("#date").val()
//
// TRANSFORM
//
/**
 * evaluate input, return false if blank
 */
// function checkFieldEmpty(anyObject){
//     if (anyObject !== "") {
//         return false
//     }
//     else {
//         return true
//     }
    // can I use jQuery.isEmptyObject($("#fullName"))?
// }
/**
 * get input, check validity, return false if invalid
 */
// function validateDate(){
//     // var regexLayout = /^(\d{4})(\-)(\d{2})(\-)(\d{2})$/
//     var incidentDate = fetchDateInput()
//     // var regexLayout = /(\d{4})-(\d{2})-(\d{2})/
//     if (checkFieldEmpty(incidentDate) === false && !(incidentDate.match(regexLayout))){
//         return false
//     }
//     else {
//         return true
//     }
// }
// create
//
/**

// modify & sync
//
// main
//
/**
 * get input, check validity, launch warning block
 */
// function runDateCheckMain(){
//     var incidentDate = fetchDateInput();
//     var incidentDateCheckResult = validateDate();
//     updateDateWarning(incidentDateCheckResult)
// }
//
// registerEventHandlers
//
/**
 * register Event Handlers/Callbacks
 */
// function registerInitialCallback(){
//     // $("#fullName").on("change", runNameCheckMain);
//     $("#Date").on("change", runDateCheckMain);
//     // $("#phoneNum").on("change", runPhoneNumCheckMain);
//     $("#submitButton").on("submit", function(event){
//         event.preventDefault();
//         submitButtonEvent
//     })
// }
// registerInitialCallback()
