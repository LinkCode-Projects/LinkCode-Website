var tiny_script = document.createElement('script');
tiny_script.type='text/javascript';
tiny_script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.appendChild(tiny_script);


tiny_script.onload = function(){
tinymce.init({
        selector: '#id_msg'
      });
      }
