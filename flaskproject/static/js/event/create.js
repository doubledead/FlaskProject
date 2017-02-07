$( document ).ready(function() {
  console.log("Ready!");

  var
    guestId = 0,
    itemId = 0;

  var params = {
    guests: [],
    items: []
  };

  function addGuestRow(email) {
    guestId++;

    var guestRow = {
      id: guestId,
      email: email
    };

    params.guests.push(guestRow);
  }

  function removeGuestRow(guestId) {
    for (var i = 0; i < params.guests.length; i++) {
      if (params.guests[i].id === guestId) {
        params.guests.splice(i, 1);
        break;
      }
    }
  }

  function addItemRow(name, quantity) {
    itemId++;

    var itemRow = {
      id: itemId,
      name: name,
      quantity: quantity
    };

    params.items.push(itemRow);
  }

  function removeItemRow(itemId) {
    for (var i = 0; i < params.items.length; i++) {
      if (params.items[i].id === itemId) {
        params.items.splice(i, 1);
        break;
      }
    }
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
