function validatePhoneNumber(e) {
  var pNumber = document.getElementById('number').value;
  if (!phoneRegex(pNumber)) {
   document.getElementById('error').classList.add('msg');
   alert("submitted");
  }
  else {
   document.getElementById('error').classList.remove('msg');
  }
  e.preventDefault();
 }
 function fun(){
     alert('successful')
 }
 