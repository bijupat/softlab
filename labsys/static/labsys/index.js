(function(){

    document.getElementById('date_select').addEventListener('change', function () {
        //console.log(document.querySelector('#datesubmit'))
        //alert("datechanged")
        document.querySelector('#datesubmit').disabled = false;
    });

    



window.onresize = reportWindowSize;


function reportWindowSize() {
    console.log (window.innerWidth)
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

