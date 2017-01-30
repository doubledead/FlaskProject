$( document ).ready(function() {
  console.log("Ready!");

  var params = {};

  function addGuest() {

  }


  function submitForm() {
    var
      deferred = $.Deferred(),
      data = JSON.stringify(params),
      wsUrl = "SomeJSONEndpoint";

    $.ajax({
      cache: false,
      contentType: 'application/json; charset=utf-8',
      accepts: 'application/json',
      url: wsUrl,
      data: data,
      dataType: 'json',
      type: 'POST'
    }).success(function(response) {
      deferred.resolve(response);
      console.log(response);
      $scope.$apply(reset());
    }).fail(function(response) {

    }).done(function(response) {

    });
    return deferred.promise();
  }


});
