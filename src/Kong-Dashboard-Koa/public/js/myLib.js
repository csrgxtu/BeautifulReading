function create() {
  var domain = $('#exampleInputName1').val();
  var path = $('#exampleInputName2').val();

  $.ajax({
    url: 'http://127.0.0.1:8001/apis/',
    type: 'POST',
    async: true,
    data: {target_url: domain, path: path},
    success: function() {
      alert("Successful adding your api ...");
      //document.getElementById("msgBoxtxtsuccess").innerHTML = "Successful adding your api ..."
    },
    error: function() {
      alert("Failure adding your api ...");
      //document.getElementById("msgBoxtxtwarning").innerHTML = "Failure adding your api ..."
    }
  });
}

function read() {
  var size = $('#exampleInputName1').val();
  var offset = $('#exampleInputName2').val();

  $.ajax({
    url: 'http://127.0.0.1:8001/apis/',
    type: 'GET',
    async: true,
    data: {size: size, offset: offset},
    success: function(data) {
      var htmlSnippet = "";
      for (var i = 0; i < data.data.length; i++) {
        htmlSnippet += "<tr>";
        htmlSnippet += "<td>" + data.data[i].id + "</td>";
        htmlSnippet += "<td>" + data.data[i].path + "</td>";
        htmlSnippet += "<td>" + data.data[i].target_url + "</td>";
        htmlSnippet += "<td>" + data.data[i].created_at + "</td>";
        htmlSnippet += "</tr>";
      }
      //alert(htmlSnippet);

      document.getElementById("msgBoxtbody").innerHTML = htmlSnippet;
    },
    error: function() {
      //alert("failure");
    }
  });
}

function update() {
  var id = $('#exampleInputName1').val();
  var target_url = $('#exampleInputName2').val();
  var path = $('#exampleInputName3').val();

  $.ajax({
    url: 'http://127.0.0.1:8001/apis/' + id,
    type: 'PATCH',
    async: false,
    data: {target_url: target_url, path: path},
    success: function() {
      alert("Successful updating your api");
    },
    error: function() {
      alert("Failure updating your api");
    }
  });
}

function deletea() {
  // get the input data
  var id = $('#exampleInputName2').val();

  // use jquery send the delete request
  $.ajax({
    url: 'http://127.0.0.1:8001/apis/' + id,
    type: 'DELETE',
    async: false,
    success: function(result) {
      alert("Successful deleting your api");
    },
    error: function() {
      alert("Failure deleting your api");
    }
  });
}
