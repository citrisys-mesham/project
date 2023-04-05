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
 

//  image page

/*document.querySelector('#files').addEventListener('change', (e) =>{
  if(window.File && window.FileReader && window.FileList && window.Blob){
      const files = e.target.files;
      const output = document.querySelector('#result');

      for(let i=0;i< files.length;i++){
          if(!files[i].type.match("image")) continue;
          const picReader = new FileReader();
          picReader.addEventListener("load",function(event){
              const picFile =event.target;
              const div =document.createElement('div');
              div.innerHTML = `<img class="thumbnail" src="${picFile.result}" tittle="${picFile.name}"/>`
              output.appendChild(div);
          })
          picReader.readAsDataURL(files[i]);
      }
  }else{
      alert('browser does not support')
  }
})*/



  
document.getElementById("signup-form").addEventListener("submit", function(event) {
    var username = document.getElementsByName("username")[0].value;
    var email = document.getElementsByName("email")[0].value;
    var password = document.getElementsByName("password")[0].value;
    var confirmPassword = document.getElementsByName("confirm_password")[0].value;
    var errors = false;
    
    // Validate username
    if (username.trim() === "") {
        document.getElementById("username-error").style.display = "block";
        errors = true;
    } else {
        document.getElementById("username-error").style.display = "none";
    }
    
    // Validate email
    if (email.trim() === "") {
        document.getElementById("email-error").style.display = "block";
        errors = true;
    } else {
        document.getElementById("email-error").style.display = "none";
    }
    
    // Validate password
    if (password.trim() === "") {
        document.getElementById("password-error").style.display = "block";
        errors = true;
    } else {
        document.getElementById("password-error").style.display = "none";
        
        if (password.length < 8) {
            document.getElementById("password-length-error").style.display = "block";
            errors = true;
        } else {
            document.getElementById("password-length-error").style.display = "none";
        }
    }
    if (confirmPassword.trim() === "") {
        document.getElementById("confirm-password-error").style.display = "block";
        errors = true;
    } else {
        document.getElementById("confirm-password-error").style.display = "none";
        
        if (confirmPassword !== password) {
            document.getElementById("compare-password-error").style.display = "block";
            errors = true;
        } else {
            document.getElementById("compare-password-error").style.display = "none";
        }
    }

    if (errors) {
        event.preventDefault();
    }
});
   