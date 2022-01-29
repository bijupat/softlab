(function(){
    //hiding both new and old patient divs initially
    document.querySelector('#new_patient').style.display = "none";
    document.querySelector('#old_patient').style.display = "none";

    // on click of new patient button display new patient div
    document.querySelector('#new_pat_btn').addEventListener("click", function(event){
        event.preventDefault(); 
        //displa new patient div
        document.querySelector('#new_patient').style.display = "block";
        //hide old patient div if displayed already
        document.querySelector('#old_patient').style.display = "none";        
    });

    // on click of old patient button display old patient div   
    document.querySelector('#old_pat_btn').addEventListener("click", function(event){
        event.preventDefault(); 
        //displa old patient div
        document.querySelector('#old_patient').style.display = "block";
        //hide new patient div if displayed already
        document.querySelector('#new_patient').style.display = "none";        
    });

   


        document.querySelector('#searchpatdropdwnbtn').addEventListener("click", function(event){
            document.getElementById("myDropdown").classList.toggle("show");
    
    
        });
    
        document.querySelector('#myInput').addEventListener("keyup", function(event){
            //alert("my input clicked");
            var input, filter, ul, li, a, i;
            input = document.getElementById("myInput");
            filter = input.value.toUpperCase();
            //alert(filter);
            div = document.getElementById("myDropdown");
            a = div.getElementsByTagName("a");
            for (i = 0; i < a.length; i++) {
              txtValue = a[i].textContent || a[i].innerText;
              if (txtValue.toUpperCase().indexOf(filter) > -1) {
                a[i].style.display = "";
              } else {
                a[i].style.display = "none";
              }
            }
    
        });
    











  

    
})()

