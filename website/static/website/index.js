(function(){

    //hiding all div elements except #homepage    
    document.querySelectorAll('.divmenu').forEach(function(element){
        element.style.display = "none";
    });
    document.querySelector('#divhome').style.display = "block";

    
    // all navbar.menu has class="navmenu" and data-divid = "div{nameofmenu}"
    // all oody > div.meny has class="divmenu" and id = "div{nameofmenu}"
    // on click of menu in navbar all  body > div.menu gets hidden(none) and body > div#divmenu{nameofmenu} gets displayed(block)
    document.querySelectorAll('.navmenu').forEach(function(element){            

        element.addEventListener("click", function(event){

            event.preventDefault();
            //alert(element.innerHTML);
            // all body > div dislpay set to none
            document.querySelectorAll('.divmenu').forEach(function(element){
                element.style.display = "none";
            });
            // get id of div to be displayed from dataset attr of element
            let id = element.dataset.divid;
            console.log(id);
            document.querySelector(`#${id}`).style.display = "block";

        });
            
    });



})()