(function(){

    document.getElementById('date_select').addEventListener('change', function () {
        //console.log(document.querySelector('#datesubmit'))
        //alert("datechanged")
        document.querySelector('#datesubmit').disabled = false;
    });

    


//hiding item with class largescreen in small screen sizes

window.onresize = reportWindowSize;
window.onload = reportWindowSize;
function reportWindowSize() {
    if (window.innerWidth < 1000) {
        document.querySelectorAll('.largescreen').forEach(function(element){
            element.style.display = "none";
        });
    }
    else{
        document.querySelectorAll('.largescreen').forEach(function(element){
            element.style.display = "block";
        });
    }
    
}


    
    
    
        
})()

