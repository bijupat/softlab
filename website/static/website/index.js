(function(){

    //hiding all div elements except #homepage
    document.querySelector('#homepage').style.display = "block";
    document.querySelector('#contactus_div').style.display = "none";

    //when concatct us clicked .....
    document.getElementById('contactus_nav').addEventListener('click', function (event) {
        event.preventDefault();
        document.querySelector('#homepage').style.display = "none";
        document.querySelector('#contactus_div').style.display = "block";

    });


    //when home clicked .....
    document.getElementById('home_nav').addEventListener('click', function (event) {
        event.preventDefault();
        document.querySelector('#homepage').style.display = "block";
        document.querySelector('#contactus_div').style.display = "none";

    });




    // on click of delete post fetch done to /deletetest/ route with data as json
    document.querySelectorAll('.deletetest').forEach(function(element){            

        element.addEventListener("click", function(event){

            event.preventDefault();

        
            
        });




            
    });



})()