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

document.querySelector('#files').addEventListener('change', (e) =>{
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
})