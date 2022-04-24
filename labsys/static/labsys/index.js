(function(){

    document.getElementById('date_select').addEventListener('change', function () {
        //console.log(document.querySelector('#datesubmit'))
        //alert("datechanged")
        document.querySelector('#datesubmit').disabled = false;
    });

    


//hiding item  in small screen sizes with class largescreen and vice versa

window.onresize = reportWindowSize;
window.onload = reportWindowSize;
function reportWindowSize() {
    if (window.innerWidth < 1000) {
        document.querySelectorAll('.largescreen').forEach(function(element){
            element.style.display = "none";
        });
        document.querySelectorAll('.smallscreen').forEach(function(element){
            element.style.display = "block";
        });

    }
    else{
        document.querySelectorAll('.largescreen').forEach(function(element){
            element.style.display = "block";
        });
        document.querySelectorAll('.smallscreen').forEach(function(element){
            element.style.display = "none";
            console.log(element)
        });
    }
    
}


    
    
    
        
})()

