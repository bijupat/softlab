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

    document.getElementById('find_fname').addEventListener('change', function () {
        //console.log(document.querySelector('#datesubmit'))
        document.querySelector('#find_name_sub').disabled = false;
        });
    document.getElementById('find_lname').addEventListener('change', function () {
        //console.log(document.querySelector('#datesubmit'))
        document.querySelector('#find_name_sub').disabled = false;
        });
    document.getElementById('find_smpno').addEventListener('change', function () {
        //console.log(document.querySelector('#datesubmit'))
        document.querySelector('#find_smpno_sub').disabled = false;
        });
    document.getElementById('find_mobno').addEventListener('change', function () {
        //console.log(document.querySelector('#datesubmit'))
        document.querySelector('#find_mobno_sub').disabled = false;
        });















  

    
})()

