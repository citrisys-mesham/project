
$(document).ready(function(){
  $('#submitBtn').click(function(){
  alert("hello");

  var name = $('#pro_name').val();
  var desc = $('#pro_desc').val();
  var image = $('#myFileInput').val();
  var room1 = $('#room1-type').val();
  var room2 = $('#room1-beds').val();
  var room3 = $('#room1-rating').val();
  var address = $('#Ad').val();
  var street = $('#st').val();
  var city = $('#city').val();
  var pin = $('#pin').val();
  var state= $('#state').val();
  var email = $('#email').val();
  var phone = $('#phoneNo').val();

  var data1 = {"name": name,
                "descrption": desc, 
                "image":image,
                "type":room1,
                "beds":room2,
                "rate":room3,
                "address":address,
                "street":street,
                "city":city,
                "pin":pin,
                "state":state,
                "email": email,
              "phone":phone};
 
  $.ajax({
    type: "POST",
    dataType: 'json',
    url: 'http://localhost:5000/api/property',
    data:data1,

    success: function(result) {
      $('#pro_name-div').text(result.pro_name);
      $('#pro_desc-div').text(result.desc);
      $('#myFileInput-div').text(result.image);
      $('#room1-type-div').text(result.room2);
      $('#room1-beds-div').text(result.room2);
      $('#room1-rating-div').text(result.room3);
      $('#Ad-div').text(result.address);
      $('#st-div').text(result.street);
      $('#city-div').text(result.city);
      $('#pin-div').text(result.pin);
      $('#state-div').text(result.state);
      $('#email-div').text(result.email);
      $('#phoneNo-div').text(result.phone);
     
    },
  });
});
});

function uploadFile() {
    var input = document.getElementById("myFileInput");
    var file = input.files[0];
    var sizeInBytes = file.size;
    var maxSizeInBytes = 1024 * 1024; 
  
    if (sizeInBytes > maxSizeInBytes) {
      alert("File size exceeds the maximum limit of 1 MB");
      input.value = null;
    } else {
       alert("Upload the file")
    }
  }
  const emailInput = document.getElementById("email");
const submitButton = document.getElementById("submit-btn");

submitButton.addEventListener("click", function() {
  if (emailInput.checkValidity()) {
    alert("Valid email address entered!");
  } else {
    alert("Please enter a valid email address.");
  }
});

  function validateNumber(input) {
          var re = /^(\d{3})[- ]?(\d{3})[- ]?(\d{4})$/
  
          return re.test(input)
        }
  
        function validateForm(event) {
          var number = document.getElementById('phoneNo').value
          if (!validateNumber(number)) {
            alert('Please enter a valid number')
            const ele = document.getElementById('result')
            ele.innerHTML = 'Validation Failed'
            ele.style.color = 'red'
          } else {
            const ele = document.getElementById('result')
            ele.innerHTML = 'Validation Successful'
            ele.style.color = 'green'
          }
          event.preventDefault()
        }
  
        document.getElementById('myform').addEventListener('submit', validateForm)
  
 var addRoomButton = document.getElementById("add-room");
  
  addRoomButton.addEventListener("click", function() {
    var roomsContainer = document.getElementById("rooms-container");
    var roomCount = roomsContainer.querySelectorAll(".room").length;
  
    var newRoom = document.createElement("div");
    newRoom.className = "room";
  
    var roomType = document.createElement("input");
    roomType.type = "text";
    roomType.id = "room" + (roomCount + 1) + "-type";
    roomType.name = "room-type[]";
  
    var bedCount = document.createElement("input");
    bedCount.type = "number";
    bedCount.id = "room" + (roomCount + 1) + "-beds";
    bedCount.name = "room-beds[]";
  
    var rating = document.createElement("input");
    rating.type = "number";
    rating.id = "room" + (roomCount + 1) + "-rating";
    rating.name = "room-rating[]";
  
    var removeButton = document.createElement("button");
    removeButton.className = "remove-room";
    removeButton.type = "button";
    removeButton.textContent = "Remove Room";
  
  
    newRoom.appendChild(roomType);
    newRoom.appendChild(bedCount);
    newRoom.appendChild(rating);
    newRoom.appendChild(removeButton);
  
    roomsContainer.appendChild(newRoom);
  
    removeButton.addEventListener("click", function() {
      newRoom.remove();
    });
    
  
  });
  
