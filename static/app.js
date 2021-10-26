  
// function onClickedEstimatePrice() {
//     console.log("Estimate price button clicked");
//     var sqft = document.getElementById("uiSqft");
//     var bhk = document.getElementById("uiBHK");
//     var bathrooms = document.getElementById("uiBathrooms");
//     var location = document.getElementById("uiLocations");
//     //var estPrice = document.getElementById("uiEstimatedPrice");
  
//     var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
//     // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
//     $.post(url, {
//         total_sqft: parseFloat(sqft.value),
//         bhk: parseInt(bhk.value),
//         bath: parseInt(bathrooms.value),
//         location: location.value
//     },function(data, status) {
//         console.log(data);
//         document.getElementById("uiEstimatedPrice").innerHTML = "<h2>" + data.toString() + " Lakhs</h2>";
//         console.log(status);
//         //window.stop()  // This stops the window from loading again and again.
//     });
//   }




function onPageLoad() {
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get("/get_location_names",function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;